import { type ReactNode, useEffect, useRef, useState } from 'react'
import { A2UISurface, applyA2UILine, createEmptySurface } from './a2ui-engine/A2UIRuntime'
import { buildA2UILines } from './a2ui-engine/buildA2UILines'
import { FloatingAssistant, type FloatingAssistantMessage } from './components'
import {
  askQuestion,
  fetchAppConfig,
  fetchHealth,
  fetchKnowledgeBases,
  fetchStrategies,
  fetchVisualizations,
  runOcrCorrection,
  uploadDocument,
  type AppConfig,
  type KnowledgeBase,
  type OcrCorrectionResult,
  type OrchestrationStep,
  type RagStrategy,
  type VisualizationInstruction,
} from './services/api'
import { createId, type ChatMessage } from './types'

const starterQuestions = [
  '查询 2050 年火星位置，要求精度小于 10^-6',
  '切比雪夫插值为什么适合 DE440？',
  '绘制 2050 年火星 VSOP 和 DE440 对照图',
]

const visualIntentMarkers = ['可视化', '展示', '绘制', '画', '图', '图示', '示意图', '演示', '模拟', '动画', '交互', 'visualize', 'show me', 'diagram', 'demo']
const planetComputeMarkers = ['vsop', 'de440', '星历', '行星位置', '精度', '误差', '坐标', '速度']
const visualizationStoragePrefix = 'universe-model-viz:'
const ocrWorkbenchSample = `| 变量 | 公式 |
|---|---|
| w | $2 7$ |

算法 1
if x > 0
  return y 2
else
  return 0`

function hasExplicitVisualizationIntent(text: string) {
  const lowered = text.toLowerCase()
  return visualIntentMarkers.some((marker) => lowered.includes(marker))
}

function wantsPlanetCalculation(text: string) {
  const lowered = text.toLowerCase()
  return planetComputeMarkers.some((marker) => lowered.includes(marker))
}

function buildRuntimeStages(useRag: boolean, question: string): OrchestrationStep[] {
  const wantsVisual = hasExplicitVisualizationIntent(question)
  const wantsCalculation = wantsPlanetCalculation(question)
  return [
    { id: 'intent', label: '确定任务意图', status: 'pending' },
    ...(wantsCalculation ? [{ id: 'calculation', label: 'Python 数值计算', status: 'pending' } as OrchestrationStep] : []),
    { id: 'retrieval', label: useRag ? '检索选定知识库' : '优先检索本地资料', status: 'pending' },
    ...(wantsVisual ? [{ id: 'visualizer', label: '匹配 A2UI 能力', status: 'pending' } as OrchestrationStep] : []),
    { id: 'generation', label: '生成文字解释', status: 'pending' },
    ...(wantsVisual ? [{ id: 'validation', label: '校验并交给前端渲染', status: 'pending' } as OrchestrationStep] : []),
  ]
}

function suggestKbId(filename: string): string {
  const stem = filename.replace(/\.[^.]+$/, '')
  const parts = stem.split(/[\s._\-()（）【】\[\]、，,]+/).filter(Boolean)
  return parts.slice(0, 2).join('-') || 'default'
}

function buildSurfaceFromVisualizations(items: VisualizationInstruction[]) {
  const renderableItems = items.filter((item) => item.a2uiInstruction?.componentId)
  if (renderableItems.length > 1) {
    const components = [
      {
        id: 'gallery-root',
        component: {
          Column: {
            children: { explicitList: renderableItems.map((item) => `viz-${item.id}`) },
          },
        },
      },
      ...renderableItems.map((item) => {
        const instruction = item.a2uiInstruction!
        return {
          id: `viz-${item.id}`,
          component: {
            [instruction.componentId]: {
              ...(instruction.initialProps ?? {}),
              title: item.title,
              description: item.description,
              componentId: instruction.componentId,
              intentType: instruction.intentType,
              pageId: item.pageId,
              embedUrl: item.embedUrl || instruction.fallback?.embedUrl,
              galleryUrl: item.galleryUrl || instruction.fallback?.galleryUrl,
              implementationKind: item.implementationKind,
              fallback: instruction.fallback,
            },
          },
        }
      }),
    ]
    return applyA2UILine(
      applyA2UILine(createEmptySurface(), JSON.stringify({ surfaceUpdate: { surfaceId: 'main', components } })),
      JSON.stringify({ beginRendering: { surfaceId: 'main', root: 'gallery-root' } }),
    )
  }

  let surface = createEmptySurface()
  const lines = items.flatMap((item) => buildA2UILines(item))
  for (const line of lines) {
    surface = applyA2UILine(surface, line)
  }
  return surface
}

function storeVisualizationForWindow(item: VisualizationInstruction) {
  const id = `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`
  window.localStorage.setItem(`${visualizationStoragePrefix}${id}`, JSON.stringify(item))
  return id
}

function buildVisualizationWindowUrl(id: string) {
  const url = new URL(window.location.href)
  url.search = ''
  url.hash = ''
  url.searchParams.set('viz', id)
  return url.toString()
}

function buildGalleryPageUrl() {
  const url = new URL(window.location.href)
  url.search = ''
  url.hash = ''
  url.searchParams.set('gallery', '1')
  return url.toString()
}

function buildOcrWorkbenchUrl() {
  const url = new URL(window.location.href)
  url.search = ''
  url.hash = ''
  url.searchParams.set('ocr', '1')
  return url.toString()
}

function loadVisualizationFromWindow(id: string): VisualizationInstruction | null {
  const raw = window.localStorage.getItem(`${visualizationStoragePrefix}${id}`)
  if (!raw) return null
  try {
    return JSON.parse(raw) as VisualizationInstruction
  } catch {
    return null
  }
}

function stageLabel(status: OrchestrationStep['status']) {
  if (status === 'completed') return '完成'
  if (status === 'running') return '进行中'
  if (status === 'skipped') return '跳过'
  return '等待'
}

function formatJson(value: unknown) {
  return JSON.stringify(value, null, 2)
}

function truncateText(value: string, limit = 220) {
  const compact = value.trim()
  if (compact.length <= limit) return compact
  return `${compact.slice(0, limit - 3)}...`
}

function readFileAsDataUrl(file: File) {
  return new Promise<string>((resolve, reject) => {
    const reader = new FileReader()
    reader.onload = () => resolve(String(reader.result || ''))
    reader.onerror = () => reject(reader.error || new Error('读取图片失败'))
    reader.readAsDataURL(file)
  })
}

function renderInlineMarkdown(text: string) {
  const nodes: ReactNode[] = []
  const tokenPattern = /(\${1,2}[^$]+\${1,2}|\*\*[^*]+\*\*|`[^`]+`)/g
  let cursor = 0
  let match: RegExpExecArray | null

  while ((match = tokenPattern.exec(text))) {
    if (match.index > cursor) nodes.push(text.slice(cursor, match.index))
    const token = match[0]
    const key = `${match.index}-${token}`

    if (token.startsWith('**') && token.endsWith('**')) {
      nodes.push(<strong key={key}>{token.slice(2, -2)}</strong>)
    } else if (token.startsWith('`') && token.endsWith('`')) {
      nodes.push(<code key={key}>{token.slice(1, -1)}</code>)
    } else {
      nodes.push(
        <span className="markdown-math" key={key}>
          {token.replace(/^\${1,2}|\${1,2}$/g, '')}
        </span>,
      )
    }

    cursor = match.index + token.length
  }

  if (cursor < text.length) nodes.push(text.slice(cursor))
  return nodes
}

function MarkdownExcerpt({ content }: { content: string }) {
  const blocks = content
    .replace(/\r\n/g, '\n')
    .split(/\n+/)
    .map((line) => line.trim())
    .filter(Boolean)

  if (!blocks.length) return <p className="markdown-muted">暂无正文片段。</p>

  const renderedBlocks: ReactNode[] = []
  let fencedCode: string[] = []

  const flushCode = (key: string) => {
    if (!fencedCode.length) return
    renderedBlocks.push(<pre key={key}>{fencedCode.join('\n')}</pre>)
    fencedCode = []
  }

  blocks.forEach((line, index) => {
    const key = `${index}-${line.slice(0, 24)}`

    if (line.startsWith('```')) {
      const rest = line.replace(/^```[a-zA-Z0-9_-]*/, '').trim()
      if (fencedCode.length) {
        if (rest) fencedCode.push(rest)
        flushCode(key)
      } else if (rest) {
        fencedCode = [rest]
      } else {
        fencedCode = ['']
      }
      return
    }

    if (fencedCode.length) {
      fencedCode.push(line)
      return
    }

    const heading = line.match(/^(#{1,6})\s+(.+)$/)
    if (heading) {
      const level = Math.min(heading[1].length, 3)
      renderedBlocks.push(
        <p className={`markdown-heading level-${level}`} key={key}>
          {renderInlineMarkdown(heading[2])}
        </p>,
      )
      return
    }

    if (/^[-*_]{3,}$/.test(line)) {
      renderedBlocks.push(<hr key={key} />)
      return
    }

    const listItem = line.match(/^([-*+]|\d+[.)])\s+(.+)$/)
    if (listItem) {
      renderedBlocks.push(
        <p className="markdown-list-item" key={key}>
          <span>{listItem[1]}</span>
          <span>{renderInlineMarkdown(listItem[2])}</span>
        </p>,
      )
      return
    }

    renderedBlocks.push(<p key={key}>{renderInlineMarkdown(line)}</p>)
  })

  flushCode('final-code-block')

  return (
    <div className="markdown-excerpt">
      {renderedBlocks}
    </div>
  )
}

function PipelineStatus({
  steps,
  activeIndex,
  loading,
}: {
  steps: OrchestrationStep[]
  activeIndex?: number
  loading?: boolean
}) {
  const visibleSteps = loading ? steps.slice(0, Math.min(steps.length, (activeIndex ?? 0) + 1)) : steps
  const resolved = visibleSteps.map((step, index) => ({
    ...step,
    status: (loading
      ? index < (activeIndex ?? 0)
        ? 'completed'
        : index === activeIndex
          ? 'running'
          : 'pending'
      : step.status) as OrchestrationStep['status'],
  }))

  return (
    <div className="pipeline-card">
      <p className="eyebrow">Orchestration</p>
      <div className="pipeline-steps">
        {resolved.map((step) => (
          <div className={`pipeline-step ${step.status}`} key={step.id}>
            <span />
            <div>
              <strong>{step.label}</strong>
              <small>{step.detail || stageLabel(step.status)}</small>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

function VisualizationFrame({ item }: { item: VisualizationInstruction }) {
  const [standaloneHref] = useState(() => buildVisualizationWindowUrl(storeVisualizationForWindow(item)))

  return (
    <section className="visualization-frame">
      <div className="visualization-toolbar">
        <span>{item.title}</span>
        <a href={standaloneHref} rel="noreferrer" target="_blank">
          新窗口打开
        </a>
      </div>
      <A2UISurface surface={buildSurfaceFromVisualizations([item])} />
    </section>
  )
}

function MessageVisualizations({ items }: { items: VisualizationInstruction[] }) {
  if (!items.length) return null
  return (
    <div className="message-visualization">
      {items.map((item) => (
        <VisualizationFrame item={item} key={item.id} />
      ))}
    </div>
  )
}

function StandaloneVisualizationPage({ item }: { item: VisualizationInstruction | null }) {
  return (
    <main className="standalone-viz-page">
      <section className="standalone-viz-shell">
        <div className="standalone-viz-head">
          <div>
            <p className="eyebrow">A2UI Standalone</p>
            <h1>{item?.title ?? '未找到可视化组件'}</h1>
          </div>
          <button type="button" onClick={() => window.close()}>
            关闭窗口
          </button>
        </div>
        {item ? (
          <A2UISurface surface={buildSurfaceFromVisualizations([item])} />
        ) : (
          <p className="muted">这个可视化指令不存在或已经被浏览器清理，请回到对话中重新打开。</p>
        )}
      </section>
    </main>
  )
}

function OcrWorkbenchPage() {
  const galleryHref = buildGalleryPageUrl()
  const appHref = new URL(window.location.href)
  appHref.search = ''
  appHref.hash = ''

  const [config, setConfig] = useState<AppConfig | null>(null)
  const [provider, setProvider] = useState('yunwu-openai')
  const [markdown, setMarkdown] = useState(ocrWorkbenchSample)
  const [dryRun, setDryRun] = useState(true)
  const [maxCandidates, setMaxCandidates] = useState(8)
  const [imageName, setImageName] = useState('')
  const [imageDataUrl, setImageDataUrl] = useState('')
  const [pageNumber, setPageNumber] = useState('1')
  const [loading, setLoading] = useState(false)
  const [status, setStatus] = useState('正在读取当前配置...')
  const [result, setResult] = useState<OcrCorrectionResult | null>(null)

  useEffect(() => {
    fetchAppConfig()
      .then((nextConfig) => {
        setConfig(nextConfig)
        setProvider(nextConfig.ocrCorrectionProvider || (nextConfig.yunwuConfigured ? 'yunwu-openai' : 'openai-compatible'))
        setStatus(nextConfig.ocrCorrectionConfigured ? '配置已加载，可以开始测试。' : 'OCR 校正模型尚未配置，请先检查 .env。')
      })
      .catch((error) => setStatus(error instanceof Error ? error.message : String(error)))
  }, [])

  async function handleImagePick(file: File | null) {
    if (!file) return
    const dataUrl = await readFileAsDataUrl(file)
    setImageName(file.name)
    setImageDataUrl(dataUrl)
    setStatus(`已载入页图：${file.name}`)
  }

  async function submitCorrection(nextDryRun: boolean) {
    if (!markdown.trim() || loading) return
    setLoading(true)
    setResult(null)
    setStatus(nextDryRun ? '正在预演高风险块筛选...' : '正在调用 OCR 校正模型...')
    try {
      const response = await runOcrCorrection({
        provider,
        markdown,
        dryRun: nextDryRun,
        maxCandidates,
        pageImages: imageDataUrl
          ? [
              {
                pageNumber: pageNumber.trim() ? Number(pageNumber) : undefined,
                image: imageDataUrl,
              },
            ]
          : undefined,
      })
      setResult(response)
      if (!response.ok) {
        setStatus(response.error || '请求失败')
      } else if (nextDryRun) {
        setStatus(`预演完成，共筛出 ${response.candidates?.length ?? 0} 个候选块。`)
      } else {
        setStatus(
          `校正完成：${response.corrections?.length ?? 0} 个块已处理，${response.errors?.length ?? 0} 个块失败。`,
        )
      }
    } catch (error) {
      setStatus(error instanceof Error ? error.message : String(error))
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="ocr-page">
      <section className="ocr-page-shell">
        <header className="standalone-viz-head">
          <div>
            <p className="eyebrow">OCR Workbench</p>
            <h1>MinerU 高风险块校正测试台</h1>
          </div>
          <div className="top-actions">
            <a className="top-link" href={appHref.toString()}>
              返回工作台
            </a>
            <a className="top-link" href={galleryHref}>
              展示厅
            </a>
          </div>
        </header>

        <section className="ocr-grid">
          <div className="ocr-card">
            <div className="section-head">
              <span>请求设置</span>
              <b>{dryRun ? '预演' : '实跑'}</b>
            </div>
            <div className="ocr-config-row">
              <label>
                <span>Provider</span>
                <select className="field" value={provider} onChange={(event) => setProvider(event.target.value)}>
                  <option value="yunwu-openai">yunwu-openai / GPT 5.5</option>
                  <option value="openai-compatible">openai-compatible</option>
                  <option value="gemini">gemini</option>
                </select>
              </label>
              <label>
                <span>Max Candidates</span>
                <input
                  className="field"
                  type="number"
                  min="1"
                  max="50"
                  value={maxCandidates}
                  onChange={(event) => setMaxCandidates(Number(event.target.value || 1))}
                />
              </label>
            </div>
            <label className="rag-toggle">
              <input type="checkbox" checked={dryRun} onChange={(event) => setDryRun(event.target.checked)} />
              <span>仅预演筛块，不调用模型</span>
            </label>
            <p className="muted">
              当前配置：{config?.ocrCorrectionConfigured ? 'OCR 校正已配置' : 'OCR 校正未配置'} /{' '}
              {config?.yunwuConfigured ? '云雾已配置' : '云雾未配置'}
            </p>
          </div>

          <div className="ocr-card">
            <div className="section-head">
              <span>页图输入</span>
              <b>{imageName ? '1' : '0'}</b>
            </div>
            <label className="file-pick ocr-file-pick">
              <input
                type="file"
                accept="image/png,image/jpeg,image/webp"
                onChange={(event) => void handleImagePick(event.target.files?.[0] ?? null)}
              />
              <span>{imageName || '选择页图用于多模态校正'}</span>
            </label>
            <label>
              <span className="ocr-label">Page Number</span>
              <input className="field" value={pageNumber} onChange={(event) => setPageNumber(event.target.value)} />
            </label>
            {imageDataUrl ? <img alt="OCR page preview" className="ocr-image-preview" src={imageDataUrl} /> : null}
          </div>
        </section>

        <section className="ocr-grid single">
          <div className="ocr-card">
            <div className="section-head">
              <span>Markdown 输入</span>
              <b>{markdown.length}</b>
            </div>
            <textarea
              className="ocr-textarea"
              value={markdown}
              onChange={(event) => setMarkdown(event.target.value)}
              placeholder="粘贴 MinerU 输出的 Markdown"
            />
            <div className="ocr-action-row">
              <button type="button" onClick={() => setMarkdown(ocrWorkbenchSample)} disabled={loading}>
                载入示例
              </button>
              <button type="button" onClick={() => void submitCorrection(true)} disabled={loading || !markdown.trim()}>
                Dry Run
              </button>
              <button type="button" onClick={() => void submitCorrection(false)} disabled={loading || !markdown.trim()}>
                {loading ? '处理中...' : '运行校正'}
              </button>
            </div>
            <p className="status-line">{status}</p>
          </div>
        </section>

        <section className="ocr-results">
          <div className="ocr-card">
            <div className="section-head">
              <span>候选块</span>
              <b>{result?.candidates?.length ?? 0}</b>
            </div>
            {result?.candidates?.length ? (
              <div className="ocr-candidate-list">
                {result.candidates.map((candidate) => (
                  <article className="ocr-candidate" key={`${candidate.block_index}-${candidate.start}`}>
                    <div className="ocr-candidate-meta">
                      <strong>块 {candidate.block_index}</strong>
                      <span>score {candidate.score}</span>
                      <span>page {candidate.page_number ?? '-'}</span>
                    </div>
                    <p>{candidate.reasons.join(' / ')}</p>
                    <pre>{truncateText(candidate.text, 360)}</pre>
                  </article>
                ))}
              </div>
            ) : (
              <p className="muted">还没有候选块结果。</p>
            )}
          </div>

          <div className="ocr-card">
            <div className="section-head">
              <span>校正结果</span>
              <b>{result?.corrections?.length ?? 0}</b>
            </div>
            {result?.corrections?.length ? (
              <div className="ocr-candidate-list">
                {result.corrections.map((item) => (
                  <article className="ocr-candidate" key={`${item.block_index}-${item.corrected.length}`}>
                    <div className="ocr-candidate-meta">
                      <strong>块 {item.block_index}</strong>
                      <span>{item.changed ? '已修改' : '未修改'}</span>
                    </div>
                    <p>{item.reasons.join(' / ')}</p>
                    <pre>{truncateText(item.corrected, 360)}</pre>
                  </article>
                ))}
              </div>
            ) : (
              <p className="muted">还没有校正结果。</p>
            )}
          </div>
        </section>

        <section className="ocr-grid single">
          <div className="ocr-card">
            <div className="section-head">
              <span>合并后的 Markdown</span>
              <b>{result?.correctedMarkdown?.length ?? 0}</b>
            </div>
            <textarea className="ocr-textarea result" readOnly value={result?.correctedMarkdown || ''} />
            {result?.errors?.length ? (
              <details className="ocr-raw-panel">
                <summary>查看错误</summary>
                <pre>{formatJson(result.errors)}</pre>
              </details>
            ) : null}
            {result ? (
              <details className="ocr-raw-panel">
                <summary>查看完整响应 JSON</summary>
                <pre>{formatJson(result)}</pre>
              </details>
            ) : null}
          </div>
        </section>
      </section>
    </main>
  )
}

function WorkspaceApp({ isGallery }: { isGallery: boolean }) {
  const galleryHref = buildGalleryPageUrl()
  const ocrHref = buildOcrWorkbenchUrl()
  const [health, setHealth] = useState<string>('Checking')
  const [strategies, setStrategies] = useState<RagStrategy[]>([])
  const [kbs, setKbs] = useState<KnowledgeBase[]>([])
  const [selectedStrategy, setSelectedStrategy] = useState<string>('naive')
  const [selectedKb, setSelectedKb] = useState<string | null>(null)
  const [useRag, setUseRag] = useState(false)
  const [kbInput, setKbInput] = useState('')
  const [messages, setMessages] = useState<ChatMessage[]>([])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [activeStage, setActiveStage] = useState(0)
  const [loadingStages, setLoadingStages] = useState<OrchestrationStep[]>(buildRuntimeStages(false, ''))
  const [evidenceOpen, setEvidenceOpen] = useState(false)
  const [status, setStatus] = useState('')
  const [galleryItems, setGalleryItems] = useState<VisualizationInstruction[]>([])
  const [galleryStatus, setGalleryStatus] = useState('正在加载展示厅...')
  const composerFileInputRef = useRef<HTMLInputElement | null>(null)

  const currentStrategy = strategies.find((item) => item.id === selectedStrategy)
  const latestAssistant = [...messages].reverse().find((item) => item.role === 'assistant')
  const latestContexts = latestAssistant?.role === 'assistant' ? latestAssistant.contexts ?? [] : []

  async function refresh() {
    const [healthResult, strategyResult, kbResult] = await Promise.all([
      fetchHealth(),
      fetchStrategies(),
      fetchKnowledgeBases(),
    ])
    setHealth(healthResult.ok ? 'Online' : 'Offline')
    setStrategies(strategyResult.items)
    setSelectedStrategy((current) => current || strategyResult.items[0]?.id || 'naive')
    setKbs(kbResult.items)
  }

  useEffect(() => {
    refresh().catch((error) => setStatus(error instanceof Error ? error.message : String(error)))
  }, [])

  useEffect(() => {
    if (!isGallery) return
    fetchVisualizations()
      .then((result) => {
        setGalleryItems(result.items)
        setGalleryStatus(result.items.length ? '' : '暂无可视化条目。')
      })
      .catch((error) => setGalleryStatus(error instanceof Error ? error.message : String(error)))
  }, [isGallery])

  useEffect(() => {
    if (!isLoading) {
      setActiveStage(0)
      return
    }

    const interval = window.setInterval(() => {
      setActiveStage((stage) => Math.min(stage + 1, loadingStages.length - 1))
    }, 750)
    return () => window.clearInterval(interval)
  }, [isLoading, loadingStages.length])

  useEffect(() => {
    if (useRag && !selectedKb && kbs[0]?.kb_id) {
      setSelectedKb(kbs[0].kb_id)
    }
  }, [useRag, selectedKb, kbs])

  useEffect(() => {
    setEvidenceOpen(false)
  }, [latestAssistant?.id])

  async function handleUpload(file: File | null) {
    if (!file) return
    const nextKbId = kbInput.trim() || suggestKbId(file.name)
    setKbInput(nextKbId)
    setStatus('正在上传并建立本地知识库...')
    const result = await uploadDocument(file, nextKbId)
    if (!result.ok) {
      setStatus(result.error || '上传失败')
      return
    }
    setStatus(`已上传到 ${result.kbId}，共摄入 ${result.chunks ?? '-'} 个文档块。`)
    setSelectedKb(result.kbId ?? nextKbId)
    await refresh()
  }

  async function sendQuestion(text = input) {
    const question = text.trim()
    if (!question || isLoading) return

    const history = messages
      .filter((message) => message.role === 'user' || message.role === 'assistant')
      .map((message) => ({ role: message.role, content: message.content }))

    setInput('')
    setIsLoading(true)
    setActiveStage(0)
    setLoadingStages(buildRuntimeStages(useRag, question))
    setMessages((prev) => [...prev, { id: createId('user'), role: 'user', content: question }])

    try {
      const response = await askQuestion({
        question,
        history,
        ragVariant: selectedStrategy,
        kbId: useRag ? selectedKb : null,
        useRag,
      })
      setMessages((prev) => [
        ...prev,
        {
          id: createId('assistant'),
          role: 'assistant',
          content: response.answer || '没有生成回答。',
          strategy: response.strategy,
          citations: response.citations,
          contexts: response.contexts,
          recommendedVisualizations: response.recommendedVisualizations,
          orchestration: response.orchestration,
          autoRagUsed: response.autoRagUsed,
          computedEphemeris: response.computedEphemeris,
        },
      ])
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          id: createId('assistant'),
          role: 'assistant',
          content: error instanceof Error ? error.message : String(error),
        },
      ])
    } finally {
      setIsLoading(false)
    }
  }

  async function askFloatingAssistant(question: string, floatingHistory: FloatingAssistantMessage[]) {
    const response = await askQuestion({
      question,
      history: floatingHistory
        .filter((message) => message.role === 'user' || message.role === 'assistant')
        .map((message) => ({ role: message.role, content: message.content })),
      ragVariant: selectedStrategy,
      kbId: useRag ? selectedKb : null,
      useRag,
    })
    return response.answer || '没有生成回答。'
  }

  if (isGallery) {
    return (
      <main className="gallery-page">
        <section className="gallery-copy">
          <p className="eyebrow">A2UI Gallery</p>
          <h1>天文学展示厅</h1>
          <p>集中预览已注册的天文学交互组件、嵌入页面和外部计算器。</p>
        </section>
        {galleryStatus ? <p className="muted">{galleryStatus}</p> : null}
        {galleryItems.length ? <A2UISurface surface={buildSurfaceFromVisualizations(galleryItems)} /> : null}
      </main>
    )
  }

  return (
    <div className="app-shell">
      <div className="background-orbit" />
      <header className="top-nav">
        <div>
          <p className="eyebrow">Universe Model Agent</p>
          <strong>宇宙模型智能体</strong>
        </div>
        <div className="top-actions">
          <span>{health}</span>
          <span>{useRag ? selectedStrategy : 'local-first'}</span>
          <a className="top-link" href={galleryHref}>
            天文学展示厅
          </a>
          <a className="top-link" href={ocrHref}>
            OCR 测试台
          </a>
        </div>
      </header>

      <div className="workspace">
        <aside className="left-rail">
          <section>
            <div className="section-head">
              <span>RAG 知识库</span>
              <b>{kbs.length}</b>
            </div>
            <label className="rag-toggle">
              <input type="checkbox" checked={useRag} onChange={(event) => setUseRag(event.target.checked)} />
              <span>使用 RAG 知识库</span>
            </label>
            <label className="file-pick">
              <input type="file" accept=".txt,.md,.docx,.pdf" onChange={(event) => void handleUpload(event.target.files?.[0] ?? null)} />
              <span>选择本地文档</span>
            </label>
            <input
              className="field"
              value={kbInput}
              onChange={(event) => setKbInput(event.target.value)}
              placeholder="知识库 ID"
            />
            <select className="field" value={selectedKb ?? ''} onChange={(event) => setSelectedKb(event.target.value || null)} disabled={!useRag}>
              <option value="">选择知识库</option>
              {kbs.map((kb) => (
                <option key={kb.kb_id} value={kb.kb_id}>
                  {kb.kb_id} ({kb.doc_count ?? 0} 文档 / {kb.chunk_count ?? 0} 块)
                </option>
              ))}
            </select>
            {status && <p className="status-line">{status}</p>}
          </section>

          <section>
            <div className="section-head">
              <span>RAG 方案</span>
              <b>{strategies.length}</b>
            </div>
            <select className="field" value={selectedStrategy} onChange={(event) => setSelectedStrategy(event.target.value)}>
              {strategies.map((strategy) => (
                <option key={strategy.id} value={strategy.id}>
                  {strategy.label}
                </option>
              ))}
            </select>
            <p className="muted">{useRag ? currentStrategy?.summary : '默认优先检索本地项目资料；没有可靠命中时再走普通 LLM。'}</p>
          </section>
        </aside>

        <main className="conversation">
          <div className="message-list">
            {messages.length === 0 ? (
              <section className="welcome-panel">
                <p className="eyebrow">Astronomy Chat</p>
                <h1>用真实 A2UI 组件解释宇宙模型</h1>
                <a className="gallery-entry-card" href={galleryHref}>
                  <div>
                    <p className="eyebrow">Gallery</p>
                    <strong>进入天文学展示厅</strong>
                    <span>查看 3D 天球、DE440 计算器、食相演示与更多交互页面。</span>
                  </div>
                  <b>进入</b>
                </a>
                <a className="gallery-entry-card" href={ocrHref}>
                  <div>
                    <p className="eyebrow">OCR</p>
                    <strong>进入 OCR 校正测试台</strong>
                    <span>直接测试 MinerU 高风险块筛选、云雾 GPT 5.5 校正和结果合并。</span>
                  </div>
                  <b>进入</b>
                </a>
                <div className="starter-row">
                  {starterQuestions.map((question) => (
                    <button key={question} onClick={() => void sendQuestion(question)}>
                      {question}
                    </button>
                  ))}
                </div>
              </section>
            ) : (
              messages.map((message) => (
                <article key={message.id} className={`message ${message.role}`}>
                  <p className="message-role">{message.role === 'user' ? 'USER' : 'ASSISTANT'}</p>
                  <div className="message-bubble">{message.content}</div>
                  {message.role === 'assistant' ? (
                    <MessageVisualizations items={message.recommendedVisualizations ?? []} />
                  ) : null}
                </article>
              ))
            )}
            {isLoading && (
              <article className="message assistant">
                <p className="message-role">ASSISTANT</p>
                <PipelineStatus steps={loadingStages} activeIndex={activeStage} loading />
              </article>
            )}
          </div>

          <div className="composer-shell">
            {status ? <p className="composer-status">{status}</p> : null}
            <div className="bottom-input">
              <input
                ref={composerFileInputRef}
                className="bottom-input-file"
                type="file"
                accept=".txt,.md,.docx,.pdf"
                onChange={(event) => {
                  const file = event.target.files?.[0] ?? null
                  void handleUpload(file)
                  event.currentTarget.value = ''
                }}
              />
              <button
                className="attach-button"
                type="button"
                onClick={() => composerFileInputRef.current?.click()}
                disabled={isLoading}
                title="上传附件到知识库"
              >
                +
              </button>
              <input
                value={input}
                onChange={(event) => setInput(event.target.value)}
                onKeyDown={(event) => {
                  if (event.key === 'Enter') void sendQuestion()
                }}
                placeholder="输入你的问题，例如：绘制 2050 年火星 VSOP 和 DE440 对照图"
              />
              <button onClick={() => void sendQuestion()} disabled={!input.trim() || isLoading}>
                {isLoading ? '...' : '↑'}
              </button>
            </div>
          </div>
        </main>

        <aside className="right-rail">
          <section className="evidence-panel">
            <div className="right-section-title">
              <p className="eyebrow">Evidence</p>
              <button type="button" onClick={() => setEvidenceOpen((open) => !open)} disabled={!latestContexts.length}>
                {evidenceOpen ? '隐藏' : latestContexts.length ? `显示 ${latestContexts.length}` : '显示'}
              </button>
            </div>
            {!evidenceOpen ? (
              <p className="muted">{latestContexts.length ? '已有引用，点击显示来源片段。' : '检索证据默认隐藏；需要核对来源时点击显示。'}</p>
            ) : latestContexts.length ? (
              latestContexts.slice(0, 4).map((context, index) => (
                <div className="evidence" key={`${context.source}-${index}`}>
                  <strong>{context.source || `上下文 ${index + 1}`}</strong>
                  <span>score {typeof context.score === 'number' ? context.score.toFixed(3) : '-'}</span>
                  <MarkdownExcerpt content={context.content} />
                </div>
              ))
            ) : (
              <p className="muted">暂无检索证据。</p>
            )}
          </section>
        </aside>
      </div>
      <FloatingAssistant
        title="宇宙模型助手"
        subtitle={health === 'Online' ? '在线，可以随时提问' : '服务连接中'}
        placeholder="问我一个天文或模型问题"
        disabled={health !== 'Online'}
        onAsk={askFloatingAssistant}
      />
    </div>
  )
}

export function App() {
  const searchParams = new URLSearchParams(window.location.search)
  const visualizationId = searchParams.get('viz')
  if (visualizationId) {
    return <StandaloneVisualizationPage item={loadVisualizationFromWindow(visualizationId)} />
  }
  if (searchParams.get('ocr') === '1') {
    return <OcrWorkbenchPage />
  }
  return <WorkspaceApp isGallery={searchParams.get('gallery') === '1'} />
}

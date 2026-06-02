import { useEffect, useMemo, useState } from 'react'
import { A2UISurface, applyA2UILine, createEmptySurface } from './a2ui-engine/A2UIRuntime'
import { buildA2UILines } from './a2ui-engine/buildA2UILines'
import {
  askQuestion,
  fetchHealth,
  fetchKnowledgeBases,
  fetchStrategies,
  uploadDocument,
  type KnowledgeBase,
  type RagStrategy,
  type VisualizationInstruction,
} from './services/api'
import { createId, type ChatMessage } from './types'

const starterQuestions = [
  '请可视化展示黄道和白道的关系',
  '为什么会发生月食？',
  '行星为什么会逆行？',
]

function suggestKbId(filename: string): string {
  const stem = filename.replace(/\.[^.]+$/, '')
  const parts = stem.split(/[\s._\-()（）【】\[\]、，,]+/).filter(Boolean)
  return parts.slice(0, 2).join('-') || 'default'
}

function buildSurfaceFromVisualizations(items: VisualizationInstruction[]) {
  let surface = createEmptySurface()
  const lines = items.flatMap((item) => buildA2UILines(item))
  for (const line of lines) {
    surface = applyA2UILine(surface, line)
  }
  return surface
}

export function App() {
  const isGallery = new URLSearchParams(window.location.search).get('gallery') === '1'
  const [health, setHealth] = useState<string>('Checking')
  const [strategies, setStrategies] = useState<RagStrategy[]>([])
  const [kbs, setKbs] = useState<KnowledgeBase[]>([])
  const [selectedStrategy, setSelectedStrategy] = useState<string>('naive')
  const [selectedKb, setSelectedKb] = useState<string | null>(null)
  const [kbInput, setKbInput] = useState('')
  const [messages, setMessages] = useState<ChatMessage[]>([])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [status, setStatus] = useState('')

  const currentStrategy = strategies.find((item) => item.id === selectedStrategy)
  const latestAssistant = [...messages].reverse().find((item) => item.role === 'assistant')
  const latestVisualizations = latestAssistant?.role === 'assistant' ? latestAssistant.recommendedVisualizations ?? [] : []
  const latestSurface = useMemo(() => buildSurfaceFromVisualizations(latestVisualizations), [latestVisualizations])

  async function refresh() {
    const [healthResult, strategyResult, kbResult] = await Promise.all([
      fetchHealth(),
      fetchStrategies(),
      fetchKnowledgeBases(),
    ])
    setHealth(healthResult.ok ? 'Online' : 'Offline')
    setStrategies(strategyResult.items)
    setSelectedStrategy(strategyResult.items[0]?.id ?? 'naive')
    setKbs(kbResult.items)
    setSelectedKb(kbResult.items[0]?.kb_id ?? null)
  }

  useEffect(() => {
    refresh().catch((error) => setStatus(error instanceof Error ? error.message : String(error)))
  }, [])

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
    setMessages((prev) => [...prev, { id: createId('user'), role: 'user', content: question }])

    try {
      const response = await askQuestion({
        question,
        history,
        ragVariant: selectedStrategy,
        kbId: selectedKb,
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

  if (isGallery) {
    return (
      <main className="gallery-page">
        <section className="gallery-copy">
          <p className="eyebrow">A2UI Gallery</p>
          <h1>天文 A2UI 组件预览</h1>
          <p>Phase 1 先注册本地 `astronomy-core.ecliptic-lunar-path`，用于替代文字假图。</p>
        </section>
        <A2UISurface
          surface={buildSurfaceFromVisualizations([
            {
              id: 'ecliptic-lunar-path',
              title: '黄道与白道关系',
              description: '',
              a2uiInstruction: {
                componentId: 'astronomy-core.ecliptic-lunar-path',
                intentType: 'spatial_geometry_explanation',
                initialProps: {
                  inclinationDeg: 5.145,
                  showNodes: true,
                  showLabels: true,
                  moonPositionDeg: 35,
                },
              },
            },
          ])}
        />
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
        <div className="top-status">
          <span>{health}</span>
          <span>{selectedStrategy}</span>
        </div>
      </header>

      <div className="workspace">
        <aside className="left-rail">
          <section>
            <div className="section-head">
              <span>RAG 知识库</span>
              <b>{kbs.length}</b>
            </div>
            <label className="file-pick">
              <input type="file" accept=".txt,.md,.docx" onChange={(event) => void handleUpload(event.target.files?.[0] ?? null)} />
              <span>选择本地文档</span>
            </label>
            <input
              className="field"
              value={kbInput}
              onChange={(event) => setKbInput(event.target.value)}
              placeholder="知识库 ID"
            />
            <select className="field" value={selectedKb ?? ''} onChange={(event) => setSelectedKb(event.target.value || null)}>
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
            <p className="muted">{currentStrategy?.summary}</p>
          </section>
        </aside>

        <main className="conversation">
          <div className="message-list">
            {messages.length === 0 ? (
              <section className="welcome-panel">
                <p className="eyebrow">Astronomy Chat</p>
                <h1>用真实 A2UI 组件解释宇宙模型</h1>
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
                </article>
              ))
            )}
          </div>

          <div className="bottom-input">
            <input
              value={input}
              onChange={(event) => setInput(event.target.value)}
              onKeyDown={(event) => {
                if (event.key === 'Enter') void sendQuestion()
              }}
              placeholder="输入你的问题，例如：请可视化展示黄道和白道的关系"
            />
            <button onClick={() => void sendQuestion()} disabled={!input.trim() || isLoading}>
              {isLoading ? '...' : '↑'}
            </button>
          </div>
        </main>

        <aside className="right-rail">
          <section>
            <p className="eyebrow">A2UI Surface</p>
            {latestVisualizations.length ? (
              <A2UISurface surface={latestSurface} />
            ) : (
              <p className="muted">提问命中可视化能力后，这里会渲染真实 A2UI 组件。</p>
            )}
          </section>

          <section>
            <p className="eyebrow">Evidence</p>
            {latestAssistant?.role === 'assistant' && latestAssistant.contexts?.length ? (
              latestAssistant.contexts.slice(0, 3).map((context, index) => (
                <div className="evidence" key={`${context.source}-${index}`}>
                  <strong>{context.source || `上下文 ${index + 1}`}</strong>
                  <span>score {typeof context.score === 'number' ? context.score.toFixed(3) : '-'}</span>
                  <p>{context.content}</p>
                </div>
              ))
            ) : (
              <p className="muted">暂无检索证据。</p>
            )}
          </section>
        </aside>
      </div>
    </div>
  )
}

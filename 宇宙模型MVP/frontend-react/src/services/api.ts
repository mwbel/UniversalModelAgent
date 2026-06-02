export type RagStrategy = {
  id: string
  label: string
  summary: string
  workflow: string
}

export type KnowledgeBase = {
  kb_id: string
  doc_count?: number
  chunk_count?: number
}

export type ChatResponse = {
  answer: string
  service?: string
  strategy?: string
  citations?: Array<{ title: string; snippet: string; url?: string }>
  contexts?: Array<{ content: string; score?: number; source?: string; metadata?: Record<string, unknown> }>
  recommendedVisualizations?: VisualizationInstruction[]
}

export type VisualizationInstruction = {
  id: string
  title: string
  description: string
  componentId?: string
  intentType?: string
  a2uiInstruction?: {
    componentId: string
    intentType: string
    initialProps: Record<string, unknown>
  }
}

const API_BASE = ''

async function readJson<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, init)
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${response.statusText}`)
  }
  return response.json() as Promise<T>
}

export async function fetchHealth() {
  return readJson<{ ok: boolean; appName: string; ragBaseUrl: string }>('/api/health')
}

export async function fetchStrategies() {
  return readJson<{ ok: boolean; items: RagStrategy[] }>('/api/rag/strategies')
}

export async function fetchKnowledgeBases() {
  return readJson<{ ok: boolean; items: KnowledgeBase[] }>('/api/rag/kbs')
}

export async function uploadDocument(file: File, kbId: string) {
  const formData = new FormData()
  formData.append('file', file)
  formData.append('kb_id', kbId)
  return readJson<{ ok: boolean; kbId?: string; chunks?: number; error?: string }>('/api/rag/upload', {
    method: 'POST',
    body: formData,
  })
}

export async function askQuestion(payload: {
  question: string
  history: Array<{ role: string; content: string }>
  ragVariant: string | null
  kbId: string | null
}) {
  return readJson<ChatResponse>('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })
}

import type { ChatResponse } from './services/api'

export type ChatMessage =
  | { id: string; role: 'user'; content: string }
  | ({
      id: string
      role: 'assistant'
      content: string
    } & Pick<ChatResponse, 'strategy' | 'citations' | 'contexts' | 'recommendedVisualizations' | 'orchestration'>)

export function createId(prefix: string): string {
  return `${prefix}-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`
}

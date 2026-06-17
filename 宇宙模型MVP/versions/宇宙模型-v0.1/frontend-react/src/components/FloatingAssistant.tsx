import { useEffect, useRef, useState } from 'react'

export type FloatingAssistantMessage = {
  id: string
  role: 'assistant' | 'user'
  content: string
}

export type FloatingAssistantProps = {
  title?: string
  subtitle?: string
  placeholder?: string
  initialMessage?: string
  disabled?: boolean
  onAsk: (question: string, history: FloatingAssistantMessage[]) => Promise<string>
}

function createFloatingId(prefix: string) {
  return `${prefix}-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`
}

export function FloatingAssistant({
  title = 'AI 助手',
  subtitle = '随时问我',
  placeholder = '输入问题...',
  initialMessage = '你好，我在这里。你可以直接问一个问题，或让我解释当前页面里的内容。',
  disabled = false,
  onAsk,
}: FloatingAssistantProps) {
  const [open, setOpen] = useState(false)
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [messages, setMessages] = useState<FloatingAssistantMessage[]>([
    { id: createFloatingId('assistant'), role: 'assistant', content: initialMessage },
  ])
  const inputRef = useRef<HTMLInputElement | null>(null)
  const listRef = useRef<HTMLDivElement | null>(null)

  useEffect(() => {
    if (open) {
      window.setTimeout(() => inputRef.current?.focus(), 80)
    }
  }, [open])

  useEffect(() => {
    listRef.current?.scrollTo({ top: listRef.current.scrollHeight, behavior: 'smooth' })
  }, [messages, loading])

  async function send() {
    const question = input.trim()
    if (!question || loading || disabled) return

    const userMessage: FloatingAssistantMessage = {
      id: createFloatingId('user'),
      role: 'user',
      content: question,
    }
    const nextMessages = [...messages, userMessage]
    setMessages(nextMessages)
    setInput('')
    setLoading(true)

    try {
      const answer = await onAsk(question, nextMessages)
      setMessages((current) => [
        ...current,
        {
          id: createFloatingId('assistant'),
          role: 'assistant',
          content: answer || '我没有拿到可展示的回答。',
        },
      ])
    } catch (error) {
      setMessages((current) => [
        ...current,
        {
          id: createFloatingId('assistant'),
          role: 'assistant',
          content: error instanceof Error ? error.message : String(error),
        },
      ])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className={`floating-assistant ${open ? 'open' : ''}`}>
      {open ? (
        <section className="floating-assistant-panel" aria-label={title}>
          <header className="floating-assistant-head">
            <button
              className="floating-assistant-avatar"
              type="button"
              onClick={() => setOpen(false)}
              title="收起助手"
              aria-label="收起助手"
            >
              <span />
            </button>
            <div>
              <strong>{title}</strong>
              <small>{loading ? '正在思考' : subtitle}</small>
            </div>
            <button
              className="floating-assistant-close"
              type="button"
              onClick={() => setOpen(false)}
              title="关闭对话框"
              aria-label="关闭对话框"
            >
              ×
            </button>
          </header>

          <div className="floating-assistant-list" ref={listRef}>
            {messages.map((message) => (
              <div className={`floating-assistant-message ${message.role}`} key={message.id}>
                {message.content}
              </div>
            ))}
            {loading ? <div className="floating-assistant-message assistant">正在生成回答...</div> : null}
          </div>

          <div className="floating-assistant-input">
            <input
              ref={inputRef}
              value={input}
              onChange={(event) => setInput(event.target.value)}
              onKeyDown={(event) => {
                if (event.key === 'Enter') void send()
              }}
              placeholder={placeholder}
              disabled={disabled}
            />
            <button type="button" onClick={() => void send()} disabled={!input.trim() || loading || disabled}>
              ↑
            </button>
          </div>
        </section>
      ) : (
        <button
          className="floating-assistant-button"
          type="button"
          onClick={() => setOpen(true)}
          title={title}
          aria-label={title}
        >
          <span className="floating-assistant-orb" />
        </button>
      )}
    </div>
  )
}

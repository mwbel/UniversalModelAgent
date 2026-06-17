export type SplitResult =
  | { type: 'text'; content: string }
  | { type: 'a2ui'; line: string }
  | { type: 'done' }
  | { type: 'unknown' }

const A2UI_MESSAGE_KEYS = new Set(['surfaceUpdate', 'dataModelUpdate', 'beginRendering', 'deleteSurface'])

export function isA2UILine(text: string): boolean {
  const stripped = text.trim()
  if (!stripped.startsWith('{')) return false

  try {
    const parsed = JSON.parse(stripped)
    if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) return false
    return Object.keys(parsed).some((key) => A2UI_MESSAGE_KEYS.has(key))
  } catch {
    return false
  }
}

export function splitSSELine(raw: string): SplitResult {
  if (!raw.startsWith('data: ')) return { type: 'unknown' }

  const jsonText = raw.slice('data: '.length).trim()
  if (!jsonText) return { type: 'unknown' }

  try {
    const parsed = JSON.parse(jsonText) as { type?: unknown; content?: unknown; line?: unknown }
    if (parsed.type === 'text' && typeof parsed.content === 'string') {
      return { type: 'text', content: parsed.content }
    }
    if (parsed.type === 'a2ui' && typeof parsed.line === 'string') {
      return { type: 'a2ui', line: parsed.line }
    }
    if (parsed.type === 'done') {
      return { type: 'done' }
    }
  } catch {
    return { type: 'unknown' }
  }

  return { type: 'unknown' }
}

export function remapSurfaceId(line: string, nextSurfaceId: string): string {
  return line.replace(/"surfaceId"\s*:\s*"main"/g, `"surfaceId":"${nextSurfaceId}"`)
}

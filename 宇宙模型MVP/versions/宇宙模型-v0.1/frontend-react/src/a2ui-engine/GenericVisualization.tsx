import { useState } from 'react'

type GenericVisualizationProps = {
  componentId: string
  node: Record<string, unknown>
}

function isNumber(value: unknown): value is number {
  return typeof value === 'number' && Number.isFinite(value)
}

export function GenericVisualization({ componentId, node }: GenericVisualizationProps) {
  const title = typeof node.title === 'string' ? node.title : componentId
  const description = typeof node.description === 'string' ? node.description : '该能力还没有专用组件，先以参数化面板展示。'
  const embedUrl = typeof node.embedUrl === 'string' ? node.embedUrl : ''
  const galleryUrl = typeof node.galleryUrl === 'string' ? node.galleryUrl : ''
  const numericEntries = Object.entries(node).filter(([, value]) => isNumber(value))
  const booleanEntries = Object.entries(node).filter(([, value]) => typeof value === 'boolean')
  const [values, setValues] = useState<Record<string, number>>(
    () => Object.fromEntries(numericEntries.map(([key, value]) => [key, Number(value)])),
  )
  const [toggles, setToggles] = useState<Record<string, boolean>>(
    () => Object.fromEntries(booleanEntries.map(([key, value]) => [key, Boolean(value)])),
  )

  if (embedUrl) {
    return (
      <div className="generic-viz legacy-viz">
        <header>
          <div>
            <p className="astro-kicker">A2UI embedded page</p>
            <h3>{title}</h3>
          </div>
          {galleryUrl ? (
            <a href={galleryUrl} rel="noreferrer" target="_blank">
              新窗口打开
            </a>
          ) : (
            <code>{componentId}</code>
          )}
        </header>
        {description ? <p>{description}</p> : null}
        <iframe src={embedUrl} title={title} loading="lazy" />
      </div>
    )
  }

  return (
    <div className="generic-viz">
      <header>
        <div>
          <p className="astro-kicker">A2UI dynamic component</p>
          <h3>{title}</h3>
        </div>
        <code>{componentId}</code>
      </header>
      <p>{description}</p>

      {(numericEntries.length > 0 || booleanEntries.length > 0) && (
        <div className="generic-controls">
          {numericEntries.map(([key, fallback]) => {
            const value = values[key] ?? Number(fallback)
            return (
              <label key={key}>
                <span>{key}</span>
                <input
                  type="range"
                  min="0"
                  max={Math.max(360, Math.ceil(Math.abs(Number(fallback)) * 2))}
                  value={value}
                  onChange={(event) => setValues((prev) => ({ ...prev, [key]: Number(event.target.value) }))}
                />
                <strong>{value.toFixed(value % 1 === 0 ? 0 : 2)}</strong>
              </label>
            )
          })}

          {booleanEntries.map(([key]) => (
            <label key={key} className="generic-toggle">
              <span>{key}</span>
              <input
                type="checkbox"
                checked={toggles[key] ?? false}
                onChange={(event) => setToggles((prev) => ({ ...prev, [key]: event.target.checked }))}
              />
            </label>
          ))}
        </div>
      )}
    </div>
  )
}

import { useEffect, useState } from 'react'

type ComponentProps = {
  node: Record<string, unknown>
}

type EphemerisItem = {
  body: string
  name: string
  de440?: { positionAu: number[]; distanceAu: number; orbitPathAu?: number[][] }
  vsop?: { positionAu: number[]; distanceAu: number; orbitPathAu?: number[][] }
  delta?: { distanceKm: number; distanceAu: number; speedKmS: number }
  recommendation?: { model: 'DE440' | 'VSOP_OK'; reason: string; meetsTolerance: boolean | null }
  error?: string
}

type EphemerisResponse = {
  ok: boolean
  date?: string
  referenceFrame?: string
  tolerance?: { value: number | null; unit: string }
  items: EphemerisItem[]
  error?: string
}

const bodyOptions = [
  ['mercury', '水星'],
  ['venus', '金星'],
  ['earth', '地球'],
  ['mars', '火星'],
  ['jupiter', '木星'],
  ['saturn', '土星'],
  ['uranus', '天王星'],
  ['neptune', '海王星'],
  ['moon', '月球'],
]

const colors: Record<string, string> = {
  mercury: '#cbd5e1',
  venus: '#facc15',
  earth: '#38bdf8',
  mars: '#fb6045',
  jupiter: '#f0b35a',
  saturn: '#d6c17b',
  uranus: '#67e8f9',
  neptune: '#60a5fa',
  moon: '#c4b5fd',
}

function stringProp(value: unknown, fallback: string) {
  return typeof value === 'string' && value.trim() ? value : fallback
}

function arrayProp(value: unknown, fallback: string[]) {
  if (!Array.isArray(value)) return fallback
  const items = value.filter((item): item is string => typeof item === 'string')
  return items.length ? items : fallback
}

function todayDateInput() {
  return new Date().toISOString().slice(0, 10)
}

function project(positionAu: number[], scale: number) {
  return {
    x: 210 + (positionAu[0] / scale) * 168,
    y: 170 + (positionAu[1] / scale) * 168,
  }
}

function toPolyline(points: number[][], scale: number) {
  return points
    .map((point) => {
      const projected = project(point, scale)
      return `${projected.x},${projected.y}`
    })
    .join(' ')
}

function formatKm(value?: number) {
  if (typeof value !== 'number') return '-'
  if (value >= 1_000_000) return `${(value / 1_000_000).toFixed(2)}M km`
  return `${Math.round(value).toLocaleString()} km`
}

export function EphemerisComparison({ node }: ComponentProps) {
  const initialBodies = arrayProp(node.bodies, ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn'])
  const initialDate = stringProp(node.date, todayDateInput())
  const initialTolerance = stringProp(node.tolerance, '')
  const [date, setDate] = useState(initialDate === 'today' ? todayDateInput() : initialDate)
  const [selectedBodies, setSelectedBodies] = useState(initialBodies)
  const [tolerance, setTolerance] = useState(initialTolerance)
  const [data, setData] = useState<EphemerisResponse | null>(null)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    const controller = new AbortController()
    setLoading(true)
    const params = new URLSearchParams({
      date,
      bodies: selectedBodies.join(','),
    })
    if (tolerance.trim()) {
      params.set('tolerance', tolerance.trim())
      params.set('toleranceUnit', 'AU')
    }
    params.set('includeOrbits', '1')
    fetch(`/api/ephemeris/compare?${params.toString()}`, { signal: controller.signal })
      .then((response) => response.json() as Promise<EphemerisResponse>)
      .then(setData)
      .catch((error) => {
        if (error instanceof DOMException && error.name === 'AbortError') return
        setData({ ok: false, error: String(error), items: [] })
      })
      .finally(() => setLoading(false))
    return () => controller.abort()
  }, [date, selectedBodies, tolerance])

  const validItems = (data?.items ?? []).filter((item) => item.de440?.positionAu && item.vsop?.positionAu)
  const maxDistance = Math.max(
    1,
    ...validItems.flatMap((item) => {
      const points = [
        item.de440?.positionAu,
        item.vsop?.positionAu,
        ...(item.de440?.orbitPathAu ?? []),
        ...(item.vsop?.orbitPathAu ?? []),
      ].filter((point): point is number[] => Array.isArray(point) && point.length >= 2)
      return points.map((point) => Math.hypot(point[0], point[1]))
    }),
  )

  return (
    <div className="ephemeris-card">
      <div className="astro-card-head">
        <div>
          <p className="astro-kicker">A2UI component</p>
          <h3>VSOP / DE440 行星运动对照</h3>
        </div>
        <span>{loading ? '计算中' : 'Python 数值计算'}</span>
      </div>

      <svg className="ephemeris-stage" viewBox="0 0 420 340" role="img" aria-label="VSOP 与 DE440 太阳系天体位置对照">
        <rect x="10" y="10" width="400" height="320" rx="22" fill="#060916" />
        <circle cx="210" cy="170" r="8" fill="#facc15" />
        <text x="226" y="160" className="astro-svg-label">太阳</text>
        {[0.25, 0.5, 0.75, 1].map((ratio) => (
          <circle
            key={ratio}
            cx="210"
            cy="170"
            r={ratio * 168}
            fill="none"
            stroke="#64748b"
            strokeOpacity="0.08"
            strokeDasharray="4 7"
          />
        ))}
        {validItems.map((item) => {
          const de = project(item.de440!.positionAu, maxDistance)
          const vsop = project(item.vsop!.positionAu, maxDistance)
          const color = colors[item.body] ?? '#dbeafe'
          const deOrbit = item.de440?.orbitPathAu ?? []
          const vsopOrbit = item.vsop?.orbitPathAu ?? []
          return (
            <g key={item.body}>
              {deOrbit.length > 2 ? (
                <polyline
                  points={toPolyline(deOrbit, maxDistance)}
                  fill="none"
                  stroke={color}
                  strokeOpacity="0.34"
                  strokeWidth="1.5"
                />
              ) : null}
              {vsopOrbit.length > 2 ? (
                <polyline
                  points={toPolyline(vsopOrbit, maxDistance)}
                  fill="none"
                  stroke={color}
                  strokeOpacity="0.18"
                  strokeWidth="1.3"
                  strokeDasharray="5 5"
                />
              ) : null}
              <line x1={de.x} y1={de.y} x2={vsop.x} y2={vsop.y} stroke={color} strokeOpacity="0.65" strokeWidth="1.6" />
              <circle cx={de.x} cy={de.y} r="5" fill={color} stroke="#f8fafc" strokeOpacity="0.8" />
              <rect x={vsop.x - 4} y={vsop.y - 4} width="8" height="8" transform={`rotate(45 ${vsop.x} ${vsop.y})`} fill={color} opacity="0.72" />
              <text x={de.x + 7} y={de.y - 7} className="astro-svg-label">{item.name}</text>
            </g>
          )
        })}
        <text x="24" y="304" className="astro-svg-label">实线轨道：DE440 · 虚线轨道：VSOP · 连线：模型位置差</text>
        <text x="24" y="320" className="astro-svg-label">圆点：DE440 当前位置 · 菱形：VSOP 当前位置</text>
      </svg>

      <div className="ephemeris-controls">
        <label>
          <span>日期</span>
          <input type="date" value={date} onChange={(event) => setDate(event.target.value)} />
        </label>
        <label>
          <span>精度阈值(AU)</span>
          <input value={tolerance} onChange={(event) => setTolerance(event.target.value)} placeholder="例如 1e-6" />
        </label>
        <div className="body-toggles">
          {bodyOptions.map(([body, label]) => (
            <label key={body}>
              <input
                type="checkbox"
                checked={selectedBodies.includes(body)}
                onChange={(event) => {
                  setSelectedBodies((current) => {
                    if (event.target.checked) return [...current, body]
                    const next = current.filter((item) => item !== body)
                    return next.length ? next : current
                  })
                }}
              />
              <span>{label}</span>
            </label>
          ))}
        </div>
      </div>

      {data?.error ? <p className="astro-note warning">{data.error}</p> : null}
      <div className="ephemeris-table">
        {validItems.slice(0, 8).map((item) => (
          <div key={item.body}>
            <strong>{item.name}</strong>
            <span>DE440 {item.de440!.distanceAu.toFixed(6)} AU</span>
            <span>VSOP {item.vsop!.distanceAu.toFixed(6)} AU</span>
            <em>差 {formatKm(item.delta?.distanceKm)}</em>
            <small>{item.recommendation?.model === 'VSOP_OK' ? 'VSOP 达标' : '建议 DE440'}</small>
          </div>
        ))}
      </div>

      <p className="astro-note">参考系：日心赤道直角坐标。DE440 使用 JPL 星历表插值，VSOP 使用 PyMeeus/VSOP87 解析模型。</p>
    </div>
  )
}

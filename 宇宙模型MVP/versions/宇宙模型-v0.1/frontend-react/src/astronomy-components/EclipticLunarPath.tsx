import { useId, useState } from 'react'

type ComponentProps = {
  node: Record<string, unknown>
}

function numberProp(value: unknown, fallback: number): number {
  return typeof value === 'number' && Number.isFinite(value) ? value : fallback
}

function booleanProp(value: unknown, fallback: boolean): boolean {
  return typeof value === 'boolean' ? value : fallback
}

export function EclipticLunarPath({ node }: ComponentProps) {
  const gradientId = useId().replace(/:/g, '')
  const [moonPositionDeg, setMoonPositionDeg] = useState(numberProp(node.moonPositionDeg, 35))
  const inclinationDeg = numberProp(node.inclinationDeg, 5.145)
  const showNodes = booleanProp(node.showNodes, true)
  const showLabels = booleanProp(node.showLabels, true)

  const angle = (moonPositionDeg / 180) * Math.PI
  const moonX = 180 + Math.cos(angle) * 132
  const moonY = 120 + Math.sin(angle) * 46 - Math.cos(angle) * inclinationDeg * 2.2

  return (
    <div className="astro-card">
      <div className="astro-card-head">
        <div>
          <p className="astro-kicker">A2UI component</p>
          <h3>黄道与白道关系</h3>
        </div>
        <span>{inclinationDeg.toFixed(3)}°</span>
      </div>

      <svg viewBox="0 0 360 240" role="img" aria-label="黄道与白道夹角示意">
        <defs>
          <linearGradient id={gradientId} x1="0" x2="1">
            <stop offset="0%" stopColor="#182544" stopOpacity="0.06" />
            <stop offset="100%" stopColor="#775a19" stopOpacity="0.14" />
          </linearGradient>
        </defs>
        <rect x="18" y="18" width="324" height="204" rx="18" fill={`url(#${gradientId})`} />
        <ellipse cx="180" cy="120" rx="136" ry="45" fill="none" stroke="#775a19" strokeWidth="3" />
        <ellipse
          cx="180"
          cy="120"
          rx="136"
          ry="45"
          fill="none"
          stroke="#1f6f8b"
          strokeWidth="3"
          strokeDasharray="9 7"
          transform="rotate(-5.145 180 120)"
        />
        <circle cx="180" cy="120" r="14" fill="#f4bf45" stroke="#775a19" strokeWidth="2" />
        <circle cx={moonX} cy={moonY} r="9" fill="#dbe4ef" stroke="#182544" strokeWidth="2" />
        {showNodes && (
          <>
            <circle cx="47" cy="120" r="5" fill="#182544" />
            <circle cx="313" cy="120" r="5" fill="#182544" />
            <line x1="47" y1="120" x2="313" y2="120" stroke="#182544" strokeOpacity="0.25" />
          </>
        )}
        {showLabels && (
          <>
            <text x="190" y="103" className="astro-svg-label">
              太阳
            </text>
            <text x="238" y="83" className="astro-svg-label">
              白道（月球轨道）
            </text>
            <text x="222" y="164" className="astro-svg-label">
              黄道（太阳视运动）
            </text>
            <text x="42" y="105" className="astro-svg-label">
              升交点
            </text>
            <text x="286" y="105" className="astro-svg-label">
              降交点
            </text>
          </>
        )}
      </svg>

      <label className="astro-slider">
        <span>月球位置</span>
        <input
          type="range"
          min="0"
          max="360"
          value={moonPositionDeg}
          onChange={(event) => setMoonPositionDeg(Number(event.target.value))}
        />
        <strong>{Math.round(moonPositionDeg)}°</strong>
      </label>

      <p className="astro-note">
        当月球靠近两个交点，同时接近新月或满月，日食或月食才更容易发生。
      </p>
    </div>
  )
}

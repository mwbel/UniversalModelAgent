import { useState } from 'react'

type ComponentProps = {
  node: Record<string, unknown>
}

type Phenomenon = 'lunar_eclipse' | 'solar_eclipse' | 'moon_phase'

function stringProp(value: unknown, fallback: Phenomenon): Phenomenon {
  return value === 'solar_eclipse' || value === 'moon_phase' || value === 'lunar_eclipse'
    ? value
    : fallback
}

function booleanProp(value: unknown, fallback: boolean): boolean {
  return typeof value === 'boolean' ? value : fallback
}

const labels: Record<Phenomenon, string> = {
  lunar_eclipse: '月食',
  solar_eclipse: '日食',
  moon_phase: '月相',
}

export function EclipseGeometry({ node }: ComponentProps) {
  const [phenomenon, setPhenomenon] = useState<Phenomenon>(stringProp(node.phenomenon, 'lunar_eclipse'))
  const [alignment, setAlignment] = useState(0)
  const showShadowCone = booleanProp(node.showShadowCone, true)

  const isSolar = phenomenon === 'solar_eclipse'
  const sun = { x: 48, y: 150 }
  const earth = { x: isSolar ? 284 : 180, y: 150 }
  const moon = {
    x: isSolar ? 180 : 292,
    y: 150 + alignment,
  }
  const litArc = phenomenon === 'moon_phase' ? 52 + alignment * 0.4 : 72

  return (
    <div className="eclipse-card">
      <div className="astro-card-head">
        <div>
          <p className="astro-kicker">A2UI component</p>
          <h3>{labels[phenomenon]}形成几何</h3>
        </div>
        <span>{Math.abs(alignment) <= 8 ? '接近对齐' : '偏离交食'}</span>
      </div>

      <div className="eclipse-tabs" role="group" aria-label="选择现象">
        {(Object.keys(labels) as Phenomenon[]).map((item) => (
          <button
            key={item}
            className={phenomenon === item ? 'active' : ''}
            onClick={() => setPhenomenon(item)}
            type="button"
          >
            {labels[item]}
          </button>
        ))}
      </div>

      <svg viewBox="0 0 360 280" role="img" aria-label={`${labels[phenomenon]}形成几何示意`}>
        <defs>
          <linearGradient id="sunGlow" x1="0" x2="1">
            <stop offset="0%" stopColor="#ffe28a" />
            <stop offset="100%" stopColor="#f59e0b" />
          </linearGradient>
          <linearGradient id="earthBlue" x1="0" x2="1">
            <stop offset="0%" stopColor="#7dd3fc" />
            <stop offset="100%" stopColor="#2563eb" />
          </linearGradient>
          <linearGradient id="moonGrey" x1="0" x2="1">
            <stop offset="0%" stopColor="#f8fafc" />
            <stop offset="100%" stopColor="#94a3b8" />
          </linearGradient>
        </defs>

        <rect x="12" y="18" width="336" height="244" rx="20" fill="#101a3d" />
        <circle cx={sun.x} cy={sun.y} r="26" fill="url(#sunGlow)" />
        <line x1="74" y1="118" x2="334" y2="118" stroke="#fde68a" strokeOpacity="0.35" strokeWidth="2" />
        <line x1="74" y1="182" x2="334" y2="182" stroke="#fde68a" strokeOpacity="0.35" strokeWidth="2" />

        {showShadowCone && phenomenon !== 'moon_phase' && (
          <polygon
            points={
              isSolar
                ? `${moon.x + 14},${moon.y - 18} 340,${moon.y - 2} ${moon.x + 14},${moon.y + 18}`
                : `${earth.x + 20},${earth.y - 28} 340,${earth.y} ${earth.x + 20},${earth.y + 28}`
            }
            fill="#020617"
            opacity="0.72"
          />
        )}

        <circle cx={earth.x} cy={earth.y} r="22" fill="url(#earthBlue)" stroke="#bfdbfe" strokeWidth="2" />
        <circle cx={moon.x} cy={moon.y} r="14" fill="url(#moonGrey)" stroke="#e2e8f0" strokeWidth="2" />

        {phenomenon === 'moon_phase' && (
          <path
            d={`M ${moon.x} ${moon.y - 14} C ${moon.x + litArc / 4} ${moon.y - 8}, ${moon.x + litArc / 4} ${
              moon.y + 8
            }, ${moon.x} ${moon.y + 14}`}
            fill="none"
            stroke="#fef3c7"
            strokeWidth="5"
            strokeLinecap="round"
          />
        )}

        <line x1="28" y1={earth.y} x2="332" y2={earth.y} stroke="#93c5fd" strokeDasharray="8 8" strokeOpacity="0.55" />
        <text x={sun.x - 16} y={sun.y + 48} className="astro-svg-label">
          太阳
        </text>
        <text x={earth.x - 16} y={earth.y + 48} className="astro-svg-label">
          地球
        </text>
        <text x={moon.x - 16} y={moon.y - 28} className="astro-svg-label">
          月球
        </text>
        <text x="28" y="42" className="astro-svg-label">
          {isSolar ? '月球本影落到地球附近形成日食' : phenomenon === 'moon_phase' ? '受光面比例形成月相' : '月球进入地球本影形成月食'}
        </text>
      </svg>

      <label className="astro-slider">
        <span>月球偏离轨道面</span>
        <input
          type="range"
          min="-48"
          max="48"
          value={alignment}
          onChange={(event) => setAlignment(Number(event.target.value))}
        />
        <strong>{alignment > 0 ? `+${alignment}` : alignment}</strong>
      </label>

      <p className="astro-note">
        拖动偏离量可以看到：只有太阳、地球、月球接近共线，并且月球靠近黄白交点时，交食条件才成立。
      </p>
    </div>
  )
}

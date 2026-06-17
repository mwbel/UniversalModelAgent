import { useMemo, useState } from 'react'

type ComponentProps = {
  node: Record<string, unknown>
}

function numberProp(value: unknown, fallback: number) {
  return typeof value === 'number' && Number.isFinite(value) ? value : fallback
}

function booleanProp(value: unknown, fallback: boolean) {
  return typeof value === 'boolean' ? value : fallback
}

function stringProp(value: unknown, fallback: string) {
  return typeof value === 'string' && value.trim() ? value : fallback
}

function todayDateInput() {
  return new Date().toISOString().slice(0, 10)
}

function currentTimeInput() {
  return new Date().toTimeString().slice(0, 5)
}

function formatSigned(value: number, digits = 2) {
  return `${value >= 0 ? '+' : ''}${value.toFixed(digits)}`
}

export function GeocentricDailyMotion({ node }: ComponentProps) {
  const [latitude, setLatitude] = useState(numberProp(node.latitude, 31.23))
  const [longitude, setLongitude] = useState(numberProp(node.longitude, 121.47))
  const [date, setDate] = useState(() => {
    const value = stringProp(node.date, 'today')
    return value === 'today' ? todayDateInput() : value
  })
  const [time, setTime] = useState(() => {
    const value = stringProp(node.time, 'now')
    return value === 'now' ? currentTimeInput() : value.slice(0, 5)
  })
  const [showTrails, setShowTrails] = useState(booleanProp(node.showTrails, true))
  const [showEquatorialGrid, setShowEquatorialGrid] = useState(booleanProp(node.showEquatorialGrid, true))
  const [showHorizonGrid, setShowHorizonGrid] = useState(booleanProp(node.showHorizonGrid, true))

  const urls = useMemo(() => {
    const params = new URLSearchParams({
      page: 'geocentric-daily-motion-3d',
      embed: '1',
      lat: latitude.toFixed(2),
      lon: longitude.toFixed(2),
      date,
      time,
      showTrails: String(showTrails),
      showEquatorialGrid: String(showEquatorialGrid),
      showHorizonGrid: String(showHorizonGrid),
    })
    const galleryParams = new URLSearchParams(params)
    galleryParams.delete('embed')
    return {
      embed: `/interactive-visualizations/index.html?${params.toString()}`,
      gallery: `/interactive-visualizations/index.html?${galleryParams.toString()}`,
    }
  }, [date, latitude, longitude, showEquatorialGrid, showHorizonGrid, showTrails, time])

  return (
    <div className="geocentric-card">
      <div className="astro-card-head">
        <div>
          <p className="astro-kicker">A2UI component</p>
          <h3>地心天球周日视运动 3D</h3>
        </div>
        <a href={urls.gallery} rel="noreferrer" target="_blank">
          新窗口打开
        </a>
      </div>

      <div className="geocentric-layout">
        <div className="geocentric-controls">
          <label className="astro-slider">
            <span>纬度</span>
            <input
              type="range"
              min="-90"
              max="90"
              step="0.1"
              value={latitude}
              onChange={(event) => setLatitude(Number(event.target.value))}
            />
            <strong>{formatSigned(latitude)}</strong>
          </label>
          <label className="astro-slider">
            <span>经度</span>
            <input
              type="range"
              min="-180"
              max="180"
              step="0.1"
              value={longitude}
              onChange={(event) => setLongitude(Number(event.target.value))}
            />
            <strong>{formatSigned(longitude)}</strong>
          </label>
          <div className="geocentric-time-row">
            <label>
              <span>日期</span>
              <input type="date" value={date} onChange={(event) => setDate(event.target.value)} />
            </label>
            <label>
              <span>时间</span>
              <input type="time" value={time} onChange={(event) => setTime(event.target.value)} />
            </label>
          </div>
          <div className="geocentric-toggles">
            <label>
              <input type="checkbox" checked={showTrails} onChange={(event) => setShowTrails(event.target.checked)} />
              <span>轨迹</span>
            </label>
            <label>
              <input
                type="checkbox"
                checked={showEquatorialGrid}
                onChange={(event) => setShowEquatorialGrid(event.target.checked)}
              />
              <span>天球网格</span>
            </label>
            <label>
              <input
                type="checkbox"
                checked={showHorizonGrid}
                onChange={(event) => setShowHorizonGrid(event.target.checked)}
              />
              <span>地平网格</span>
            </label>
          </div>
        </div>

        <iframe className="geocentric-frame" src={urls.embed} title="地心天球周日视运动 3D" loading="lazy" />
      </div>

      <p className="astro-note">拖动纬度、经度或时间，3D 天球会按观测地点和时刻重新绘制；新窗口可查看完整控制面板和大图。</p>
    </div>
  )
}

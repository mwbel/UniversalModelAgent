import React, { useState } from 'react'
import './VisualizationPanel.css'

interface Scene {
  id: string
  name: string
  description: string
}

const VisualizationPanel: React.FC = () => {
  const [activeScene, setActiveScene] = useState<string>('solar-system')
  const [isFullscreen, setIsFullscreen] = useState(false)

  const scenes: Scene[] = [
    { id: 'solar-system', name: '太阳系', description: '太阳系行星运行模拟' },
    { id: 'big-bang', name: '宇宙演化', description: '大爆炸宇宙演化时间线' },
    { id: 'kalachakra', name: '时轮金刚', description: '时轮金刚三重时轮可视化' },
    { id: 'galaxy', name: '星系碰撞', description: '星系碰撞模拟' }
  ]

  const toggleFullscreen = () => {
    setIsFullscreen(!isFullscreen)
  }

  return (
    <div className={`visualization-panel ${isFullscreen ? 'fullscreen' : ''}`}>
      <div className="viz-header">
        <h2 className="viz-title">3D 可视化</h2>
        <div className="viz-controls">
          <button className="control-btn" title="截图">📷</button>
          <button className="control-btn" title="设置">⚙️</button>
          <button className="control-btn" onClick={toggleFullscreen} title="全屏">
            {isFullscreen ? '⊗' : '⛶'}
          </button>
        </div>
      </div>

      <div className="scene-selector">
        {scenes.map(scene => (
          <button
            key={scene.id}
            className={`scene-btn ${activeScene === scene.id ? 'active' : ''}`}
            onClick={() => setActiveScene(scene.id)}
            title={scene.description}
          >
            {scene.name}
          </button>
        ))}
      </div>

      <div className="viz-canvas">
        <div className="canvas-placeholder">
          <div className="placeholder-icon">🌌</div>
          <div className="placeholder-text">
            <h3>{scenes.find(s => s.id === activeScene)?.name}</h3>
            <p>{scenes.find(s => s.id === activeScene)?.description}</p>
            <p className="placeholder-hint">3D 场景将在此处渲染</p>
          </div>
        </div>
      </div>

      <div className="viz-info">
        <div className="info-section">
          <h4 className="info-title">场景信息</h4>
          <div className="info-content">
            <div className="info-item">
              <span className="info-label">当前场景:</span>
              <span className="info-value">{scenes.find(s => s.id === activeScene)?.name}</span>
            </div>
            <div className="info-item">
              <span className="info-label">渲染状态:</span>
              <span className="info-value status-ready">就绪</span>
            </div>
          </div>
        </div>

        <div className="info-section">
          <h4 className="info-title">交互提示</h4>
          <div className="info-content">
            <div className="hint-item">🖱️ 左键拖动 - 旋转视角</div>
            <div className="hint-item">🖱️ 右键拖动 - 平移视角</div>
            <div className="hint-item">🖱️ 滚轮 - 缩放视角</div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default VisualizationPanel

import React, { useState } from 'react'
import './Sidebar.css'

interface NavItem {
  id: string
  title: string
  icon: string
}

const Sidebar: React.FC = () => {
  const [activeItem, setActiveItem] = useState<string>('chat')
  const [conversations, setConversations] = useState<Array<{ id: string; title: string }>>([
    { id: '1', title: '宇宙大爆炸理论' },
    { id: '2', title: '时轮金刚体系探索' },
    { id: '3', title: '太阳系行星运动' }
  ])

  const navItems: NavItem[] = [
    { id: 'chat', title: '对话', icon: '💬' },
    { id: 'scenes', title: '场景', icon: '🌌' },
    { id: 'knowledge', title: '知识库', icon: '📚' },
    { id: 'history', title: '历史', icon: '🕐' }
  ]

  const handleRagClick = () => {
    window.open('https://manyragsfronted.cpolar.top/', '_blank')
  }

  return (
    <div className="sidebar">
      <div className="sidebar-header">
        <h1 className="sidebar-title">宇宙模型</h1>
        <button className="new-chat-btn">+ 新对话</button>
      </div>

      <nav className="sidebar-nav">
        {navItems.map(item => (
          <button
            key={item.id}
            className={`nav-item ${activeItem === item.id ? 'active' : ''}`}
            onClick={() => setActiveItem(item.id)}
          >
            <span className="nav-icon">{item.icon}</span>
            <span className="nav-label">{item.title}</span>
          </button>
        ))}
      </nav>

      <div className="conversation-list">
        <h3 className="list-title">最近对话</h3>
        {conversations.map(conv => (
          <div key={conv.id} className="conversation-item">
            <span className="conversation-icon">💭</span>
            <span className="conversation-title">{conv.title}</span>
          </div>
        ))}
      </div>

      <div className="sidebar-footer">
        <button className="rag-btn" onClick={handleRagClick}>
          🔍 RAG 服务
        </button>
        <button className="settings-btn">⚙️ 设置</button>
      </div>
    </div>
  )
}

export default Sidebar

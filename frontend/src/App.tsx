import React from 'react'
import './App.css'
import Sidebar from './components/Sidebar'
import ChatArea from './components/ChatArea'
import VisualizationPanel from './components/VisualizationPanel'

const App: React.FC = () => {
  return (
    <div className="app-container">
      <Sidebar />
      <ChatArea />
      <VisualizationPanel />
    </div>
  )
}

export default App

import React, { useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Sidebar from './components/Sidebar'
import Header from './components/Header'
import Upload from './pages/Upload'
import About from './pages/About'

function App() {
  const [darkMode, setDarkMode] = useState(false)
  const [sidebarOpen, setSidebarOpen] = useState(true)

  return (
    <Router>
      <div className={`min-h-screen ${darkMode ? 'dark' : ''} bg-background dark:bg-gray-900`}>
        <div className="flex min-h-screen bg-background dark:bg-gray-900">
          <Sidebar isOpen={sidebarOpen} setIsOpen={setSidebarOpen} />
          
          <div className={`flex-1 transition-all duration-300 ${sidebarOpen ? 'ml-64' : 'ml-16'} min-h-screen bg-background dark:bg-gray-900`}>
            <Header darkMode={darkMode} setDarkMode={setDarkMode} />
            
            <main className="p-6 bg-background dark:bg-gray-900 min-h-screen">
              <Routes>
                <Route path="/" element={<Upload />} />
                <Route path="/upload" element={<Upload />} />
                <Route path="/about" element={<About />} />
              </Routes>
            </main>
          </div>
        </div>
      </div>
    </Router>
  )
}

export default App
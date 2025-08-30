import React from 'react'
import { Link, useLocation } from 'react-router-dom'
import { Upload, Info, Menu, X } from 'lucide-react'

const Sidebar = ({ isOpen, setIsOpen }) => {
  const location = useLocation()
  
  const menuItems = [
    { path: '/upload', icon: Upload, label: 'Upload Scan' },
    { path: '/about', icon: Info, label: 'About' },
  ]

  return (
    <>
      <div className={`fixed inset-y-0 left-0 z-50 w-64 bg-surface dark:bg-gray-800 shadow-xl transform transition-transform duration-300 ${isOpen ? 'translate-x-0' : '-translate-x-48'}`}>
        <div className="flex items-center justify-between p-6 border-b border-border-color dark:border-gray-700">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-primary rounded-xl flex items-center justify-center">
              <span className="text-white font-bold text-lg">K</span>
            </div>
            {isOpen && (
              <div>
                <h1 className="font-bold text-lg text-text-primary dark:text-white">KidneyAI Pro</h1>
                <p className="text-sm text-text-secondary dark:text-gray-400">Medical AI Platform</p>
              </div>
            )}
          </div>
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors text-text-primary dark:text-white"
          >
            {isOpen ? <X size={20} /> : <Menu size={20} />}
          </button>
        </div>

        <nav className="p-4 space-y-2">
          {menuItems.map((item) => {
            const Icon = item.icon
            const isActive = location.pathname === item.path
            
            return (
              <Link
                key={item.path}
                to={item.path}
                className={`sidebar-item ${isActive ? 'active' : ''} ${!isOpen ? 'justify-center' : ''}`}
              >
                <Icon size={20} />
                {isOpen && <span className="font-medium">{item.label}</span>}
              </Link>
            )
          })}
        </nav>

        {isOpen && (
          <div className="absolute bottom-6 left-4 right-4">
            <div className="bg-primary/10 rounded-xl p-4">
              <div className="flex items-center gap-2 mb-2">
                <div className="w-2 h-2 bg-secondary rounded-full animate-pulse-slow"></div>
                <span className="text-sm font-medium text-primary">AI System Online</span>
              </div>
              <p className="text-xs text-text-secondary dark:text-gray-400">
                Ready for medical image analysis
              </p>
            </div>
          </div>
        )}
      </div>
    </>
  )
}

export default Sidebar
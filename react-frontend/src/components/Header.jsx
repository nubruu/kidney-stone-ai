import React from 'react'
import { Moon, Sun, Settings } from 'lucide-react'

const Header = ({ darkMode, setDarkMode }) => {
  return (
    <header className="bg-surface dark:bg-gray-800 border-b border-border-color dark:border-gray-700 px-6 py-4">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-text-primary dark:text-white">
            AI Medical Diagnostics
          </h2>
          <p className="text-text-secondary dark:text-gray-400">
            Advanced kidney stone detection system
          </p>
        </div>

        <div className="flex items-center gap-4">


          <button className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
            <Settings size={20} className="text-text-secondary dark:text-gray-400" />
          </button>

          <button
            onClick={() => setDarkMode(!darkMode)}
            className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
          >
            {darkMode ? (
              <Sun size={20} className="text-yellow-500" />
            ) : (
              <Moon size={20} className="text-text-secondary" />
            )}
          </button>


        </div>
      </div>
    </header>
  )
}

export default Header
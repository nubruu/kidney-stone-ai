import React, { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { Calendar, Download, Eye, Trash2, TrendingUp } from 'lucide-react'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'

const History = () => {
  const [history, setHistory] = useState([])
  const [selectedScan, setSelectedScan] = useState(null)

  useEffect(() => {
    const savedHistory = JSON.parse(localStorage.getItem('scanHistory') || '[]')
    setHistory(savedHistory)
  }, [])

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    })
  }

  const deleteScan = (id) => {
    const updatedHistory = history.filter(scan => scan.id !== id)
    setHistory(updatedHistory)
    localStorage.setItem('scanHistory', JSON.stringify(updatedHistory))
  }

  const chartData = history.slice(0, 10).reverse().map((scan, index) => ({
    name: `Scan ${index + 1}`,
    confidence: scan.result.confidence,
    date: new Date(scan.date).toLocaleDateString()
  }))

  return (
    <div className="space-y-6">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="flex items-center justify-between"
      >
        <div>
          <h1 className="text-3xl font-bold text-text-primary dark:text-white">Scan History</h1>
          <p className="text-text-secondary dark:text-gray-400">
            View and manage your previous medical scans
          </p>
        </div>
        <div className="flex items-center gap-2 text-text-secondary dark:text-gray-400">
          <Calendar size={20} />
          <span>{history.length} total scans</span>
        </div>
      </motion.div>

      {history.length > 0 && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="card"
        >
          <h2 className="text-xl font-bold text-text-primary dark:text-white mb-4 flex items-center gap-2">
            <TrendingUp size={24} />
            Confidence Trend
          </h2>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={chartData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis domain={[0, 100]} />
              <Tooltip 
                formatter={(value) => [`${value}%`, 'Confidence']}
                labelFormatter={(label) => `${label}`}
              />
              <Line 
                type="monotone" 
                dataKey="confidence" 
                stroke="#1E88E5" 
                strokeWidth={3}
                dot={{ fill: '#1E88E5', strokeWidth: 2, r: 6 }}
              />
            </LineChart>
          </ResponsiveContainer>
        </motion.div>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2">
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            className="card"
          >
            <h2 className="text-xl font-bold text-text-primary dark:text-white mb-4">
              Recent Scans
            </h2>
            
            {history.length === 0 ? (
              <div className="text-center py-12">
                <div className="w-16 h-16 bg-gray-100 dark:bg-gray-700 rounded-full flex items-center justify-center mx-auto mb-4">
                  <Calendar size={32} className="text-text-secondary dark:text-gray-400" />
                </div>
                <p className="text-text-secondary dark:text-gray-400">
                  No scan history available
                </p>
                <p className="text-sm text-text-secondary dark:text-gray-400 mt-2">
                  Upload your first medical scan to see it here
                </p>
              </div>
            ) : (
              <div className="space-y-4 max-h-96 overflow-y-auto">
                {history.map((scan, index) => (
                  <motion.div
                    key={scan.id}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: index * 0.1 }}
                    className="flex items-center gap-4 p-4 bg-gray-50 dark:bg-gray-700 rounded-xl hover:bg-gray-100 dark:hover:bg-gray-600 transition-colors cursor-pointer"
                    onClick={() => setSelectedScan(scan)}
                  >
                    <img
                      src={scan.image}
                      alt="Scan thumbnail"
                      className="w-16 h-16 object-cover rounded-lg"
                    />
                    
                    <div className="flex-1">
                      <div className="flex items-center justify-between mb-1">
                        <h3 className="font-semibold text-text-primary dark:text-white">
                          {scan.filename}
                        </h3>
                        <span className={`px-2 py-1 rounded-full text-xs font-semibold ${
                          scan.result.prediction === 'Stone'
                            ? 'bg-danger/10 text-danger'
                            : 'bg-secondary/10 text-secondary'
                        }`}>
                          {scan.result.prediction === 'Stone' ? 'Stone Detected' : 'Normal'}
                        </span>
                      </div>
                      <div className="flex items-center justify-between text-sm text-text-secondary dark:text-gray-400">
                        <span>{formatDate(scan.date)}</span>
                        <span>Confidence: {scan.result.confidence}%</span>
                      </div>
                    </div>

                    <div className="flex items-center gap-2">
                      <button
                        onClick={(e) => {
                          e.stopPropagation()
                          // Mock download
                          alert('Report downloaded!')
                        }}
                        className="p-2 text-text-secondary hover:text-primary transition-colors"
                      >
                        <Download size={16} />
                      </button>
                      <button
                        onClick={(e) => {
                          e.stopPropagation()
                          deleteScan(scan.id)
                        }}
                        className="p-2 text-text-secondary hover:text-danger transition-colors"
                      >
                        <Trash2 size={16} />
                      </button>
                    </div>
                  </motion.div>
                ))}
              </div>
            )}
          </motion.div>
        </div>

        <div>
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            className="card"
          >
            <h2 className="text-xl font-bold text-text-primary dark:text-white mb-4">
              Scan Details
            </h2>
            
            {selectedScan ? (
              <div className="space-y-4">
                <img
                  src={selectedScan.image}
                  alt="Selected scan"
                  className="w-full h-48 object-cover rounded-xl"
                />
                
                <div className="space-y-3">
                  <div>
                    <label className="text-sm font-medium text-text-secondary dark:text-gray-400">
                      Filename
                    </label>
                    <p className="text-text-primary dark:text-white">{selectedScan.filename}</p>
                  </div>
                  
                  <div>
                    <label className="text-sm font-medium text-text-secondary dark:text-gray-400">
                      Analysis Date
                    </label>
                    <p className="text-text-primary dark:text-white">{formatDate(selectedScan.date)}</p>
                  </div>
                  
                  <div>
                    <label className="text-sm font-medium text-text-secondary dark:text-gray-400">
                      Result
                    </label>
                    <p className={`font-semibold ${
                      selectedScan.result.prediction === 'Stone' ? 'text-danger' : 'text-secondary'
                    }`}>
                      {selectedScan.result.prediction === 'Stone' ? 'Kidney Stone Detected' : 'No Kidney Stone Detected'}
                    </p>
                  </div>
                  
                  <div>
                    <label className="text-sm font-medium text-text-secondary dark:text-gray-400">
                      Confidence Score
                    </label>
                    <div className="flex items-center gap-3">
                      <div className="flex-1 bg-gray-200 dark:bg-gray-600 rounded-full h-2">
                        <div
                          className={`h-2 rounded-full ${
                            selectedScan.result.prediction === 'Stone' ? 'bg-danger' : 'bg-secondary'
                          }`}
                          style={{ width: `${selectedScan.result.confidence}%` }}
                        ></div>
                      </div>
                      <span className="font-semibold text-text-primary dark:text-white">
                        {selectedScan.result.confidence}%
                      </span>
                    </div>
                  </div>
                </div>

                <div className="flex gap-2">
                  <button className="btn-secondary flex-1 flex items-center justify-center gap-2">
                    <Eye size={16} />
                    View Heatmap
                  </button>
                  <button className="btn-primary flex-1 flex items-center justify-center gap-2">
                    <Download size={16} />
                    Download
                  </button>
                </div>
              </div>
            ) : (
              <div className="text-center py-12">
                <div className="w-16 h-16 bg-gray-100 dark:bg-gray-700 rounded-full flex items-center justify-center mx-auto mb-4">
                  <Eye size={32} className="text-text-secondary dark:text-gray-400" />
                </div>
                <p className="text-text-secondary dark:text-gray-400">
                  Select a scan to view details
                </p>
              </div>
            )}
          </motion.div>
        </div>
      </div>
    </div>
  )
}

export default History
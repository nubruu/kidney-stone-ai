import React from 'react'
import { motion } from 'framer-motion'
import { Activity, Users, Clock, TrendingUp, Upload, Eye } from 'lucide-react'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'

const Home = () => {
  const stats = [
    { icon: Activity, label: 'Scans Analyzed', value: '1,247', change: '+12%' },
    { icon: Users, label: 'Patients Served', value: '892', change: '+8%' },
    { icon: Clock, label: 'Avg. Analysis Time', value: '2.3s', change: '-15%' },
    { icon: TrendingUp, label: 'Accuracy Rate', value: '94.7%', change: '+2%' },
  ]

  const chartData = [
    { name: 'Jan', accuracy: 92 },
    { name: 'Feb', accuracy: 93 },
    { name: 'Mar', accuracy: 94 },
    { name: 'Apr', accuracy: 95 },
    { name: 'May', accuracy: 94 },
    { name: 'Jun', accuracy: 95 },
  ]

  return (
    <div className="space-y-6">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="bg-gradient-to-r from-primary to-blue-600 rounded-2xl p-8 text-white"
      >
        <h1 className="text-3xl font-bold mb-2">Welcome to KidneyAI Pro</h1>
        <p className="text-blue-100 mb-6">
          Advanced AI-powered kidney stone detection with 94.7% accuracy
        </p>
        <div className="flex gap-4">
          <button className="bg-white text-primary px-6 py-3 rounded-xl font-semibold hover:bg-gray-100 transition-colors flex items-center gap-2">
            <Upload size={20} />
            Upload New Scan
          </button>
          <button className="border border-white/30 px-6 py-3 rounded-xl font-semibold hover:bg-white/10 transition-colors flex items-center gap-2">
            <Eye size={20} />
            View Demo
          </button>
        </div>
      </motion.div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((stat, index) => {
          const Icon = stat.icon
          return (
            <motion.div
              key={stat.label}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
              className="card"
            >
              <div className="flex items-center justify-between mb-4">
                <div className="p-3 bg-primary/10 rounded-xl">
                  <Icon size={24} className="text-primary" />
                </div>
                <span className="text-secondary font-semibold text-sm">{stat.change}</span>
              </div>
              <h3 className="text-2xl font-bold text-text-primary dark:text-white mb-1">
                {stat.value}
              </h3>
              <p className="text-text-secondary dark:text-gray-400">{stat.label}</p>
            </motion.div>
          )
        })}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          className="card"
        >
          <h3 className="text-xl font-bold text-text-primary dark:text-white mb-4">
            Accuracy Trend
          </h3>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={chartData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Line 
                type="monotone" 
                dataKey="accuracy" 
                stroke="#1E88E5" 
                strokeWidth={3}
                dot={{ fill: '#1E88E5', strokeWidth: 2, r: 6 }}
              />
            </LineChart>
          </ResponsiveContainer>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          className="card"
        >
          <h3 className="text-xl font-bold text-text-primary dark:text-white mb-4">
            Recent Activity
          </h3>
          <div className="space-y-4">
            {[
              { time: '2 min ago', action: 'Scan analyzed', result: 'No stone detected', confidence: '92%' },
              { time: '15 min ago', action: 'Scan analyzed', result: 'Stone detected', confidence: '87%' },
              { time: '1 hour ago', action: 'Scan analyzed', result: 'No stone detected', confidence: '95%' },
              { time: '2 hours ago', action: 'Scan analyzed', result: 'Stone detected', confidence: '89%' },
            ].map((activity, index) => (
              <div key={index} className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-700 rounded-xl">
                <div>
                  <p className="font-medium text-text-primary dark:text-white">{activity.action}</p>
                  <p className="text-sm text-text-secondary dark:text-gray-400">{activity.time}</p>
                </div>
                <div className="text-right">
                  <p className={`font-semibold ${activity.result.includes('detected') && !activity.result.includes('No') ? 'text-danger' : 'text-secondary'}`}>
                    {activity.result}
                  </p>
                  <p className="text-sm text-text-secondary dark:text-gray-400">{activity.confidence}</p>
                </div>
              </div>
            ))}
          </div>
        </motion.div>
      </div>
    </div>
  )
}

export default Home
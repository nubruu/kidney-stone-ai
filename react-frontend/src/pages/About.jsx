import React from 'react'
import { motion } from 'framer-motion'
import { Brain, Shield, Clock, Award, AlertTriangle, Users, Target, Zap } from 'lucide-react'

const About = () => {
  const features = [
    {
      icon: Brain,
      title: 'Advanced AI Technology',
      description: 'State-of-the-art deep learning models trained on thousands of medical images for accurate detection.'
    },
    {
      icon: Clock,
      title: 'Instant Analysis',
      description: 'Get results in seconds with our optimized AI pipeline, enabling faster medical decision-making.'
    },
    {
      icon: Shield,
      title: 'Secure & Private',
      description: 'Your medical data is processed securely and never stored permanently on our servers.'
    },
    {
      icon: Award,
      title: '94.7% Accuracy',
      description: 'Clinically validated accuracy rate with continuous improvement through machine learning.'
    }
  ]

  const stats = [
    { icon: Users, value: '10,000+', label: 'Patients Served' },
    { icon: Target, value: '94.7%', label: 'Accuracy Rate' },
    { icon: Zap, value: '2.3s', label: 'Average Analysis Time' },
    { icon: Brain, value: '50,000+', label: 'Images Analyzed' }
  ]

  return (
    <div className="space-y-8">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center"
      >
        <h1 className="text-4xl font-bold text-text-primary dark:text-white mb-4">
          About KidneyAI Pro
        </h1>
        <p className="text-xl text-text-secondary dark:text-gray-400 max-w-3xl mx-auto">
          Advanced AI-powered kidney stone detection system designed to assist healthcare professionals 
          in early diagnosis and treatment planning.
        </p>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="bg-gradient-to-r from-primary to-blue-600 rounded-2xl p-8 text-white"
      >
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
          {stats.map((stat, index) => {
            const Icon = stat.icon
            return (
              <div key={index} className="text-center">
                <Icon size={32} className="mx-auto mb-2 opacity-80" />
                <div className="text-2xl font-bold mb-1">{stat.value}</div>
                <div className="text-blue-100 text-sm">{stat.label}</div>
              </div>
            )
          })}
        </div>
      </motion.div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {features.map((feature, index) => {
          const Icon = feature.icon
          return (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3 + index * 0.1 }}
              className="card"
            >
              <div className="flex items-start gap-4">
                <div className="p-3 bg-primary/10 rounded-xl">
                  <Icon size={24} className="text-primary" />
                </div>
                <div>
                  <h3 className="text-xl font-bold text-text-primary dark:text-white mb-2">
                    {feature.title}
                  </h3>
                  <p className="text-text-secondary dark:text-gray-400">
                    {feature.description}
                  </p>
                </div>
              </div>
            </motion.div>
          )
        })}
      </div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.7 }}
        className="card"
      >
        <h2 className="text-2xl font-bold text-text-primary dark:text-white mb-4">
          Why Early Detection Matters
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="text-center">
            <div className="w-16 h-16 bg-secondary/10 rounded-full flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl">⚡</span>
            </div>
            <h3 className="font-semibold text-text-primary dark:text-white mb-2">
              Faster Treatment
            </h3>
            <p className="text-text-secondary dark:text-gray-400 text-sm">
              Early detection enables prompt treatment, reducing complications and recovery time.
            </p>
          </div>
          
          <div className="text-center">
            <div className="w-16 h-16 bg-warning/10 rounded-full flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl">💰</span>
            </div>
            <h3 className="font-semibold text-text-primary dark:text-white mb-2">
              Cost Effective
            </h3>
            <p className="text-text-secondary dark:text-gray-400 text-sm">
              Prevents expensive emergency procedures and reduces overall healthcare costs.
            </p>
          </div>
          
          <div className="text-center">
            <div className="w-16 h-16 bg-danger/10 rounded-full flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl">🛡️</span>
            </div>
            <h3 className="font-semibold text-text-primary dark:text-white mb-2">
              Prevent Complications
            </h3>
            <p className="text-text-secondary dark:text-gray-400 text-sm">
              Avoids serious complications like kidney damage, infections, and chronic pain.
            </p>
          </div>
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.9 }}
        className="card bg-warning/5 border-warning/20"
      >
        <div className="flex items-start gap-4">
          <AlertTriangle size={24} className="text-warning mt-1" />
          <div>
            <h3 className="text-xl font-bold text-text-primary dark:text-white mb-2">
              Medical Disclaimer
            </h3>
            <div className="space-y-2 text-text-secondary dark:text-gray-400">
              <p>
                <strong>Important:</strong> This AI system is designed for educational and research purposes only. 
                It is not intended to replace professional medical diagnosis or treatment.
              </p>
              <p>
                Always consult with qualified healthcare professionals for proper medical diagnosis, 
                treatment recommendations, and medical advice. Do not rely solely on AI analysis 
                for medical decisions.
              </p>
              <p>
                The accuracy rates mentioned are based on research data and may vary in real-world 
                clinical settings. This tool should be used as a supplementary aid alongside 
                professional medical expertise.
              </p>
            </div>
          </div>
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 1.1 }}
        className="card"
      >
        <h2 className="text-2xl font-bold text-text-primary dark:text-white mb-4">
          How It Works
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div className="text-center">
            <div className="w-12 h-12 bg-primary text-white rounded-full flex items-center justify-center mx-auto mb-3 font-bold">
              1
            </div>
            <h4 className="font-semibold text-text-primary dark:text-white mb-2">Upload Image</h4>
            <p className="text-sm text-text-secondary dark:text-gray-400">
              Upload kidney ultrasound or CT scan image
            </p>
          </div>
          
          <div className="text-center">
            <div className="w-12 h-12 bg-primary text-white rounded-full flex items-center justify-center mx-auto mb-3 font-bold">
              2
            </div>
            <h4 className="font-semibold text-text-primary dark:text-white mb-2">AI Analysis</h4>
            <p className="text-sm text-text-secondary dark:text-gray-400">
              Advanced neural networks analyze the image
            </p>
          </div>
          
          <div className="text-center">
            <div className="w-12 h-12 bg-primary text-white rounded-full flex items-center justify-center mx-auto mb-3 font-bold">
              3
            </div>
            <h4 className="font-semibold text-text-primary dark:text-white mb-2">Get Results</h4>
            <p className="text-sm text-text-secondary dark:text-gray-400">
              Receive prediction with confidence score
            </p>
          </div>
          
          <div className="text-center">
            <div className="w-12 h-12 bg-primary text-white rounded-full flex items-center justify-center mx-auto mb-3 font-bold">
              4
            </div>
            <h4 className="font-semibold text-text-primary dark:text-white mb-2">Visual Explanation</h4>
            <p className="text-sm text-text-secondary dark:text-gray-400">
              View Grad-CAM heatmap for AI reasoning
            </p>
          </div>
        </div>
      </motion.div>
    </div>
  )
}

export default About
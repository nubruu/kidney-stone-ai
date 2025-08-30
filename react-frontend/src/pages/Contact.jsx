import React, { useState } from 'react'
import { motion } from 'framer-motion'
import { Mail, Phone, MapPin, Send, MessageCircle, Clock, Globe } from 'lucide-react'

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: ''
  })
  const [isSubmitting, setIsSubmitting] = useState(false)

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setIsSubmitting(true)
    
    // Simulate form submission
    setTimeout(() => {
      alert('Message sent successfully! We\'ll get back to you soon.')
      setFormData({ name: '', email: '', subject: '', message: '' })
      setIsSubmitting(false)
    }, 2000)
  }

  const contactInfo = [
    {
      icon: Mail,
      title: 'Email Support',
      value: 'support@kidneyai.pro',
      description: 'Get help with technical issues'
    },
    {
      icon: Phone,
      title: 'Phone Support',
      value: '+1 (555) 123-4567',
      description: 'Mon-Fri, 9AM-6PM EST'
    },
    {
      icon: MapPin,
      title: 'Office Location',
      value: 'San Francisco, CA',
      description: 'Medical AI Research Center'
    },
    {
      icon: Clock,
      title: 'Response Time',
      value: '< 24 hours',
      description: 'Average response time'
    }
  ]

  const faqs = [
    {
      question: 'How accurate is the AI detection?',
      answer: 'Our AI system has a clinically validated accuracy rate of 94.7%, continuously improved through machine learning on diverse medical datasets.'
    },
    {
      question: 'Is my medical data secure?',
      answer: 'Yes, all medical images are processed securely and never stored permanently. We follow HIPAA compliance standards for data protection.'
    },
    {
      question: 'Can I use this for actual medical diagnosis?',
      answer: 'No, this system is for educational and research purposes only. Always consult qualified healthcare professionals for medical diagnosis.'
    },
    {
      question: 'What image formats are supported?',
      answer: 'We support PNG, JPG, and JPEG formats up to 10MB. Images should be clear kidney ultrasound or CT scans.'
    }
  ]

  return (
    <div className="space-y-8">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center"
      >
        <h1 className="text-4xl font-bold text-text-primary dark:text-white mb-4">
          Contact Us
        </h1>
        <p className="text-xl text-text-secondary dark:text-gray-400 max-w-2xl mx-auto">
          Have questions about KidneyAI Pro? We're here to help. Reach out to our team 
          for support, feedback, or collaboration opportunities.
        </p>
      </motion.div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {contactInfo.map((info, index) => {
          const Icon = info.icon
          return (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
              className="card text-center"
            >
              <div className="w-12 h-12 bg-primary/10 rounded-xl flex items-center justify-center mx-auto mb-4">
                <Icon size={24} className="text-primary" />
              </div>
              <h3 className="font-bold text-text-primary dark:text-white mb-2">
                {info.title}
              </h3>
              <p className="font-semibold text-primary mb-1">{info.value}</p>
              <p className="text-sm text-text-secondary dark:text-gray-400">
                {info.description}
              </p>
            </motion.div>
          )
        })}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.4 }}
          className="card"
        >
          <h2 className="text-2xl font-bold text-text-primary dark:text-white mb-6 flex items-center gap-2">
            <MessageCircle size={24} />
            Send us a Message
          </h2>
          
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-text-primary dark:text-white mb-2">
                  Full Name *
                </label>
                <input
                  type="text"
                  name="name"
                  value={formData.name}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 border border-border-color rounded-xl focus:ring-2 focus:ring-primary focus:border-transparent dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                  placeholder="Enter your full name"
                />
              </div>
              
              <div>
                <label className="block text-sm font-medium text-text-primary dark:text-white mb-2">
                  Email Address *
                </label>
                <input
                  type="email"
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 border border-border-color rounded-xl focus:ring-2 focus:ring-primary focus:border-transparent dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                  placeholder="Enter your email"
                />
              </div>
            </div>
            
            <div>
              <label className="block text-sm font-medium text-text-primary dark:text-white mb-2">
                Subject *
              </label>
              <select
                name="subject"
                value={formData.subject}
                onChange={handleChange}
                required
                className="w-full px-4 py-3 border border-border-color rounded-xl focus:ring-2 focus:ring-primary focus:border-transparent dark:bg-gray-700 dark:border-gray-600 dark:text-white"
              >
                <option value="">Select a subject</option>
                <option value="technical-support">Technical Support</option>
                <option value="general-inquiry">General Inquiry</option>
                <option value="collaboration">Collaboration</option>
                <option value="feedback">Feedback</option>
                <option value="other">Other</option>
              </select>
            </div>
            
            <div>
              <label className="block text-sm font-medium text-text-primary dark:text-white mb-2">
                Message *
              </label>
              <textarea
                name="message"
                value={formData.message}
                onChange={handleChange}
                required
                rows={6}
                className="w-full px-4 py-3 border border-border-color rounded-xl focus:ring-2 focus:ring-primary focus:border-transparent dark:bg-gray-700 dark:border-gray-600 dark:text-white resize-none"
                placeholder="Tell us how we can help you..."
              />
            </div>
            
            <button
              type="submit"
              disabled={isSubmitting}
              className="w-full btn-primary disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              {isSubmitting ? (
                <>
                  <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                  Sending...
                </>
              ) : (
                <>
                  <Send size={20} />
                  Send Message
                </>
              )}
            </button>
          </form>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.6 }}
          className="space-y-6"
        >
          <div className="card">
            <h2 className="text-2xl font-bold text-text-primary dark:text-white mb-6">
              Frequently Asked Questions
            </h2>
            
            <div className="space-y-4">
              {faqs.map((faq, index) => (
                <div key={index} className="border-b border-border-color dark:border-gray-700 pb-4 last:border-b-0">
                  <h3 className="font-semibold text-text-primary dark:text-white mb-2">
                    {faq.question}
                  </h3>
                  <p className="text-text-secondary dark:text-gray-400 text-sm">
                    {faq.answer}
                  </p>
                </div>
              ))}
            </div>
          </div>

          <div className="card bg-primary/5 border-primary/20">
            <div className="flex items-start gap-4">
              <Globe size={24} className="text-primary mt-1" />
              <div>
                <h3 className="text-xl font-bold text-text-primary dark:text-white mb-2">
                  Global Reach
                </h3>
                <p className="text-text-secondary dark:text-gray-400 mb-4">
                  Our AI system is being used by healthcare professionals and researchers 
                  worldwide to advance kidney stone detection and treatment.
                </p>
                <div className="grid grid-cols-2 gap-4 text-center">
                  <div>
                    <div className="text-2xl font-bold text-primary">50+</div>
                    <div className="text-sm text-text-secondary dark:text-gray-400">Countries</div>
                  </div>
                  <div>
                    <div className="text-2xl font-bold text-primary">200+</div>
                    <div className="text-sm text-text-secondary dark:text-gray-400">Hospitals</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </div>
  )
}

export default Contact
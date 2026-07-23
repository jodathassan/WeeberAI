'use client'

import { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Chat } from '@/components/chat'
import { Message } from '@/lib/types'
import { chatWithWeeber } from '@/lib/api'

function generateId() {
  return Math.random().toString(36).substring(2) + Date.now().toString(36)
}

export default function Home() {
  const [showSplash, setShowSplash] = useState(true)
  const [showChat, setShowChat] = useState(false)
  const [messages, setMessages] = useState<Message[]>([])
  const [isLoading, setIsLoading] = useState(false)

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowSplash(false)
      setShowChat(true)
    }, 2000)

    return () => clearTimeout(timer)
  }, [])

  const sendMessage = async (content: string) => {
    // Add user message
    const userMessage: Message = {
      id: generateId(),
      role: 'user',
      content,
      timestamp: new Date(),
    }

    setMessages(prev => [...prev, userMessage])
    setIsLoading(true)

    try {
      const response = await chatWithWeeber(content)

      // Add assistant message
      const assistantMessage: Message = {
        id: generateId(),
        role: 'assistant',
        content: response.answer,
        timestamp: new Date(),
        model: response.model,
        sources: response.sources,
      }

      setMessages(prev => [...prev, assistantMessage])
    } catch (error) {
      // Add error message
      const errorMessage: Message = {
        id: generateId(),
        role: 'assistant',
        content: `Failed to get recommendations. Please check your connection and try again.`,
        timestamp: new Date(),
      }
      setMessages(prev => [...prev, errorMessage])
      console.error('Error:', error)
    } finally {
      setIsLoading(false)
    }
  }

  const handleSendMessage = (message: string) => {
    sendMessage(message)
  }

  return (
    <div className="min-h-screen bg-background text-foreground overflow-hidden flex items-center justify-center">
      <AnimatePresence mode="wait">
        {showSplash && (
          <motion.div
            key="splash"
            className="fixed inset-0 flex items-center justify-center bg-background z-50"
            initial={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.5 }}
          >
            <motion.h1
              className="text-7xl md:text-8xl font-bold text-foreground"
              initial={{ scale: 0.8, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.8, opacity: 0 }}
              transition={{ duration: 0.5 }}
            >
              Weeber
            </motion.h1>
          </motion.div>
        )}

        {showChat && (
          <motion.div
            key="chat"
            className="w-full h-screen"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.5 }}
          >
            <Chat
              messages={messages}
              isLoading={isLoading}
              onSendMessage={handleSendMessage}
            />
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}

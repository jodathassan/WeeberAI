'use client'

import { motion, AnimatePresence } from 'framer-motion'
import { Message, ChatResponse } from '@/lib/types'
import { MessageBubble } from './message-bubble'
import { ChatInput } from './chat-input'
import { LoadingState } from './loading-state'
import { useEffect, useRef } from 'react'

interface ChatProps {
  messages: Message[]
  isLoading: boolean
  onSendMessage: (message: string) => void
  onLoadingMessage?: (message: string) => void
}

export function Chat({
  messages,
  isLoading,
  onSendMessage,
  onLoadingMessage,
}: ChatProps) {
  const messagesEndRef = useRef<HTMLDivElement>(null)
  const scrollContainerRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  return (
    <div className="w-full h-full flex flex-col bg-background">
      {/* Messages container */}
      <motion.div
        ref={scrollContainerRef}
        className="flex-1 overflow-y-auto space-y-4 p-4 md:p-6 max-w-4xl mx-auto w-full"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.5 }}
      >
        <AnimatePresence mode="popLayout">
          {messages.map((message, index) => (
            <motion.div
              key={message.id}
              layout
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              transition={{
                duration: 0.4,
                delay: index * 0.05,
                layout: { duration: 0.3 },
              }}
            >
              <MessageBubble message={message} />
            </motion.div>
          ))}

          {isLoading && (
            <motion.div
              key="loading"
              layout
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              transition={{ duration: 0.4 }}
            >
              <LoadingState model={onLoadingMessage ? 'Thinking...' : 'Weeber'} />
            </motion.div>
          )}
        </AnimatePresence>

        <div ref={messagesEndRef} />
      </motion.div>

      {/* Input area */}
      <motion.div
        className="border-t border-white/10 p-4 md:p-6 bg-background"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.2 }}
      >
        <div className="max-w-4xl mx-auto">
          <ChatInput
            onSendMessage={onSendMessage}
            isLoading={isLoading}
          />
        </div>
      </motion.div>
    </div>
  )
}

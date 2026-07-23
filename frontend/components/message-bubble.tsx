'use client'

import { motion } from 'framer-motion'
import { Message } from '@/lib/types'
import { getModelBadge } from '@/lib/utils'
import { AnimeCard } from './anime-card'
import ReactMarkdown from 'react-markdown'

interface MessageBubbleProps {
  message: Message
}

export function MessageBubble({ message }: MessageBubbleProps) {
  const isUser = message.role === 'user'
  const badge = message.model ? getModelBadge(message.model) : null

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} gap-3`}>
      {!isUser && (
        <motion.div
          className="w-6 h-6 rounded-full bg-primary flex items-center justify-center flex-shrink-0 mt-1 text-xs"
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ duration: 0.3 }}
        >
          <span>W</span>
        </motion.div>
      )}

      <div className={`flex flex-col gap-2 max-w-2xl ${isUser ? 'items-end' : 'items-start'}`}>
        {/* Message content */}
        <motion.div
          className={`px-4 py-3 rounded-lg transition-all ${
            isUser
              ? 'bg-primary text-background'
              : 'bg-muted text-foreground'
          }`}
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.3 }}
        >
          <div className="prose prose-invert text-sm max-w-none">
            <ReactMarkdown
              components={{
                p: ({ children }) => <p className="mb-2 last:mb-0">{children}</p>,
                strong: ({ children }) => <strong className="font-semibold text-primary">{children}</strong>,
                em: ({ children }) => <em className="italic text-accent">{children}</em>,
                code: ({ children }) => (
                  <code className="bg-primary/10 px-2 py-1 rounded text-xs font-mono text-primary">
                    {children}
                  </code>
                ),
                ul: ({ children }) => <ul className="list-disc list-inside space-y-1 mb-2">{children}</ul>,
                ol: ({ children }) => <ol className="list-decimal list-inside space-y-1 mb-2">{children}</ol>,
                li: ({ children }) => <li className="ml-2">{children}</li>,
                a: ({ href, children }) => (
                  <a
                    href={href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-primary hover:underline"
                  >
                    {children}
                  </a>
                ),
              }}
            >
              {message.content}
            </ReactMarkdown>
          </div>
        </motion.div>



        {/* Source cards */}
        {message.sources && message.sources.length > 0 && (
          <motion.div
            className="w-full space-y-3 mt-3"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.3, delay: 0.3 }}
          >
            <p className="text-xs text-muted-foreground font-semibold">
              Recommendations
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {message.sources.map((source, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.3, delay: 0.3 + index * 0.1 }}
                >
                  <AnimeCard source={source} />
                </motion.div>
              ))}
            </div>
          </motion.div>
        )}
      </div>
    </div>
  )
}

'use client'

import { motion } from 'framer-motion'

interface LoadingStateProps {
  model?: string
}

export function LoadingState({ model = 'Weeber' }: LoadingStateProps) {
  const dots = [0, 1, 2]

  return (
    <div className="flex gap-3">
      {/* Avatar */}
      <motion.div
        className="w-6 h-6 rounded-full bg-primary flex items-center justify-center flex-shrink-0 text-xs"
        animate={{ scale: [1, 1.05, 1] }}
        transition={{ duration: 1.5, repeat: Infinity }}
      >
        W
      </motion.div>

      {/* Message bubble */}
      <motion.div
        className="flex-1 max-w-2xl"
        initial={{ opacity: 0, scale: 0.8 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.3 }}
      >
        <div className="px-4 py-3 rounded-lg bg-muted inline-block">
          <div className="flex items-center gap-2">
            {/* Animated dots */}
            <div className="flex gap-1">
              {dots.map((dot) => (
                <motion.span
                  key={dot}
                  className="w-1.5 h-1.5 rounded-full bg-primary"
                  animate={{
                    scale: [1, 1.2, 1],
                    opacity: [0.4, 1, 0.4],
                  }}
                  transition={{
                    duration: 1.4,
                    repeat: Infinity,
                    delay: dot * 0.2,
                  }}
                />
              ))}
            </div>
          </div>
        </div>
      </motion.div>
    </div>
  )
}

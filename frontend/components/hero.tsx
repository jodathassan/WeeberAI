'use client'

import { motion } from 'framer-motion'
import { ArrowRight } from 'lucide-react'

interface HeroProps {
  onPromptClick: (prompt: string) => void
  isLoading: boolean
}

const examplePrompts = [
  'Cute romance anime pleease ♡',
  'Show me kawaii slice of life',
  'Best magical girl anime ~',
  'What is about My Neighbor Totoro?',
  'Recommend wholesome anime ♡',
]

export function Hero({ onPromptClick, isLoading }: HeroProps) {
  return (
    <motion.section
      className="min-h-screen flex flex-col items-center justify-center px-4 pt-20 pb-10"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.8 }}
    >
      <motion.div
        className="text-center mb-12 max-w-3xl"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.2 }}
      >
        <h1 className="text-5xl md:text-7xl font-bold mb-6 leading-tight">
          <span className="block mb-2">Find Your Favorite</span>
          <span className="bg-gradient-to-r from-primary via-accent to-pink-400 bg-clip-text text-transparent animate-[glow_3s_ease-in-out_infinite]">
            Anime ~ ♡
          </span>
        </h1>

        <p className="text-lg md:text-xl text-muted-foreground mb-8">
          Discover adorable and amazing anime recommendations powered by cute AI magic ✨
        </p>
      </motion.div>

      {/* Featured badge */}
      <motion.div
        className="mb-12 flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 border border-primary/30 backdrop-blur-sm"
        initial={{ opacity: 0, scale: 0.8 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5, delay: 0.4 }}
      >
        <span className="text-lg animate-pulse">💕</span>
        <span className="text-sm text-muted-foreground">
          Cute AI Recommendations
        </span>
      </motion.div>

      {/* Example prompts */}
      <motion.div
        className="w-full max-w-2xl space-y-3 mb-12"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.6, delay: 0.5 }}
      >
        <p className="text-xs uppercase tracking-widest text-muted-foreground text-center mb-4">
          ✨ Try these cute prompts ✨
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
          {examplePrompts.map((prompt, index) => (
            <motion.button
              key={index}
              onClick={() => onPromptClick(prompt)}
              disabled={isLoading}
              className="group relative p-4 rounded-2xl bg-gradient-to-br from-primary/10 to-accent/5 border border-primary/30 hover:border-primary/60 hover:shadow-lg hover:shadow-primary/20 transition-all duration-300 text-left hover:bg-primary/15 disabled:opacity-50 disabled:cursor-not-allowed"
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.4, delay: 0.5 + index * 0.05 }}
              whileHover={{ scale: 1.05, y: -2 }}
              whileTap={{ scale: 0.98 }}
            >
              <span className="text-sm font-medium text-foreground group-hover:text-primary transition-colors">
                {prompt}
              </span>
              <ArrowRight className="w-4 h-4 absolute right-4 top-1/2 -translate-y-1/2 opacity-0 group-hover:opacity-100 transition-opacity" />
            </motion.button>
          ))}
        </div>
      </motion.div>

      {/* Scroll indicator */}
      <motion.div
        className="mt-12"
        animate={{ y: [0, 10, 0] }}
        transition={{ duration: 2, repeat: Infinity }}
      >
        <div className="w-6 h-10 rounded-full border-2 border-primary/50 flex items-center justify-center">
          <motion.div
            className="w-1 h-2 rounded-full bg-primary"
            animate={{ y: [0, 6, 0] }}
            transition={{ duration: 2, repeat: Infinity }}
          />
        </div>
      </motion.div>
    </motion.section>
  )
}

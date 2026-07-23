'use client'

import { motion } from 'framer-motion'
import { AnimeSource } from '@/lib/types'

interface AnimeCardProps {
  source: AnimeSource
}

export function AnimeCard({ source }: AnimeCardProps) {
  const genres = source.genre.split(',').map(g => g.trim())

  return (
    <motion.div
      className="group relative overflow-hidden rounded-lg bg-card border border-white/10 hover:border-white/20"
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
      whileHover={{ y: -2 }}
    >

      <div className="relative z-10 p-4 space-y-3">
        {/* Title */}
        <div className="space-y-2">
          <h3 className="text-base font-bold text-foreground line-clamp-2 group-hover:text-primary transition-colors">
            {source.title}
          </h3>
        </div>

        {/* Genres */}
        <div className="flex flex-wrap gap-2">
          {genres.slice(0, 3).map((genre, index) => (
            <span
              key={index}
              className="text-xs px-2 py-1 rounded bg-white/10 text-muted-foreground"
            >
              {genre}
            </span>
          ))}
        </div>
      </div>
    </motion.div>
  )
}

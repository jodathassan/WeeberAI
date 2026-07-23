'use client'

import { motion } from 'framer-motion'
import React, { useMemo } from 'react'

export function AnimatedBackground() {
  const particles = useMemo(() => 
    Array.from({ length: 20 }).map((_, i) => ({
      id: i,
      left: Math.random() * 100,
      delay: Math.random() * 5,
      duration: 15 + Math.random() * 10,
      size: 2 + Math.random() * 4,
    })), []
  )

  return (
    <div className="fixed inset-0 overflow-hidden pointer-events-none">
      {/* Aurora effect */}
      <motion.div
        className="absolute inset-0"
        animate={{
          background: [
            'radial-gradient(at 20% 30%, rgba(255, 105, 180, 0.2) 0px, transparent 50%)',
            'radial-gradient(at 80% 70%, rgba(157, 109, 217, 0.2) 0px, transparent 50%)',
            'radial-gradient(at 40% 60%, rgba(255, 166, 214, 0.15) 0px, transparent 50%)',
            'radial-gradient(at 20% 30%, rgba(255, 105, 180, 0.2) 0px, transparent 50%)',
          ],
        }}
        transition={{
          duration: 15,
          repeat: Infinity,
          repeatType: 'loop',
        }}
      />

      {/* Floating particles */}
      {particles.map((particle) => (
        <motion.div
          key={particle.id}
          className="absolute rounded-full bg-gradient-to-r from-primary to-accent opacity-20 blur-sm"
          style={{
            width: particle.size,
            height: particle.size,
            left: `${particle.left}%`,
            bottom: '-10%',
          }}
          animate={{
            y: [-20, -800],
            opacity: [0, 0.4, 0],
          }}
          transition={{
            duration: particle.duration,
            delay: particle.delay,
            repeat: Infinity,
            repeatType: 'loop',
            ease: 'linear',
          }}
        />
      ))}

      {/* Grid effect */}
      <div className="absolute inset-0 bg-grid opacity-5" />
    </div>
  )
}

// CSS for grid pattern
const gridStyle = `
  background-image: 
    linear-gradient(rgba(139, 92, 246, 0.1) 1px, transparent 1px),
    linear-gradient(90deg, rgba(139, 92, 246, 0.1) 1px, transparent 1px);
  background-size: 50px 50px;
`

export function BackgroundGrid() {
  return <div className="fixed inset-0 pointer-events-none opacity-10" style={{ backgroundImage: 'url("data:image/svg+xml,%3Csvg width=\'50\' height=\'50\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cpath d=\'M0 0h50v50H0z\' fill=\'none\'/%3E%3Cpath d=\'M0 0h50M0 50v-50M50 0v50M50 50h-50\' stroke=\'rgba(139,92,246,0.1)\' stroke-width=\'1\'/%3E%3C/svg%3E")' }} />
}

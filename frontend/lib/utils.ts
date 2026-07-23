import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function getModelBadge(model: string): { icon: string; color: string } {
  const badges: Record<string, { icon: string; color: string }> = {
    Gemini: { icon: '✨', color: 'text-blue-400' },
    'Claude': { icon: '🧠', color: 'text-purple-400' },
    'Ollama': { icon: '⚙️', color: 'text-amber-400' },
    'GPT': { icon: '🤖', color: 'text-green-400' },
  }
  return badges[model] || { icon: '🔮', color: 'text-cyan-400' }
}

export function formatScore(score: number): string {
  return score.toFixed(2)
}

export function formatSimilarity(similarity: number): string {
  return `${(similarity * 100).toFixed(0)}%`
}

export function scrollToBottom(elementId: string) {
  const element = document.getElementById(elementId)
  if (element) {
    setTimeout(() => {
      element.scrollTop = element.scrollHeight
    }, 0)
  }
}

export function debounce<T extends (...args: any[]) => any>(
  func: T,
  wait: number
): (...args: Parameters<T>) => void {
  let timeout: NodeJS.Timeout
  return (...args: Parameters<T>) => {
    clearTimeout(timeout)
    timeout = setTimeout(() => func(...args), wait)
  }
}

export const examplePrompts = [
  'Recommend anime like Attack on Titan',
  'Best psychological thriller anime',
  'Recommend romance anime under 24 episodes',
  'What is Naruto about?',
  'Recommend dark fantasy anime',
]

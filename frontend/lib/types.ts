export interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  timestamp: Date
  model?: string
  sources?: AnimeSource[]
}

export interface AnimeSource {
  title: string
  genre: string
  score: number
  similarity: number
}

export interface ChatResponse {
  intent: string
  model: string
  answer: string
  sources: AnimeSource[]
}

export interface StreamMessage {
  type: 'text' | 'source' | 'complete' | 'error'
  content?: string
  source?: AnimeSource
  model?: string
  error?: string
}

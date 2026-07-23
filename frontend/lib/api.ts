import { ChatResponse, StreamMessage } from './types'

// Clean up raw environment variable or fallback string
let rawUrl = process.env.NEXT_PUBLIC_API_URL || 'https://weeberai-production.up.railway.app'

// Remove duplicate "https://" or "http://" prefixes if present
rawUrl = rawUrl.replace(/^(https?:\/\/)+/i, '')

// Set clean API URL with a single https:// and no trailing slashes
const API_URL = `https://${rawUrl.replace(/\/$/, '')}`

export async function chatWithWeeber(query: string): Promise<ChatResponse> {
  try {
    const response = await fetch(`${API_URL}/recommend`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query }),
    })

    if (!response.ok) {
      throw new Error(`API error: ${response.statusText}`)
    }

    const data = await response.json()
    return data
  } catch (error) {
    console.error('Chat error:', error)
    throw error
  }
}

export async function* streamChat(query: string): AsyncGenerator<StreamMessage> {
  try {
    const response = await fetch(`${API_URL}/recommend`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query }),
    })

    if (!response.ok) {
      throw new Error(`API error: ${response.statusText}`)
    }

    const data = await response.json()

    if (data.answer) {
      yield {
        type: 'text',
        content: data.answer,
        model: data.model,
      }
    }

    if (data.sources && data.sources.length > 0) {
      for (const source of data.sources) {
        yield {
          type: 'source',
          source,
        }
      }
    }

    yield {
      type: 'complete',
      model: data.model,
    }
  } catch (error) {
    console.error('Stream error:', error)
    yield {
      type: 'error',
      error: error instanceof Error ? error.message : 'Unknown error',
    }
  }
}
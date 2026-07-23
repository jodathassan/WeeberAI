import { ChatResponse, StreamMessage } from './types'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

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

    // Simulate streaming the response
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

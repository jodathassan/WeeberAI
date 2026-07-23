import { ChatResponse, StreamMessage } from './types'

// Hardcode direct Railway endpoint to remove all Vercel variable issues
const API_URL = 'https://weeberai-production.up.railway.app'

export async function chatWithWeeber(query: string): Promise<ChatResponse> {
  console.log('--- WEEBER API DEBUG ---')
  console.log('Sending request to:', `${API_URL}/recommend`)
  console.log('Payload:', { query })

  try {
    const response = await fetch(`${API_URL}/recommend`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query }),
    })

    console.log('Response Status:', response.status, response.statusText)

    if (!response.ok) {
      const errorText = await response.text()
      console.error('Server returned error body:', errorText)
      throw new Error(`API error (${response.status}): ${response.statusText}`)
    }

    const data = await response.json()
    console.log('Response Data:', data)
    return data
  } catch (error) {
    console.error('Fetch caught error:', error)
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
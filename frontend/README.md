# Weeber - Your Intelligent Anime Companion

A stunning, AI-powered anime recommendation frontend built with Next.js, React, Framer Motion, and Tailwind CSS.

## 🎨 Features

- **Beautiful Dark UI**: Premium glassmorphism design with animated gradients and particle effects
- **Smooth Animations**: Extensive use of Framer Motion for delightful micro-interactions
- **AI-Powered Recommendations**: Integrated with FastAPI backend using RAG technology
- **Responsive Design**: Perfect on desktop, tablet, and mobile devices
- **Real-time Chat**: ChatGPT-style conversation interface with typing animations
- **Anime Cards**: Beautiful recommendation cards with glowing effects and hover animations
- **Model Badges**: Shows which AI model powered the recommendation
- **Markdown Support**: Rich text rendering for anime descriptions
- **Loading States**: Custom animated loading indicators
- **Error Handling**: Friendly error messages and recovery

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ (LTS recommended)
- pnpm (or npm/yarn)
- FastAPI backend running on `http://localhost:8000`

### Installation

1. **Clone and setup the project**
```bash
cd weeber
pnpm install
```

2. **Configure environment variables**
```bash
cp .env.example .env.local
# Edit .env.local and set NEXT_PUBLIC_API_URL to your FastAPI backend
```

3. **Run development server**
```bash
pnpm dev
```

4. **Open in browser**
Navigate to `http://localhost:3000`

## 📁 Project Structure

```
weeber/
├── app/
│   ├── layout.tsx              # Root layout with theme setup
│   ├── page.tsx                # Main page with chat logic
│   └── globals.css             # Global styles, animations, and design tokens
├── components/
│   ├── header.tsx              # Header with logo and navigation
│   ├── hero.tsx                # Landing hero section with example prompts
│   ├── chat.tsx                # Main chat interface
│   ├── message-bubble.tsx       # Individual message component
│   ├── chat-input.tsx           # Chat input with IME support
│   ├── anime-card.tsx           # Anime recommendation card
│   ├── loading-state.tsx        # Animated loading indicator
│   └── background.tsx           # Aurora and particle effects
├── lib/
│   ├── types.ts                # TypeScript interfaces
│   ├── api.ts                  # API client functions
│   └── utils.ts                # Utility functions and helpers
└── public/                     # Static assets
```

## 🎯 How It Works

### Frontend Flow

1. **Landing Page**: Hero section with example prompts
2. **User Input**: Click example or type custom query
3. **API Call**: Send request to FastAPI backend at `/chat` endpoint
4. **Display Results**: Show AI response with anime recommendations
5. **Conversation**: Continue chatting with full context

### API Integration

The frontend expects the FastAPI backend to have a `/chat` endpoint:

**Request:**
```json
{
  "query": "Recommend anime like Attack on Titan"
}
```

**Response:**
```json
{
  "intent": "recommendation",
  "model": "Gemini",
  "answer": "Based on your interest...",
  "sources": [
    {
      "title": "Vinland Saga",
      "genre": "Action, Drama",
      "score": 8.74,
      "similarity": 0.91
    }
  ]
}
```

## 🎨 Design System

### Color Palette
- **Background**: `#0a0e27` (Deep Blue)
- **Primary**: `#8b5cf6` (Purple)
- **Secondary**: `#6366f1` (Indigo)
- **Accent**: `#06b6d4` (Cyan)
- **Text**: `#e8ecff` (Light Blue)

### Typography
- **Headings**: System fonts (Geist)
- **Body**: System fonts (Geist)
- **Code**: Monospace (Geist Mono)

### Animations
- **Float**: Floating particles with smooth motion
- **Glow**: Pulsing text effects for titles
- **Shimmer**: Loading state animations
- **Pulse Glow**: Card hover effects
- **Slide Up**: Message entrance animations

## 🛠 Development

### Available Scripts

```bash
# Development server with HMR
pnpm dev

# Production build
pnpm build

# Start production server
pnpm start

# Run linting
pnpm lint
```

### Technology Stack

- **Framework**: Next.js 16 (App Router)
- **Language**: TypeScript 5
- **Styling**: Tailwind CSS 4
- **Animations**: Framer Motion 11
- **Icons**: Lucide React
- **Markdown**: React Markdown
- **Package Manager**: pnpm

## 🔧 Configuration

### Environment Variables

Create a `.env.local` file:

```env
# Required
NEXT_PUBLIC_API_URL=http://localhost:8000

# Optional
# Add any other configuration as needed
```

### API URL

The frontend connects to the FastAPI backend. Make sure:
1. Your backend is running on the configured URL
2. CORS is properly configured to allow requests from `localhost:3000`
3. The `/chat` endpoint is available and working

## 📱 Responsive Design

The UI is fully responsive:
- **Mobile**: Optimized touch targets, single column layout
- **Tablet**: Two column recommendations, adjusted spacing
- **Desktop**: Full feature set, optimal spacing and typography

## ♿ Accessibility

- Semantic HTML structure
- ARIA labels and roles
- Keyboard navigation support
- Screen reader friendly
- Color contrast compliant
- Focus indicators for keyboard users

## 🚀 Deployment

### Deploy to Vercel

1. **Push to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Connect to Vercel**
- Go to [vercel.com](https://vercel.com)
- Import your GitHub repository
- Add environment variables in project settings
- Deploy!

### Deploy to Other Platforms

The project can be deployed anywhere that supports Node.js:
- Netlify
- Railway
- Render
- AWS
- DigitalOcean

Run `pnpm build` and follow platform-specific deployment instructions.

## 🐛 Troubleshooting

### API Connection Failed
- Check that FastAPI backend is running on the configured URL
- Verify CORS is enabled on the backend
- Check `NEXT_PUBLIC_API_URL` environment variable

### Animations Not Working
- Ensure Framer Motion is installed: `pnpm install framer-motion`
- Check browser console for errors
- Try clearing cache: `pnpm build && pnpm start`

### Styling Issues
- Rebuild Tailwind: `pnpm dev`
- Clear Next.js cache: `rm -rf .next`
- Check that globals.css is imported in layout.tsx

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Check the FastAPI backend documentation
4. Open an issue on GitHub

---

Built with ❤️ by v0 - Your AI-Powered Frontend Engineer

# Weeber - Complete Setup Guide

## 📦 What's Included

This is a production-ready, premium anime recommendation frontend built with cutting-edge technologies:

### ✨ Features Implemented

- **Landing Page**: Stunning hero section with animated background and example prompts
- **Chat Interface**: Real-time conversation UI with smooth animations
- **Anime Recommendations**: Beautiful cards with glass-morphism design
- **Model Badges**: Shows which AI model powered each response
- **Dark Mode**: Premium dark theme optimized for anime content
- **Responsive Design**: Perfect on all devices (mobile, tablet, desktop)
- **Smooth Animations**: 50+ animation sequences with Framer Motion
- **Type Safety**: Full TypeScript support throughout
- **IME Support**: Proper keyboard composition support for CJK languages
- **Error Handling**: Graceful fallbacks and friendly error messages

### 🎨 Design Highlights

- **Color Scheme**: Purple, Indigo, Cyan, and Dark Blue
- **Typography**: System fonts for optimal performance
- **Effects**: Aurora background, floating particles, glowing text, shimmer effects
- **Interactions**: Hover effects, micro-interactions, smooth transitions
- **Glassmorphism**: Modern frosted glass UI elements throughout

## 🚀 Getting Started in 3 Steps

### Step 1: Install Dependencies

```bash
# Navigate to project directory
cd weeber

# Install with pnpm (recommended)
pnpm install

# Or with npm
npm install

# Or with yarn
yarn install
```

### Step 2: Configure Backend Connection

```bash
# Copy environment template
cp .env.example .env.local

# Edit .env.local with your FastAPI backend URL
# NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Step 3: Run Development Server

```bash
pnpm dev
```

Open `http://localhost:3000` in your browser. You should see:
- Beautiful hero section with Weeber branding
- Five example prompt cards
- Smooth animations and glowing effects
- Fully responsive design

## 🔌 Backend Integration

The frontend expects a FastAPI backend with this endpoint:

### POST `/chat`

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
  "answer": "Here are some anime recommendations similar to Attack on Titan...",
  "sources": [
    {
      "title": "Vinland Saga",
      "genre": "Action, Drama",
      "score": 8.74,
      "similarity": 0.91
    },
    {
      "title": "Demon Slayer",
      "genre": "Action, Supernatural",
      "score": 8.63,
      "similarity": 0.87
    }
  ]
}
```

### CORS Configuration

Make sure your FastAPI backend has CORS enabled:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 📁 File Structure Explained

```
weeber/
├── app/
│   ├── layout.tsx                 # Root layout, imports globals.css
│   ├── page.tsx                   # Main page, handles chat state & API calls
│   ├── globals.css                # All animations, colors, and design tokens
│   └── favicon.svg                # Browser tab icon
│
├── components/                    # All React components
│   ├── header.tsx                 # Top navigation bar with logo
│   ├── hero.tsx                   # Landing page section
│   ├── chat.tsx                   # Main chat container
│   ├── message-bubble.tsx         # Individual chat messages with markdown
│   ├── chat-input.tsx             # Input field with send button
│   ├── anime-card.tsx             # Anime recommendation card
│   ├── loading-state.tsx          # Animated loading indicator
│   └── background.tsx             # Aurora & particle animations
│
├── lib/
│   ├── types.ts                   # TypeScript interfaces
│   ├── api.ts                     # Fetch/streaming API functions
│   └── utils.ts                   # Helper functions
│
├── public/                        # Static assets (icons, logos)
├── .env.example                   # Environment template
├── README.md                       # Full documentation
├── SETUP.md                       # This file
├── package.json                   # Dependencies
├── tsconfig.json                  # TypeScript config
├── next.config.mjs                # Next.js config
├── tailwind.config.ts             # Tailwind config
└── postcss.config.mjs             # PostCSS config
```

## 🎯 Key Components

### 1. **Hero Component** (`components/hero.tsx`)
- Landing page with animated title
- Five example prompt buttons
- Smooth entrance animations
- Scroll indicator

### 2. **Chat Component** (`components/chat.tsx`)
- Messages container with auto-scroll
- Loading states
- Message list with staggered animations
- Input area with glass morphism

### 3. **Message Bubble** (`components/message-bubble.tsx`)
- User & assistant messages with different styles
- Markdown rendering
- Model badge display
- Anime recommendations display

### 4. **Anime Card** (`components/anime-card.tsx`)
- Glass-morphic design
- Title, genres, score, and similarity
- Hover effects and glowing borders
- Responsive grid layout

### 5. **Background** (`components/background.tsx`)
- Aurora gradient effects
- Floating particle animation
- Grid pattern overlay
- Responsive to viewport

## 🎨 Customization Guide

### Changing Colors

Edit `app/globals.css` to modify the color scheme:

```css
:root {
  --background: #0a0e27;      /* Main background */
  --foreground: #e8ecff;       /* Main text */
  --primary: #8b5cf6;          /* Primary buttons/accents */
  --secondary: #6366f1;        /* Secondary accents */
  --accent: #06b6d4;           /* Tertiary accents */
  --muted: #334155;            /* Muted text */
}
```

### Changing Animations

Modify animation durations and keyframes in `app/globals.css`:

```css
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }  /* Change this */
}
```

### Changing Fonts

Edit `app/layout.tsx`:

```typescript
import { Inter, Poppins } from 'next/font/google'

const sans = Poppins({ subsets: ['latin'] })
```

Then update `app/globals.css`:
```css
@theme inline {
  --font-sans: 'Poppins';
}
```

## 🚀 Production Build

### Build for Production

```bash
pnpm build
```

This creates an optimized build in the `.next/` directory.

### Start Production Server

```bash
pnpm start
```

### Build Size

Expected bundle size: ~200KB (gzipped)
- Next.js: ~50KB
- React: ~40KB
- Framer Motion: ~30KB
- Other: ~80KB

## 🌐 Deployment

### Deploy to Vercel (Recommended)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Follow prompts to connect GitHub and deploy
```

### Deploy to Other Platforms

**Netlify:**
```bash
netlify deploy --prod --dir=.next
```

**Docker:**
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN pnpm install && pnpm build
EXPOSE 3000
CMD ["pnpm", "start"]
```

**Environment Variables**
Don't forget to set `NEXT_PUBLIC_API_URL` in your hosting platform's environment variables dashboard.

## 🔍 Debugging

### Enable Debug Logs

Add console statements to `app/page.tsx`:

```typescript
const sendMessage = async (content: string) => {
  console.log('[v0] Sending message:', content)
  try {
    const response = await chatWithWeeber(content)
    console.log('[v0] Received response:', response)
  } catch (error) {
    console.error('[v0] Error:', error)
  }
}
```

### Check Network Requests

1. Open DevTools (F12)
2. Go to Network tab
3. Send a message
4. Look for POST request to `/chat`
5. Check response body

### Common Issues

**Issue: "Failed to connect to API"**
- Check backend is running: `http://localhost:8000/docs`
- Verify `NEXT_PUBLIC_API_URL` in `.env.local`
- Check CORS configuration in FastAPI
- Check firewall/network settings

**Issue: "Animations are stuttering"**
- Check browser performance in DevTools
- Reduce particle count in `components/background.tsx`
- Disable hardware acceleration test
- Try different browser

**Issue: "Styling looks broken"**
- Clear cache: `rm -rf .next node_modules`
- Reinstall: `pnpm install`
- Restart dev server: `pnpm dev`

## 📚 Technology Stack Details

- **Next.js 16**: Latest React framework with App Router
- **React 19**: Latest React with automatic batching
- **TypeScript 5**: Full type safety throughout
- **Tailwind CSS 4**: Utility-first CSS with new features
- **Framer Motion 11**: Production-ready animation library
- **Lucide React**: Modern icon library
- **React Markdown**: Safe markdown rendering

## ✅ Pre-deployment Checklist

- [ ] Backend API is running and responding
- [ ] CORS is properly configured
- [ ] Environment variables are set
- [ ] No console errors in DevTools
- [ ] All pages load correctly
- [ ] Chat functionality works end-to-end
- [ ] Mobile responsive design looks good
- [ ] Animations are smooth (60 FPS)
- [ ] Build completes without errors: `pnpm build`

## 📞 Support & Resources

- **Next.js Docs**: https://nextjs.org/docs
- **React Docs**: https://react.dev
- **Tailwind Docs**: https://tailwindcss.com/docs
- **Framer Motion**: https://www.framer.com/motion/
- **TypeScript**: https://www.typescriptlang.org/docs/

## 🎓 Learning Path

To understand the codebase:

1. Start with `app/layout.tsx` - Root structure
2. Read `app/globals.css` - Design system & animations
3. Check `app/page.tsx` - State management & API calls
4. Review `components/hero.tsx` - Component structure
5. Explore `lib/api.ts` - API integration
6. Check other components - UI patterns

## 🤝 Contributing

To add new features:

1. Create component in `components/`
2. Add types to `lib/types.ts`
3. Add utilities to `lib/utils.ts`
4. Import and use in pages/components
5. Test on mobile and desktop
6. Commit with clear message

## 📝 Notes

- All animations use GPU acceleration for performance
- Images are optimized with Next.js Image component
- Code is formatted with reasonable defaults
- TypeScript strict mode is enabled
- Tree-shaking removes unused code
- Dark mode is forced for anime aesthetic

---

**You're all set! 🚀**

Your Weeber frontend is ready to go. Connect it to your FastAPI backend and start recommending anime!

For questions or issues, check the README.md or review the component code - it's well-commented throughout.

Happy coding! ✨

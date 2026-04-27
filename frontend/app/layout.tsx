import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
  display: 'swap',
})

export const metadata: Metadata = {
  title: 'Plant Disease Detector — Local AI Diagnosis',
  description:
    'Identify plant diseases instantly on your local machine using an optimised TFLite MobileNet model. No internet required. Designed for 16GB RAM systems.',
  keywords: ['plant disease', 'agriculture', 'AI', 'machine learning', 'local inference', 'TFLite'],
  authors: [{ name: 'Plant Disease Detector' }],
  openGraph: {
    title: 'Plant Disease Detector',
    description: 'Fast, local, private plant disease detection powered by optimised AI.',
    type: 'website',
  },
  robots: { index: true, follow: true },
  viewport: 'width=device-width, initial-scale=1',
  themeColor: '#22c55e',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={inter.variable}>
      <body className="min-h-screen bg-gradient-to-br from-slate-50 via-green-50/30 to-sky-50/20">
        {children}
      </body>
    </html>
  )
}

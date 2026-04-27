import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  output: 'standalone',
  images: {
    formats: ['image/avif', 'image/webp'],
  },
  async rewrites() {
    return [
      {
        source: '/api/predict',
        destination: `${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/predict`,
      },
      {
        source: '/api/health',
        destination: `${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/health`,
      },
    ]
  },
}

export default nextConfig

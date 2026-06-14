import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

const frontendHost = process.env.FRONTEND_HOST ?? '127.0.0.1'
const frontendPort = Number(process.env.FRONTEND_PORT ?? 5173)
const backendHost = process.env.APP_HOST ?? '127.0.0.1'
const backendPort = Number(process.env.APP_PORT ?? 8787)
const backendTarget = `http://${backendHost}:${backendPort}`

export default defineConfig({
  plugins: [react()],
  server: {
    port: frontendPort,
    host: frontendHost,
    proxy: {
      '/api': {
        target: backendTarget,
        changeOrigin: true,
      },
      '/interactive-visualizations': {
        target: backendTarget,
        changeOrigin: true,
      },
    },
  },
})

import path from "path";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    port: 5173,
    proxy: {
      // proxy /api to FastAPI during dev if VITE_API_BASE_URL is relative
      // "/api": { target: "http://localhost:8000", changeOrigin: true },
    },
  },
});

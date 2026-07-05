import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

// https://astro.build/config
export default defineConfig({
  // Konfigurasi untuk GitHub Pages
  // Pastikan nama repository di GitHub = "ninja-urban-farming" agar sesuai dengan base path ini
  site: 'https://satyaadiditech.github.io',
  base: '/ninja-urban-farming',
  
  integrations: [mdx()],
  
  // Output static untuk GitHub Pages
  output: 'static',
  
  // Markdown config
  markdown: {
    shikiConfig: {
      theme: 'github-dark',
      wrap: true
    }
  }
});

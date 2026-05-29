import { readdirSync, statSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, relative, resolve } from 'node:path';
import { defineConfig } from 'vite';

const projectDir = dirname(fileURLToPath(import.meta.url));

function collectHtmlInputs(dir, inputs = {}) {
  for (const entry of readdirSync(dir)) {
    if (entry === 'node_modules' || entry === 'dist') continue;
    const fullPath = resolve(dir, entry);
    const stats = statSync(fullPath);
    if (stats.isDirectory()) {
      collectHtmlInputs(fullPath, inputs);
    } else if (entry.endsWith('.html')) {
      const key = relative(projectDir, fullPath).replace(/\/index\.html$/, '').replace(/\.html$/, '') || 'main';
      inputs[key.replace(/[^a-zA-Z0-9_]/g, '_')] = fullPath;
    }
  }
  return inputs;
}

export default defineConfig({
  build: {
    rollupOptions: {
      input: collectHtmlInputs(projectDir),
    },
  },
});

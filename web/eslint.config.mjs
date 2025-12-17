// eslint.config.mjs

import { defineConfig } from 'eslint-define-config';
import nextVitals from 'eslint-config-next/core-web-vitals';
import nextTs from 'eslint-config-next/typescript';

export default defineConfig({
  extends: [
    ...nextVitals,
    ...nextTs,
  ],
  ignorePatterns: [
    ".next/**",
    "out/**",
    "build/**",
    "next-env.d.ts",
  ],
  rules: {
    'react/react-in-jsx-scope': 'off',
    '@typescript-eslint/explicit-module-boundary-types': 'on',
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
  plugins: [
    'prettier',
  ],
});

import globals from 'globals';
import pluginJs from '@eslint/js';

export default [
  {
    languageOptions: { globals: { ...globals.browser, ...globals.node } },
    env: {
      es6: true,
    },
    extends: 'airbnb',
    parserOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
    },
    rule: {
      'no-unused-vars': 'error',
      'no-undef': 'error',
      'semi': 'error',
      'prefer-const': 'error',
    },
  },
  pluginJs.configs.recommended,
];

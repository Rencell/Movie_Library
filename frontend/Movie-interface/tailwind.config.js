/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html', 
    './src/**/*.{vue,js,ts,jsx,tsx}',
    "./node_modules/flowbite/**/*.js"
  ],
  darkMode: true,
  theme: {
    extend: {},
  },
  theme: {
    extend: {},
  },
  plugins: [

    require('flowbite/plugin')
  ],
}


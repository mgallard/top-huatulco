/** @type {import('tailwindcss').Config} */
export default {
  content: ['./**/*.html', './src/**/*.js', '!./dist/**', '!./node_modules/**'],
  theme: {
    extend: {
      colors: {
        background: '#FBFCFC',
        ink: '#182B36',
        surface: '#F3F8FA',
        secondary: '#EEF6F8',
        border: '#DCE9ED',
        primary: '#2C9AB7',
        ocean: '#182B36',
        coral: '#F47A45',
        sand: '#FFF7ED',
        maize: '#FBBF24',
        cloud: '#F8FAFC',
        charcoal: '#1F2937',
        mist: '#E5E7EB',
        volcano: '#2D6A4F',
        pacific: '#2C9AB7',
      },
      fontFamily: {
        heading: ['Poppins', 'Inter', 'system-ui', 'sans-serif'],
        body: ['Inter', 'system-ui', 'sans-serif'],
        script: ['Kalam', 'Inter', 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        soft: '0 10px 40px -12px rgba(44, 154, 183, 0.28)',
        card: '0 8px 30px -10px rgba(24, 43, 54, 0.18)',
      },
    },
  },
  plugins: [],
};

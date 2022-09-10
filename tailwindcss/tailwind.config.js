/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../templates/ba_code.html",
          "../templates/base.html",
        "../templates/contact.html",
      "../templates/projects.html",
    "../templates/studies.html"],
  theme: {
    fontFamily: {
      sans: ['Michroma', 'sans-serif']
    },
    extend: {
      backgroundImage:{
        'berlin': "url('../static/images/berlin_bg_crop_2.jpg')",
      },
      
      colors: {
        pmint:{
          50: '#F5FBF7',
          100: '#EBF8F0',
          200: '#E1F4E8',
          300: '#D7F1E1',
          400: '#CDEDD9',
          500: '#C2E9D1',
          600: '#B8E6CA',
          700: '#AEE2C2',
          800: '#95C9A9',
          900: '#92C0A4',
        },
        shirt:{
          20: '#e0bfff',
          50: '#ad58ff',
          100: '#a052ec',
          200: '#934bd9',
          300: '#8745c6',
          400: '#7a3eb3',
          500: '#6d38a1',
          600: '#60318e',
          700: '#542b7b',
          800: '#472468',
          900: '#3a1e55',
        },
      }
    },
  },
  plugins: [],
}

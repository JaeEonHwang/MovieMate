import { createApp } from 'vue'
import { createVuetify } from 'vuetify'

export default createVuetify({
  theme: {
    defaultTheme: 'myCustomTheme',
    themes: {
      // 토글 버튼은 default dark(#000000)이 아닌 Material Design 권장 사항인 #121212로 변경
      myCustomTheme: {
        dark: false,
        colors: '#121212',
      },
    },
  },
})
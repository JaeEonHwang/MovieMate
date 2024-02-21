import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import App from './App.vue'
import router from './router'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import '@fortawesome/fontawesome-free/css/all.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})



const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)

// app.use(createPinia())
app.use(pinia)
app.use(router)
// app.use(Vuetify)

// const vuetify = new Vuetify({
//   theme: {
//     themes: {
//       light: {
//         primary: '#A44CD3', // Medium Orchid
//         secondary: '#E090DF', // Plum
//         accent: '#FBBEDE', // Lavender Pink
//       },
//     },
//   },
// });

// app.use(vuetify)

// app.mount('#app')
app.use(vuetify).mount('#app')

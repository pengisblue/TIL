import PiniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

const app = createApp(App)
const pinia = createPinia()

pinia.use(PiniaPluginPersistedstate)

app.use(pinia)
// app.use(createPinia())

app.mount('#app')

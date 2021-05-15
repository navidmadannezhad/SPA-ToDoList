import Vue from 'vue'
import App from './App.vue'
import { router } from './router/router.js'
import { store } from './vuex/store.js'

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')

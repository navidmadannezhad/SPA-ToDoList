import Vue from 'vue'
import App from './App.vue'
import { router } from './router/router.js'
import { store } from './vuex/store.js'
import { getCookie } from './csrf.js'
import axios from 'axios'

Vue.config.productionTip = false

let user = window.localStorage.getItem('user');

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
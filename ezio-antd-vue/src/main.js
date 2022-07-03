import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// mock
// WARNING: `mockjs` NOT SUPPORT `IE` PLEASE DO NOT USE IN `production` ENV.
import './mock'

import './core/use' // use lazy load components
import './permission' // permission control
import './utils/filter' // base filter
// import Print from 'vue-print-nb-jeecg'
import './global.sass' // global style

// 表单验证
import { rules } from '@/utils/rules'
Vue.prototype.rules = rules
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: (h) => h(App)
}).$mount('#app')

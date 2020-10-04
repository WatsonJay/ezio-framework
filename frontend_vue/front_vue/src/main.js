import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import 'normalize.css/normalize.css' // a modern alternative to CSS resets
//集成iconfont图标
import "@/icons/iconfonts/iconfont.js";
import "@/icons/iconfonts/iconfont.css";
import "./icons/index"
//全局scss
import "./styles/index.scss";
//vue-i18n 多语言版本处理
import i18n from "./lang";
//全局校验规则
import validate from "./utils/validate.js";
//axios
import "./utils/axios.js";

Vue.config.productionTip = false;

if (process.env.NODE_ENV === 'development') {
  const { mockXHR } = require('../mock')
  mockXHR()
}

Vue.use(ElementUI);
Vue.use({
  //size: Cookies.get('size') || 'medium', // set element-ui default size
  i18n: (key, value) => i18n.t(key, value)
});
Vue.use(validate);

new Vue({
  router,
  store,
  i18n,
  render: h => h(App)
}).$mount("#app");

import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
//element-ui
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
//集成iconfont图标
import "@/icons/iconfonts/iconfont.css";
//全局scss
import "./styles/main.scss";
//vue-i18n 多语言版本处理
import i18n from "./lang";
//全局校验规则
import validate from "./util/validate.js";
//axios
import "./util/axios.js";

Vue.config.productionTip = false;

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

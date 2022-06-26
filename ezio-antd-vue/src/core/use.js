import Vue from "vue";

// base library
import Antd, { version } from "ant-design-vue";
console.log("ant-design-vue version:", version);
import "ant-design-vue/dist/antd.css"; // or 'ant-design-vue/dist/antd.less'

Vue.use(Antd);

process.env.NODE_ENV !== "production" &&
  console.warn("[antd-pro] WARNING: Antd now use fulled imported.");

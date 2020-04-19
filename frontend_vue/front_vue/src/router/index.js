import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

//所有权限通用路由表
//如首页和登录页和一些不用权限的公用页面
export const constantRouterMap = [
  {
    path: "/login",
    name: "login",
    component: () => import("@/views/auth/login"),
    hidden: true
  },
  {
    path: "/register",
    name: "register",
    component: () => import("@/views/auth/register"),
    hidden: true
  },
  {
    path: "/404",
    name: "404",
    component: () => import("@/views/error-page/404"),
    hidden: true
  },
  {
    path: "/403",
    name: "403",
    component: () => import("@/views/error-page/403"),
    hidden: true
  }
];

//动态页面通过后台传至前端

const router = new VueRouter({
  mode: "history",
  routes: constantRouterMap
});

export default router;

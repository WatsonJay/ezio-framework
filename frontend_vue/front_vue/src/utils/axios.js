import axios from "axios";
import { Loading, Message } from "element-ui";
import store from "../store";

let loading; //Loading 实例

axios.defaults.timeout = 5000; //响应时间
axios.defaults.headers.post["Content-Type"] = "application/json;charset=UTF-8"; //配置请求头

//添加请求拦截器
axios.interceptors.request.use(
  config => {
    //在发送请求之前做某件事
    if (
      config.method === "post" &&
      config.headers["Content-Type"] !== "multipart/form-data"
    ) {
      debugger;
      config.data = JSON.stringify(config.data);
    }
    const token = store.getters.user.token;
    token && (config.headers.Authorization = token);
    return config;
  },
  error => {
    console.log("错误的传参");
    return Promise.reject(error);
  }
);

//错误信息参数
const errMsgOpts = { type: "error", duration: 3000, showClose: true };

//返回状态判断(添加响应拦截器)
axios.interceptors.response.use(
  res => {
    if (res.data != null && res.data.success == false) {
      Message.error({
        message: res.data.message,
        ...errMsgOpts
      });
    }
    return res;
  },
  error => {
    Message.error({
      message: "系统出现错误",
      ...errMsgOpts
    });
    return Promise.reject(error);
  }
);

let waitingRequestCount = 0; //等待的请求数

//全局loading启用
export function showFullScreenLoading() {
  if (waitingRequestCount === 0) {
    loading = Loading.service({
      lock: true,
      text: "加载中……",
      background: "rgba(0, 0, 0, 0.7)"
    });
  }
  waitingRequestCount++;
}

//全局loading停用
export function hideFullScreenLoading() {
  if (waitingRequestCount <= 0) return;
  waitingRequestCount--;
  if (waitingRequestCount === 0) {
    loading.close();
  }
}

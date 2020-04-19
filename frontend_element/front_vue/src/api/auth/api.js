import axios from "axios";
import { base } from "@/api/config.js";

/*
  quanxian相关接口
 */
//用户注册API
export const addOrUpadteUserUrl = params => {
  return axios({
    method: "post",
    url: `${base}/user/addOrUpadteUser`,
    data: params,
    headers: {
      "Content-Type": "multipart/form-data"
    }
  }).then(res => res.data);
};
//用户登陆API
export const loginUrl = params => {
  return axios.post(`${base}/user/login`, params).then(res => res.data);
};

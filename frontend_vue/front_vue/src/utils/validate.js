/**
 * @author jay
 * @date 2020/2/23
 * @Description: 校验公共方法
 */
import i18n from "@/lang";

export default {
  install(Vue) {
    Vue.prototype.$Validate = {
      mobile: (rule, value, callback) => {
        // 验证手机号码
        let phoneReg = /^1(3|4|5|6|7|8|9)\d{9}$/;
        if (!phoneReg.test(value)) {
          callback(new Error(i18n.t("rules.validate.mobile")));
        } else {
          callback();
        }
      },
      chsIntAndEn_: (rule, value, callback) => {
        // 验证中文数字英文和_
        let nickNameReg = /^[\u4e00-\u9fa5a-zA-Z0-9_]+$/;
        if (!nickNameReg.test(value)) {
          callback(new Error(i18n.t("rules.validate.chsIntAndEn_")));
        } else {
          callback();
        }
      },
      intAndEn_: (rule, value, callback) => {
        // 验证中文数字英文和_
        let nickNameReg = /^[a-zA-Z0-9_]+$/;
        if (!nickNameReg.test(value)) {
          callback(new Error(i18n.t("rules.validate.intAndEn_")));
        } else {
          callback();
        }
      },
      email: (rule, value, callback) => {
        // 验证中文数字英文和_
        let emailReg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
        if (!emailReg.test(value)) {
          callback(new Error(i18n.t("rules.validate.email")));
        } else {
          callback();
        }
      }
    };
  }
};

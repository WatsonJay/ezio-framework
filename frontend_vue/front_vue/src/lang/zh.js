export default {
  //应用翻译
  app: {},
  //输入水印
  placeholder: {
    username: "用户名",
    password: "密码",
    nickname: "昵称",
    checkpassword: "确认密码",
    Email: "邮箱",
    phone: "电话"
  },
  //系统提示
  tip: {
    translate: "切换语言成功",
    backstageError: "后端异常，请联系管理员",
    slidingPic: "拖动左边滑块完成上方拼图",
    slidingPicError: "验证失败，请重试",
    slidingPicSuccess: "验证成功",
    pic: "请点击上传jpg/png文件，且不超过2M"
  },
  //校验规则
  rules: {
    common: {
      picType: "请点击上传jpg/png文件",
      picSize: "上传图片大小不能超过2MB"
    },
    username: {
      notnull: "请输入用户名"
    },
    password: {
      notnull: "请输入密码",
      notmatch: "密码不匹配"
    },
    userNickName: {
      notnull: "请输入昵称"
    },
    repassword: {
      notnull: "请再次输入密码"
    },
    Email: {
      notnull: "请输入邮箱"
    },
    validate: {
      length: "长度在 {min} 到 {max} 个字符",
      chsIntAndEn_: "请输入英文、_、数字、中文",
      intAndEn_: "请输入英文、_、数字",
      email: "请输入正确的邮箱",
      mobile: "请输入正确的手机号"
    }
  },
  //系统页面
  system: {
    login: {
      title: "系统登陆",
      login: "登陆",
      register: "注册",
      thirdLogin: "第三方登录"
    },
    register: {
      title: "用户注册",
      goback: "返回"
    },
    settings: {},
    guide: {}
  }
};

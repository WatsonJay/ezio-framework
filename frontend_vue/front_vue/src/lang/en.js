export default {
  //application Page
  app: {},
  //Input Placeholder
  placeholder: {
    username: "Username",
    password: "Password",
    nickname: "nickname",
    checkpassword: "checkpassword",
    Email: "Email",
    phone: "phone"
  },
  //System Tip
  tip: {
    translate: "Switch Language Success",
    backstageError: "backStage is exception, please contact administrator",
    slidingPic: "slide to complete the puzzle",
    slidingPicError: "varify fail,please retry",
    slidingPicSuccess: "varify success",
    pic: "Please upload jpg/png file, and no more than 2M"
  },

  //Check Rule
  rules: {
    common: {
      picType: "Please upload jpg/png file",
      picSize: "pic no more than 2MB"
    },
    username: {
      notnull: "plesae input usename"
    },
    password: {
      notnull: "plesae input password",
      notmatch: "password can not match"
    },
    userNickName: {
      notnull: "plesae input nickname"
    },
    repassword: {
      notnull: "plesae input password again"
    },
    Email: {
      notnull: "please input Email"
    },
    validate: {
      length: "length must between {min} and {max}",
      chsIntAndEn_: "please input EN,CHS,number or _",
      intAndEn_: "please input EN,number or _",
      email: "please input current E-Mail",
      mobile: "please input current mobilephone"
    }
  },
  //System Page
  system: {
    login: {
      title: "System Login",
      login: "Login",
      register: "Register",
      thirdLogin: "Third Login"
    },
    register: {
      title: "User Register",
      goback: "back"
    },
    settings: {},
    guide: {}
  }
};

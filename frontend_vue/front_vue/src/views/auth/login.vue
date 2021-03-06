<template>
  <el-container class="login_container">
    <el-main>
      <div class="login_div">
        <logo />
        <div
          class="background_div"
          v-loading="loading"
          element-loading-text="登陆中"
          element-loading-spinner="el-icon-loading"
          element-loading-background="rgba(0, 0, 0, 0.8)"
        >
          <div class="title_div">
            <h3 class="title">{{ $t("system.login.title") }}</h3>
            <lang-select class="language_select" />
          </div>
          <el-form
            class="login_form"
            :model="loginForm"
            ref="login"
            :rules="rules"
          >
            <el-form-item prop="userName">
              <svg-icon icon-class="user" />
              <el-input
                ref="userName"
                v-model="loginForm.userName"
                type="text"
                :placeholder="$t('placeholder.username')"
                tabindex="1"
              />
            </el-form-item>
            <el-form-item prop="password">
              <svg-icon icon-class="3701mima" />
              <el-input
                ref="password"
                v-model="loginForm.password"
                :type="passwordType"
                :placeholder="$t('placeholder.password')"
                tabindex="2"
              />
              <span class="show-pwd" @click="pwdShow">
                <svg-icon :icon-class="passwordType === 'password' ? 'yanjing_yincang' : 'yanjing_xianshi'" />
              </span>
            </el-form-item>
            <el-row :gutter="8" class="login-btn">
              <el-col :span="16">
                <el-popover
                  placement="top"
                  width="330"
                  trigger="manual"
                  v-model="visible"
                >
                  <SlidePic :key="uuid" @verify="login"></SlidePic>
                  <el-button
                    type="primary"
                    slot="reference"
                    @click="validate"
                    >{{ $t("system.login.login") }}</el-button
                  >
                </el-popover>
              </el-col>
              <el-col :span="8">
                <el-button @click="goRegister">{{
                  $t("system.login.register")
                }}</el-button>
              </el-col>
            </el-row>
            <el-button type="text">{{
              $t("system.login.thirdLogin")
            }}</el-button>
          </el-form>
        </div>
      </div>
    </el-main>
    <el-footer></el-footer>
  </el-container>
</template>

<script>
import Logo from "@/components/logo";
import LangSelect from "@/components/LangSelect";
import { loginUrl } from "@/api/auth/api.js";
// 组件懒加载
const SlidePic = () => import("@/components/SlidePic");
export default {
  name: "login",
  components: {
    Logo,
    LangSelect,
    SlidePic
  },
  data() {
    return {
      passwordType: "password",
      visible: false,
      loading: false,
      uuid: "",
      loginForm: {
        userName: "",
        password: ""
      }
    };
  },
  computed: {
    rules() {
      return {
        userName: [
          { required: true, message: this.$t("rules.username.notnull") },
          { validator: this.$Validate.chsIntAndEn_, trigger: "blur" }
        ],
        password: [
          { required: true, message: this.$t("rules.password.notnull") }
        ]
      };
    }
  },
  methods: {
    pwdShow() {
      if (this.passwordType == "password") {
        this.passwordType = "text";
      } else {
        this.passwordType = "password";
      }
      this.$nextTick(() => {
        this.$refs.password.focus();
      });
    },
    goRegister() {
      this.$router.push({ name: "register" });
    },
    login() {
      setTimeout(() => {
        this.visible = false;
      }, 500);
      this.$refs.login.validate(valid => {
        if (valid) {
          let params = Object.assign({}, this.loginForm);
          this.loading = true;
          loginUrl(params).then(response => {
            if (response.code == 200) {
              this.$message.success(response.message);
              this.$store.dispatch("user/setUser", {
                username: this.loginForm.userName,
                token: response.data.userToken,
                userNickName: response.data.userNickName
              });
              sessionStorage.setItem("access-token", response.data.userToken);
              sessionStorage.setItem("userName", this.loginForm.userName);
              sessionStorage.setItem("userNickName", response.data.userNickName);
              sessionStorage.setItem("userAvatorUrl", response.data.userPicUrl);
              this.$router.push({name:'Home'});
            }else {
              this.$message.error(response.message);
            }
            this.loading = false;
          },
          error =>{
            this.$message.error("登录异常，请重试")
            this.loading = false;
          });
        }
      });
    },
    validate() {
      this.visible = !this.visible;
      this.uuid = UUID.createUUID();
    }
  }
};
</script>

<!--替换全局样式-->
<style lang="scss">
$bg: #283443;
$light_gray: #fff;
$cursor: #fff;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .el-container .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */
.el-container {
  .el-input {
    //display: inline-block;
    height: 35px;
    width: 85%;

    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      padding: 12px 5px 12px 15px;
      color: $light_gray;
      height: 35px;
      caret-color: $cursor;

      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px $bg inset !important;
        -webkit-text-fill-color: $cursor !important;
      }
    }
  }

  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
  }
}
</style>

<style lang="scss" scoped>
$bg: #2d3a4b;
$dark_gray: #889aa4;
$light_gray: #eee;

.login_container {
  min-height: 100%;
  width: 100%;
  background-image: url("../../assets/img/bg.png");
  background-size: cover;
  .login_div {
    position: relative;
    height: 100%;
    width: 420px;
    max-width: 100%;
    padding: 160px 35px 0;
    margin: 0 auto;
    overflow: hidden;
    .background_div {
      background: rgba(255, 255, 255, 0.3);
      box-shadow: 0 0 15px #cac6c6;
      border-radius: 5px;
      .title_div {
        position: relative;
        .title {
          width: 100%;
          text-align: center;
          line-height: 50px;
          color: #fff;
          font-size: 20px;
          border-bottom: 1px solid #ddd;
        }
        .language_select {
          background: #ffffff;
          border-radius:4px;
          overflow: hidden;
          position: absolute;
          top: 13px;
          right: 20px;
          font-size: 20px;
          cursor: pointer;
        }
      }
      .login_form {
        padding: 20px 30px;
        text-align: center;
        .icontech {
          color: $dark_gray;
        }
        .show-pwd {
          position: absolute;
          right: 10px;
          top: 1px;
          font-size: 16px;
          color: $dark_gray;
          cursor: pointer;
          user-select: none;
        }
        .login-btn {
          text-align: center;
        }
        .login-btn button {
          width: 100%;
          height: 36px;
          padding: 3px 3px;
        }
      }
    }
  }
}
</style>

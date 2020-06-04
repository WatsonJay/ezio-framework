<template>
  <el-container class="register-container">
    <el-main>
      <div class="register_div">
        <div
          class="background_div"
          v-loading="loading"
          element-loading-text="登陆中"
          element-loading-spinner="el-icon-loading"
          element-loading-background="rgba(0, 0, 0, 0.8)"
        >
          <div class="title_div">
            <h3 class="title">{{ $t("system.register.title") }}</h3>
            <lang-select class="language_select" />
          </div>

          <el-upload
            class="avatar-uploader"
            ref="upload"
            action=""
            :show-file-list="false"
            :limit="1"
            :http-request="handleImg"
            :on-change="setAvatarPath"
            accept=".jpg,.jpeg,.gif,.png,.bmp"
          >
            <el-tooltip
              class="item"
              effect="dark"
              :content="$t('tip.pic')"
              placement="right"
            >
              <img v-if="imageUrl" :src="imageUrl" class="avatar" />
              <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-tooltip>
          </el-upload>

          <el-form
            class="register_form"
            :model="register"
            ref="register"
            :rules="rules"
          >
            <el-form-item prop="userName">
              <i class="icon-tech icon-user" />
              <el-input
                v-model="register.userName"
                :placeholder="$t('placeholder.username')"
              ></el-input>
            </el-form-item>
            <el-form-item prop="userNickName">
              <i class="icon-tech icon-postcard" />
              <el-input
                v-model="register.userNickName"
                :placeholder="$t('placeholder.nickname')"
              ></el-input>
            </el-form-item>
            <el-form-item prop="password">
              <span>
                <i class="icon-tech icon-3701mima" />
              </span>
              <el-input
                v-model="register.password"
                ref="password"
                :type="passwordType"
                :placeholder="$t('placeholder.password')"
              ></el-input>
              <span class="show-pwd" @click="pwdShow">
                <i
                  :class="
                    passwordType === 'password'
                      ? 'icon-tech icon-yanjing_yincang'
                      : 'icon-tech icon-yanjing_xianshi'
                  "
                />
              </span>
            </el-form-item>
            <el-form-item prop="checkpassword">
              <i class="icon-tech icon-key" />
              <el-input
                v-model="register.checkpassword"
                :type="passwordType"
                :placeholder="$t('placeholder.checkpassword')"
              ></el-input>
            </el-form-item>
            <el-form-item prop="userMail">
              <i class="icon-tech icon-youxiang" />
              <el-input
                v-model="register.userMail"
                :placeholder="$t('placeholder.Email')"
              ></el-input>
            </el-form-item>
            <el-form-item prop="userPhone">
              <i class="icon-tech icon-phone" />
              <el-input
                v-model="register.userPhone"
                :placeholder="$t('placeholder.phone')"
              ></el-input>
            </el-form-item>
            <el-row :gutter="8" class="login-btn">
              <el-col :span="16">
                <el-button type="primary" @click="registerUser">{{
                  $t("system.login.register")
                }}</el-button>
              </el-col>
              <el-col :span="8">
                <el-button @click="goBack">{{
                  $t("system.register.goback")
                }}</el-button>
              </el-col>
            </el-row>
          </el-form>
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import LangSelect from "@/components/LangSelect";
import { addOrUpadteUserUrl } from "@/api/auth/api.js";
export default {
  name: "register",
  components: {
    LangSelect
  },
  data() {
    return {
      passwordType: "password",
      loading: false,
      avatar: "",
      imageUrl: "",
      register: {
        userName: "",
        userNickName: "",
        password: "",
        checkpassword: "",
        userMail: "",
        userPhone: "",
        picName: "",
        userPicUrl: "",
        userPicDelUrl: ""
      }
    };
  },
  computed: {
    rules() {
      var validatePassword = (rule, value, callback) => {
        if (value === "") {
          callback(new Error(this.$t("rules.password.notnull")));
        } else {
          if (this.register.checkpassword !== "") {
            this.$refs.register.validateField("checkpassword");
          }
          callback();
        }
      };
      var validateRePassword = (rule, value, callback) => {
        if (value === "") {
          callback(new Error(this.$t("rules.repassword.notnull")));
        } else if (value !== this.register.password) {
          callback(new Error(this.$t("rules.password.notmatch")));
        } else {
          callback();
        }
      };
      return {
        userName: [
          {
            required: true,
            message: this.$t("rules.username.notnull"),
            trigger: "blur"
          },
          {
            min: 3,
            max: 15,
            message: this.$t("rules.validate.length", { min: "3", max: "15" }),
            trigger: "blur"
          },
          { validator: this.$Validate.intAndEn_, trigger: "blur" }
        ],
        userNickName: [
          {
            required: true,
            message: this.$t("rules.userNickName.notnull"),
            trigger: "blur"
          },
          {
            min: 3,
            max: 30,
            message: this.$t("rules.validate.length", { min: "3", max: "30" }),
            trigger: "blur"
          },
          { validator: this.$Validate.chsIntAndEn_, trigger: "blur" }
        ],
        password: [{ validator: validatePassword, trigger: "blur" }],
        checkpassword: [{ validator: validateRePassword, trigger: "blur" }],
        userMail: [
          {
            required: true,
            message: this.$t("rules.Email.notnull"),
            trigger: "blur"
          },
          { validator: this.$Validate.email, trigger: "blur" }
        ],
        userPhone: [{ validator: this.$Validate.mobile, trigger: "blur" }]
      };
    }
  },
  methods: {
    handleImg() {
      this.$refs.upload.clearFiles();
    },
    setAvatarPath(file) {
      const isLt2M = file.size / 1024 / 1024 < 2;
      const fileName = file.name;
      let regex = /(.jpg|.jpeg|.gif|.png|.bmp)$/;
      debugger;
      const hasFIle = regex.test(fileName.toLowerCase());
      if (!hasFIle) {
        this.$message.error(this.$t("rules.common.picType"));
        return;
      }
      if (!isLt2M) {
        this.$message.error(this.$t("rules.common.picSize"));
        return;
      }
      this.avatar = file;
      this.imageUrl = URL.createObjectURL(file.raw);
    },
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
    goBack: function() {
      this.$router.go(-1);
    },
    registerUser() {
      this.$refs.register.validate(valid => {
        //代表通过验证 ,将参数传回后台
        if (valid) {
          let formData = new FormData();
          formData.append("userName", this.register.userName);
          formData.append("userNickName", this.register.userNickName);
          formData.append("password", this.register.password);
          formData.append("userPhone", this.register.userPhone);
          formData.append("userMail", this.register.userMail);
          formData.append(
            "file",
            this.avatar ? this.avatar.raw : "", this.avatar ?this.avatar.name : ""
          );
          this.loading = true;
          addOrUpadteUserUrl(formData).then(response => {
            if (response.success) {
              this.$message.success(response.message);
              this.$router.push({ name: "login" });
            }
            this.loading = false;
          },error =>{
            this.loading = false;
          });
        }
      });
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

.register-container {
  min-height: 100%;
  width: 100%;
  background-image: url("../../assets/img/bg.png");
  background-size: cover;
  .register_div {
    position: relative;
    width: 500px;
    max-width: 100%;
    height: 100%;
    padding: 130px 35px 0;
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
          //color: #fff;
          overflow: hidden;
          position: absolute;
          top: 13px;
          right: 15px;
          font-size: 18px;
          cursor: pointer;
        }
      }
      .avatar-uploader {
        text-align: center;
        margin-top: 20px;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        .avatar,
        .avatar-uploader-icon {
          width: 70px;
          height: 70px;
          display: block;
          border-radius: 50%;
        }
        .avatar-uploader-icon {
          border: 1px dashed #d9d9d9;
          font-size: 18px;
          color: #8c939d;
          line-height: 70px;
        }
        .avatar-uploader-icon:hover {
          border-color: #409eff;
        }
      }
      .register_form {
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

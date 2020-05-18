<template>
  <el-dropdown trigger="click" class="international" @command="handleSetLanguage">
    <div class = "button">
      <i class="icon-tech icon-zhongyingwen"/>
    </div>
    <el-dropdown-menu slot="dropdown">
      <el-dropdown-item :disabled="language==='zh'" command="zh">
        中文
      </el-dropdown-item>
      <el-dropdown-item :disabled="language==='en'" command="en">
        English
      </el-dropdown-item>
    </el-dropdown-menu>
  </el-dropdown>
</template>

<script>
    export default {
      name: "langSelect",
      computed: {
        language() {
          return this.$store.getters.language
        }
      },
      methods: {
        handleSetLanguage(lang) {
          this.$i18n.locale = lang
          this.$store.dispatch('app/setLanguage', lang)
          this.$message({
            message: this.$t('tip.translate'),
            type: 'success'
          })
        }
      }
    }
</script>

<style lang="scss" scoped>
  .button{
    background: #fff;
    padding: 2px 4px;
    border-radius:4px;
  }
</style>

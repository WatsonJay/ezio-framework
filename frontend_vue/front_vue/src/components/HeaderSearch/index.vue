<template>
  <div :class="{ show: show }" class="header-search">
    <svg-icon class-name="search-icon" icon-class="sousuo" @click.stop="click"/>
    <el-select
      ref="headerSearchSelect"
      class="header-search-select"
      v-model="search"
      filterable
      default-first-option
      :placeholder="$t('placeholder.searchRouter')"
      remote
      :remote-method="querySearch"
      @change="change">
      <el-option v-for="item in options" :key="item.path" :value="item" :label="item.title.join(' > ')" />
    </el-select>
  </div>
</template>

<script>
import Fuse from "fuse.js";
import path from "path";
export default {
  name: "HeaderSearch",
  data() {
    return {
      search: "",
      options: [],
      searchPool: [],
      show: false,
      fuse: undefined
    };
  },
  computed: {},
  watch: {
    show(value) {
      if (value) {
        document.body.addEventListener('click', this.close)
      } else {
        document.body.removeEventListener('click', this.close)
      }
    }
  },
  mounted() {},
  methods: {
    initFuse(list){
      var fuseOptions = {
        shouldSort: true, // 是否按分数对结果列表排序
        threshold: 0.4, // 匹配算法阈值。阈值为0.0需要完全匹配（字母和位置），阈值为1.0将匹配任何内容。
        /**
         * 确定匹配与模糊位置（由位置指定）的距离。一个精确的字母匹配，即距离模糊位置很远的字符将被视为完全不匹配。
         *  距离为0要求匹配位于指定的准确位置，距离为1000则要求完全匹配位于使用阈值0.8找到的位置的800个字符以内。
         */
        location: 0, // 确定文本中预期找到的模式的大致位置。
        distance: 100,
        maxPatternLength: 32, // 模式的最大长度
        minMatchCharLength: 1, // 模式的最小字符长度
        // 搜索标题与作者名
        keys: [{
          name: 'title',
          weight: 0.7
        }, {
          name: 'path',
          weight: 0.3
        }]
      };
      this.fuse = new Fuse(list, fuseOptions);
    },
    click() {
      this.show = !this.show
      if (this.show) {
        this.$refs.headerSearchSelect && this.$refs.headerSearchSelect.focus()
      }
    },
    close(){
      this.$refs.headerSearchSelect && this.$refs.headerSearchSelect.blur()
      this.options = []
      this.show = false
    },
    querySearch(query) {
      if (query != ''){
        this.options = this.fuse.search(query)
      } else {
        this.options = []
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.header-search{
  font-size: 0 !important;

  .search-icon{
    cursor: pointer;
    font-size: 18px;
    vertical-align: middle;
  }

  .header-search-select{
    width: 0;
    font-size: 18px;
    transition: width 0.2s;
    overflow: hidden;
    background: transparent;
    display: inline-block;
    vertical-align: middle;

    ::v-deep .el-input__inner {
      border-radius: 0;
      border: 0;
      padding-left: 0;
      padding-right: 0;
      box-shadow: none !important;
      border-bottom: 1px solid #d9d9d9;
      vertical-align: middle;
    }
  }

  &.show{
    .header-search-select{
      width: 210px;
      margin-left: 10px;
    }
  }
}
</style>

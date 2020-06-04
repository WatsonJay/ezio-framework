<template>
  <div class="navbar">
    <Hamburger id="hamburger-container" :is-active="sidebar.opened" class="hamburger-container" @toggleClick="toggleSideBar"/>
    <div class="right-menu">
      <template v-if="device!=='mobile'">
        <lang-select class="right-menu-item hover-effect" />
      </template>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import Hamburger from "@/components/Hamburger";
import LangSelect from "@/components/LangSelect";
export default {
  components: {
    Hamburger,
    LangSelect
  },
  computed: {
    ...mapGetters([
      "sidebar",
      "device"
    ]),
  },
  methods: {
    toggleSideBar() {
      this.$store.dispatch("app/toggleSideBar");
    }
  }
};
</script>

<style lang="scss" scoped>
.navbar {
  height: 60px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 1px 4px rgba(0,21,41,.08);

  .hamburger-container{
    height: 100%;
    line-height: 54px;
    float: left;
    cursor: pointer;
    transition: background .3s;
    -webkit-tap-highlight-color:transparent;

    &:hover {
      background: rgba(0, 0, 0, .025)
    }
  }

  .right-menu {
    float: right;
    height: 100%;
    line-height: 50px;

    &:focus {
      outline: none;
    }
    .right-menu-item {
      display: inline-block;
      padding: 0 8px;
      height: 100%;
      font-size: 18px;
      color: #5a5e66;
      vertical-align: text-bottom;

      &.hover-effect {
        cursor: pointer;
        transition: background .3s;

        &:hover {
          background: rgba(0, 0, 0, .025)
        }
      }
    }
  }
}
</style>

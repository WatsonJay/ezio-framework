<template>
  <div :class="classObj" class="app-wrapper">
    <div v-if="device === 'mobile' && sidebar.opened" class="drawer-bg" @click="handleClickOutside"/>
    <sidebar class="sidebar-container" />
    <div :class="{hasTagView: needTagsView}" class="main-container">
      <div :class="{'fix-header': fixedHeader}">
        <Navbar />
      </div>
    </div>
  </div>
</template>

<script>
import ResizeMixin from "./mixins/ResizeHandler";
import { Sidebar, Navbar } from "./componments";
import { mapState } from "vuex";
export default {
  name: "Layout",
  components: {
    Sidebar,
    Navbar
  },
  mixins: [ResizeMixin],
  computed: {
    ...mapState({
      sidebar: state => state.app.sidebar,
      device: state => state.app.device,
      needTagsView: state => state.settings.tagsView,
      fixedHeader: state => state.settings.fixedHeader,
    }),
    classObj() {
      return {
        hideSidebar: !this.sidebar.opened,
        openSidebar: this.sidebar.opened,
        withoutAnimation: this.sidebar.withoutAnimation,
        mobile: this.device === "mobile"
      };
    }
  },
  methods: {
    handleClickOutside() {
      this.$store.dispatch("app/closeSideBar", { withoutAnimation: false });
    }
  }
};
</script>

<style lang="scss" scoped>
@import "~@/styles/mixins.scss";

.app-wrapper {
  @include clearfix;
  position: relative;
  height: 100%;
  width: 100%;
}

.drawer-bg {
  background: #000;
  opacity: 0.3;
  height: 100%;
  width: 100%;
  top: 0;
  position: absolute;
  z-index: 999;
}
</style>

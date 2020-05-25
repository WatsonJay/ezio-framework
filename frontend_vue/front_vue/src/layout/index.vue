<template>
  <div></div>
</template>

<script>
import ResizeMixin from "./mixins/ResizeHandler";
export default {
  name: "Layout",
  components: {

  },
  mixins: [ResizeMixin],
  computed: {
    classObj() {
      return {
        hideSidebar: !this.sidebar.opened,
        openSidebar: this.sidebar.opened,
        withoutAnimation: this.sidebar.withoutAnimation,
        mobile: this.device === "mobile"
      };
    }
  }
};
</script>

<style scoped></style>

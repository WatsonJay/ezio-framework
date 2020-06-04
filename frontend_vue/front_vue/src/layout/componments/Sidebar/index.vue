<template>
  <div :class="{ 'has-logo': showLogo }">
    <Logo v-if="showLogo" :collapse="isCollapse" />
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import Logo from './Logo'
import variables from '@/styles/variables.scss'
export default {
  components: {Logo},
  computed: {
    ...mapGetters([
      'sidebar',
    ]),
    showLogo() {
      return this.$store.state.settings.sidebarLogo;
    },
    isCollapse(){
      return !this.sidebar.opened;
    }
  }
};
</script>

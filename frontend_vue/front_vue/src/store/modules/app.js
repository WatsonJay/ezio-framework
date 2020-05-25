import Cookies from "js-cookie";
import { getLanguage } from "@/lang/index";

const state = {
  language: getLanguage(),
  siderbar: {
    opened: Cookies.get("sidebarStatus")
      ? !!+Cookies.get("sidebarStatus")
      : true,
    withoutAnimation: false
  },
  device: 'desktop',
};

const mutations = {
  SET_LANGUAGE: (state, language) => {
    state.language = language;
    Cookies.set("language", language);
  },
  CLOSE_SIDEBAR: (state, withoutAnimation) => {
    Cookies.set("sidebar", 0);
    state.siderbar.opened = false;
    state.siderbar.withoutAnimation = withoutAnimation;
  },
  TOGGLE_DEVICE: (state, device) =>{
    state.device = device;
  }
};

const actions = {
  setLanguage({ commit }, language) {
    commit("SET_LANGUAGE", language);
  },
  closeSideBar({ commit }, { withoutAnimation }) {
    commit("CLOSE_SIDEBAR", withoutAnimation);
  },
  toggleDevice({ commit }, device) {
    commit("TOGGLE_DEVICE", device);
  }
};

export default {
  namespaced: true,
  state,
  mutations,
  actions
};
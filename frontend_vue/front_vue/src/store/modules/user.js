const state = {
  user: { username: "", token: "", userNickName: "" } // 用户信息
};

const mutations = {
  SET_USER: (state, user) => {
    state.user = user;
  }
};

const actions = {
  setUser({ commit }, user) {
    commit("SET_USER", user);
  }
};

export default {
  namespaced: true,
  state,
  mutations,
  actions
};

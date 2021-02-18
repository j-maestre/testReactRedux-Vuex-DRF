import { createStore } from "vuex";
import user from "./modules/user";
import shipping from "./modules/shipping";

const state = {
  msg: {},
};
const mutations = {
  SET_MSG(state, payload) {
    state.msg = payload;
  },
};
const getters = {
  state_msg: (state) => {
    return state.msg;
  },
  state: (state) => {
    return state;
  },
};
const actions = {
  sendMsg({ commit }) {
    commit("SET_MSG", {
      type: false,
      title: "Login required",
      details: "",
    });
  },
};
const modules = {
  user,
  shipping,
};

const store = createStore({
  namespaced: true,
  state,
  mutations,
  getters,
  actions,
  modules,
});

export default store;

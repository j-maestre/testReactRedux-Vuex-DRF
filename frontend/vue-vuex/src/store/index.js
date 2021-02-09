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
const getters = {};
const actions = {};
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

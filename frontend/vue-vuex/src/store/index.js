import { createStore } from "vuex";
import user from "./modules/user";

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
};

const store = createStore({
  state,
  mutations,
  getters,
  actions,
  modules,
});

export default store;

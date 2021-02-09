import { createStore } from "vuex";
import user from "./modules/user";
import movement from "./modules/movement";

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

const store = createStore({
  state,
  mutations,
  getters,
  actions,
  modules,
});

export const modules = {
  user,
  movement,
};

export default store;

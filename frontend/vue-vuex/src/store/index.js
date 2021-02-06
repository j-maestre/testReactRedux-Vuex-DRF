import { createStore } from "vuex";
import { userLogin } from "../api";

const state = {
  count: 0,
  user: {},
  msg_success: "",
  msg_error: "",
};

const mutations = {
  setUser(state, data) {
    state.user = data;
  },
  setSuccess(state, msg) {
    state.msg_success = msg;
  },
  setError(state, msg) {
    state.msg_error = msg;
  },
  increment(state) {
    state.count++;
  },
  decrement(state) {
    state.count--;
  },
};

const actions = {
  async login({ commit }, credentials) {
    // Hacemos el login
    const result = await userLogin(credentials);

    console.log(result);
    // // Comprobamos la informacion
    // if (result.data.success) {
    //   localStorage.setItem("token", result.data);
    //   commit("setSuccess", "Authentication Success");
    //   router.push("/");
    // } else {
    //   commit("setError", "Authentication Failed");
    // }
    commit("setSuccess", "Authentication Success");
  },
};

const store = createStore({
  state,
  mutations,
  actions,
});

export default store;

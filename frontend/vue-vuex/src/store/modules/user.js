import { userApi } from "../../api";

const state = {
  token: "",
  loading: false,
  user: {},
};

const mutations = {
  SET_TOKEN(state, payload) {
    state.token = payload;
    payload
      ? localStorage.setItem("token", payload)
      : localStorage.removeItem("token");
  },
  SET_LOADER(state, payload) {
    state.loading = payload;
  },
  SET_USER(state, payload) {
    state.user = payload;
  },
};
const getters = {};

const actions = {
  async logout({ commit }) {
    commit("SET_TOKEN", "");
    commit("SET_USER", {});

    commit(
      "SET_MSG",
      {
        type: true,
        title: "Logout success",
        details: "The logout was successful",
      },
      { root: true }
    );
  },
  async login({ commit }, credentials) {
    commit("SET_LOADER", true);

    try {
      // REGISTER
      var request = await userApi.login(credentials);

      // SUCCESS
      commit(
        "SET_MSG",
        {
          type: true,
          title: "Authentication success",
          details: "The login was successful",
        },
        { root: true }
      );
      commit("SET_TOKEN", request.data.user.token);
      commit("SET_USER", {
        username: request.data.user.username,
        email: request.data.user.email,
      });
    } catch (error) {
      let log = Object.entries(error.response.data.errors).map(
        ([key, value]) => key + ": " + value
      );

      // ERROR
      commit(
        "SET_MSG",
        {
          type: false,
          title: "Authentication failed",
          details: "" + log,
        },
        { root: true }
      );
      return false;
    }

    commit("SET_LOADER", false);
    return request;
  },

  async register({ commit }, credentials) {
    commit("SET_LOADER", true);

    try {
      // REGISTER
      var request = await userApi.register(credentials);

      // SUCCESS
      commit(
        "SET_MSG",
        {
          type: true,
          title: "Authentication success",
          details: "The login was successful",
        },
        { root: true }
      );

      commit("SET_TOKEN", request.data.user.token);
      commit("SET_USER", {
        username: request.data.user.username,
        email: request.data.user.email,
      });
    } catch (error) {
      let log = Object.entries(error.response.data.errors).map(
        ([key, value]) => key + ": " + value
      );

      // ERROR
      commit(
        "SET_MSG",
        {
          type: false,
          title: "Registration failed",
          details: "" + log,
        },
        { root: true }
      );
      return false;
    }

    commit("SET_LOADER", false);

    return request;
  },
  async checkout({ commit }) {
    const token = localStorage.getItem("token");

    if (!token) {
      return true;
    }

    try {
      var request = await userApi.checkout(token);

      commit("SET_TOKEN", request.data.user.token);
      commit("SET_USER", {
        username: request.data.user.username,
        email: request.data.user.email,
      });
    } catch (error) {
      let log = Object.entries(error.response.data.errors).map(
        ([key, value]) => key + ": " + value
      );

      // ERROR
      commit(
        "SET_MSG",
        {
          type: false,
          title: "Registration failedd",
          details: "" + log,
        },
        { root: true }
      );
      return false;
    }
  },
};

export default { namespaced: true, state, mutations, getters, actions };

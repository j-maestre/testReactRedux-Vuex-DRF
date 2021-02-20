import { userApi } from "../../api";
import { failed } from "../utils/failed";

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
  logout({ commit }) {
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
      return failed(commit, error, "Authentication failed");
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
      return failed(commit, error, "Registration failed");
    }

    commit("SET_LOADER", false);

    return request;
  },
  async checkout({ commit }) {
    try {
      var request = await userApi.getProfile();

      commit("SET_TOKEN", request.data.user.token);
      commit("SET_USER", {
        username: request.data.user.username,
        email: request.data.user.email,
      });
    } catch (error) {
      return failed(commit, error, false);
    }
  },

  async getProfile({ commit }) {
    try {
      return await userApi.getProfile();
    } catch (error) {
      return failed(commit, error, "Registration failed");
    }
  },

  async updateProfile({ commit }, form) {
    try {
      return await userApi.updateProfile(form);
    } catch (error) {
      return failed(commit, error, "Registration failed");
    }
  },
};

export default { namespaced: true, state, mutations, getters, actions };

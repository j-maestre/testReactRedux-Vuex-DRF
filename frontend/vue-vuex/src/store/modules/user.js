import { userApi } from "../../api";

const state = {
  token: {},
  loading: false,
  user: {},
};
const mutations = {
  LOGIN(state, payload) {
    state.token = payload;
  },
  SET_LOADER(state, payload) {
    state.loading = payload;
  },
  SET_USER(state, payload) {
    state.user = payload;
  },
};
const actions = {
  login({ commit }, credentials) {
    commit("SET_LOADER", true);

    userApi
      .login(credentials)
      .then(() => {
        commit(
          "SET_MSG",
          {
            type: true,
            title: "Authentication success",
            details: "The login was successful",
          },
          { root: true }
        );
        commit("LOGIN", credentials);
      })
      .catch(() =>
        commit(
          "SET_MSG",
          {
            type: false,
            title: "Authentication failed",
            details: "The login was completed incorrectly",
          },
          { root: true }
        )
      );

    commit("SET_LOADER", false);
  },

  register({ commit }, credentials) {
    commit("SET_LOADER", true);

    userApi
      .register(credentials)
      .then(() => {
        userApi
          .login(credentials)
          .then(() => {
            commit(
              "SET_MSG",
              {
                type: true,
                title: "Registation success",
                details: "The register was successful",
              },
              { root: true }
            );
            commit("LOGIN", credentials);
          })
          .catch(() =>
            commit("SET_MSG", {
              type: false,
              title: "Registation failed",
              details: "The register was completed incorrectly",
            })
          );
      })
      .catch(() =>
        commit(
          "SET_MSG",
          {
            type: false,
            title: "Registation failed",
            details: "The register was completed incorrectly",
          },
          { root: true }
        )
      );

    commit("SET_LOADER", false);
  },
};
const getters = {};

export default { namespaced: true, state, mutations, getters, actions };

const state = {
  category: null,
  filters: null,
  travel: null
};

const mutations = {
  SET_CATEGORY(state, payload) {
    state.category = payload;
  },
  SET_FILTERS(state, payload) {
    state.filters = payload;
  },
};

const actions = {
  setCategory({ commit }, idcategory) {
    commit("SET_CATEGORY", idcategory);
  },
  seFilters({ commit }, filters) {
    commit("SET_FILTERS", filters);
  }
};

const getters = {};

export default { namespaced: true, state, mutations, getters, actions };

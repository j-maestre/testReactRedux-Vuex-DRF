const state = {
  category: null,
};
const mutations = {
  SET_CATEGORY(state, payload) {
    state.category = payload;
  },
};
const actions = {
  setCategory({ commit }, idcategory) {
    commit("SET_CATEGORY", idcategory);
  },
};
const getters = {};

export default { namespaced: true, state, mutations, getters, actions };

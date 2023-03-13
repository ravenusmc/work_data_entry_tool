import Vue from 'vue';
import Vuex from 'vuex';


Vue.use(Vuex);

const data = {
  userObject: [],
};

const getters = {
  userObject: (state) => state.userObject,
};

const mutations = {

  setUserObject(state, value) {
    state.userObject = value;
  },

};

export default {
  namespaced: true,
  state: data,
  getters,
  mutations,
};
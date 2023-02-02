import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const data = {
	actionFound: false,
	actionNumber: '',
};

const getters = {
	actionFound: (state) => state.actionFound,
	actionNumber: (state) => state.actionNumber,
};

const actions = {

	locateAction: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/locateAction';
		axios.post(path, payload)
			.then((res) => {
				commit('setActionFound', res.data);
				commit('setActionNumber', payload['actionNumber'])
			})
			.catch((error) => {
				console.log(error);
			});
	},

	submitAction: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/submitAction';
		axios.post(path, payload)
			.then((res) => {
				
				commit('setActionNumber', payload['actionNumber'])
				commit('setActionFound', false);
			})
			.catch((error) => {
				console.log(error);
			});
	},

};

const mutations = {

	setActionFound(state, value) {
		state.actionFound = value;
	},

	setActionNumber(state, value) {
		state.actionNumber = value
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};
import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const data = {
	actionFound: false,
	actionID: 0,
	actionNumber: '',
};

const getters = {
	actionFound: (state) => state.actionFound,
	actionID: (state) => state.actionID,
	actionNumber: (state) => state.actionNumber,
};

const actions = {

	locateAction: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/locateAction';
		axios.post(path, payload)
			.then((res) => {
				console.log(res.data)
				if (res.data[0] === true) {
					commit('setActionFound', res.data[0]);
					commit('setActionID', res.data[1]);
					commit('setActionNumber', payload['actionNumber'])
				} else {
					commit('setActionFound', res.data[0]);
				}
			})
			.catch((error) => {
				console.log(error);
			});
	},

	submitActionToDatabase: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/submitActionToDatabase';
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

	setActionID(state, value) {
		state.actionID = value;
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
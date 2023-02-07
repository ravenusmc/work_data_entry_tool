import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const data = {
	actionFound: false,
	actionNotFound: false, 
	actionID: 0,
	actionNumber: '',
};

const getters = {
	actionFound: (state) => state.actionFound,
	actionNotFound: (state) => state.actionNotFound,
	actionID: (state) => state.actionID,
	actionNumber: (state) => state.actionNumber,
};

const actions = {

	locateAction: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/locateAction';
		axios.post(path, payload)
			.then((res) => {
				if (res.data[0] === true) {
					commit('setActionFound', res.data[0]);
					commit('setActionID', res.data[1]);
					commit('setActionNumber', payload['actionNumber'])
				} else {
					let ActionNotFound = !res.data[0] 
					commit('setActionNotFound', ActionNotFound);
					commit('setActionNumber', payload['actionNumber'])
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

	setActionNotFound(state, value) {
		state.actionNotFound = value;
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
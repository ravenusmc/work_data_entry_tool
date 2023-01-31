import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const data = {
};

const getters = {
};

const actions = {

	locateAction: ({ commit }, { payload }) => {
		console.log("ACTION")
		const path = 'http://localhost:5000/locateAction';
		axios.post(path, payload)
			.then((res) => {
				console.log(res.data)
				// commit('setLoginFlag', res.data.login_flag);
			})
			.catch((error) => {
				console.log(error);
			});
	},


};

const mutations = {

	// setUserNotFound(state, value) {
	// 	state.userNotFound = value;
	// },

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};
import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import router from '../../router';

Vue.use(Vuex);

const data = {
	userNotFound: false,
	passwordNoMatch: false,
	loginFlag: false,
};

const getters = {
	userNotFound: (state) => state.userNotFound,
	passwordNoMatch: (state) => state.passwordNoMatch,
	loginFlag: (state) => state.loginFlag,
};

const actions = {

	setUpUser: (context, { payload }) => {
		console.log("ACTION")
		console.log(payload)
	// 	const path = 'http://localhost:5000/signup';
	// 	axios.post(path, payload)
	// 		.then((res) => {
	// 			router.push({ name: 'login' });
	// 		})
	// 		.catch((error) => {
	// 			console.log(error);
	// 		});
	},

};

const mutations = {

	setUserNotFound(state, value) {
		state.userNotFound = value;
	},

	setNoPasswordMatch(state, value) {
		state.passwordNoMatch = value;
	},

	setLoginFlag(state, value) {
		state.loginFlag = value;
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};
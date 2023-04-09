import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';

Vue.use(Vuex);

const data = {
	actionFound: false,
	actionNotFound: false, 
	actionID: 0,
	actionNumber: '',
	missingActionSubmitted: false, 
	actionsByUser: {},
	actionData: [],
	showUserActions: false, 
};

const getters = {
	actionFound: (state) => state.actionFound,
	actionNotFound: (state) => state.actionNotFound,
	actionID: (state) => state.actionID,
	actionNumber: (state) => state.actionNumber,
	missingActionSubmitted: (state) => state.missingActionSubmitted,
	actionsByUser: (state) => state.actionsByUser,
	actionData: (state) => state.actionData,
	showUserActions: (state) => state.showUserActions,
};

const actions = {

	locateAction: ({ commit }, { payload }) => {
		commit('setMissingActionSubmitted', false)
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

	submitMissingActionToDatabase: ({ commit }, { payload }) => {
		console.log('payload')
		const path = 'http://localhost:5000/submitMissingActionToDatabase';
		axios.post(path, payload)
			.then((res) => {
				commit('setMissingActionSubmitted', res.data)
			})
			.catch((error) => {
				console.log(error);
			});
	},

	getSpecificActionsByUser: ({ commit, getters }) => {
		const user = {
			id: store.state.session.userObject.id,
			ieNumber: store.state.session.userObject.ieNumber
		};
		const path = 'http://localhost:5000/actionsByUser';
		axios.post(path, user)
			.then((res) => {
				commit('setActionsByUser', res.data)
			})
			.catch((error) => {
				console.log(error);
			});
	},
	
	fetchDrillDownDataForForm: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/fetchDrillDownDataForForm';
		axios.post(path, payload)
			.then((res) => {
				commit('setActionData', res.data)
			})
			.catch((error) => {
				console.log(error);
			});
	},

	updateData: ({ commit }, { payload }) => {
		payload['id'] = store.state.session.userObject.id
		payload['userIENumber'] = store.state.session.userObject.ieNumber
		const path = 'http://localhost:5000/updateAction';
		axios.post(path, payload)
			.then((res) => {
				commit('setActionsByUser', res.data)
			})
			.catch((error) => {
				console.log(error);
			});
	},

	filterTableAction: ({ commit }, { payload }) => {
		payload['id'] = store.state.session.userObject.id
		payload['userIENumber'] = store.state.session.userObject.ieNumber
		const path = 'http://localhost:5000/filterTable';
		axios.post(path, payload)
			.then((res) => {
				commit('setActionsByUser', res.data)
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

	setMissingActionSubmitted(state, value) {
		state.missingActionSubmitted = value
	},

	setActionsByUser(state, value) {
		state.actionsByUser = value
	},

	setActionData(state, value) {
		state.actionData = value
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};
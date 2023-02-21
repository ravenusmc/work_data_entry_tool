import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const data = {
	actionFound: false,
};

const getters = {
	actionFound: (state) => state.actionFound,
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

};

const mutations = {

	setActionFound(state, value) {
		state.actionFound = value;
	},


};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};
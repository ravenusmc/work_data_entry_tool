import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const data = {
	allActionsByCount: [['Action Type', 'Count'], 
	['101', 255], 
	['500', 239], 
	['702', 246], 
	['792', 260]],
	recruitTypes: [['Recruit Type', 'Count'], 
	['True', 506], 
	['False', 494]],
	ieNumbers: ['ie7046', 'ie7001',  'ie7002', 'ie7003'],
	typeOfAction: ['101', '500', '702', '792'],
	actionsByIenumber: [['Action Type', 'Count'], 
	['101', 226], 
	['500', 226], 
	['702', 226], 
	['792', 226]],
};

const getters = {
	allActionsByCount: (state) => state.allActionsByCount,
	recruitTypes: (state) => state.recruitTypes,
	ieNumbers: (state) => state.ieNumbers,
	typeOfAction: (state) => state.typeOfAction,
	actionsByIenumber: (state) => state.actionsByIenumber,
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
		state.allActionsByCount = value;
	},


};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};
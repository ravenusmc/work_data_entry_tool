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
	legalAuthority: [['Legal Authority', 'Count'], 
	['MOW', 246], 
	['CHG', 260], 
	['ACC', 254], 
	['CON', 239]],
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
	legalAuthority: (state) => state.legalAuthority,
};

const actions = {

	changeDynamicGraphs: ({ commit }, { payload }) => {
		console.log(payload)
		const path = 'http://localhost:5000/changeDynamicGraphs';
		axios.post(path, payload)
			.then((res) => {
				commit('setActionsByIeNumber', res.data)
			})
			.catch((error) => {
				console.log(error);
			});
	},

};

const mutations = {

	setActionsByIeNumber(state,value) {
		state.actionsByIenumber = value
	},


};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};
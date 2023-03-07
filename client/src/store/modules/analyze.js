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
	recruitActionCount: [['Recruit Action', 'Count'], 
	['True', 112], 
	['False', 114]]
};

const getters = {
	allActionsByCount: (state) => state.allActionsByCount,
	recruitTypes: (state) => state.recruitTypes,
	ieNumbers: (state) => state.ieNumbers,
	typeOfAction: (state) => state.typeOfAction,
	actionsByIenumber: (state) => state.actionsByIenumber,
	legalAuthority: (state) => state.legalAuthority,
	recruitActionCount: (state) => state.recruitActionCount,
};

const actions = {

	changeDynamicGraphs: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/changeDynamicGraphs';
		axios.post(path, payload)
			.then((res) => {
				console.log(res.data[1])
				commit('setActionsByIeNumber', res.data[0])
				commit('setRecruitActionCount', res.data[1])
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

	setRecruitActionCount(state, value) {
		state.recruitActionCount = value
	},


};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};
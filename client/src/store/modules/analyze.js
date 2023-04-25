import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';

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
	ieNumbers: ['ie7046', 'ie7001', 'ie7002', 'ie7003'],
	selectedIENumber: 'ie7046',
	typeOfAction: ['101', '500', '702', '792'],
	actionsByIenumber: [['Action Type', 'Count'], 
	['101', 54], 
	['500', 60], 
	['702', 55], 
	['792', 57]],
	recruitActionCount: [['Recruit Action', 'Count'],
	['True', 112],
	['False', 114]],
	stackedGraph: [['Action', 'ie7046', 'ie7001', 'ie7002', 'ie7003'], 
	['101', 54, 69, 63, 69], 
	['500', 60, 59, 61, 59], 
	['702', 55, 70, 57, 64], 
	['792', 57, 65, 75, 63]],
	drillDownData: [],
};

const getters = {
	allActionsByCount: (state) => state.allActionsByCount,
	recruitTypes: (state) => state.recruitTypes,
	ieNumbers: (state) => state.ieNumbers,
	typeOfAction: (state) => state.typeOfAction,
	actionsByIenumber: (state) => state.actionsByIenumber,
	legalAuthority: (state) => state.legalAuthority,
	recruitActionCount: (state) => state.recruitActionCount,
	stackedGraph: (state) => state.stackedGraph,
	drillDownData: (state) => state.drillDownData,
	selectedIENumber: (state) => state.selectedIENumber,
};

const actions = {

	changeDynamicGraphs: ({ commit }, { payload }) => {
		commit('setSelectedIENumber', payload['ieNumber'])
		const path = 'http://localhost:5000/changeDynamicGraphs';
		axios.post(path, payload)
			.then((res) => {
				commit('setActionsByIeNumber', res.data[0])
				commit('setRecruitActionCount', res.data[1])
			})
			.catch((error) => {
				console.log(error);
			});
	},

	fetchDrillDownData: ({ commit }, { payload }) => {
		if (payload['needsIENUMBER']) {
			payload['IENumber'] = store.state.analyze.selectedIENumber
		}
		const path = 'http://localhost:5000/fetchDrillDownDataForGraphs';
		axios.post(path, payload)
			.then((res) => {
				commit('setDrillDownData', res.data)
			})
			.catch((error) => {
				console.log(error);
			});
	},

};

const mutations = {

	setActionsByIeNumber(state, value) {
		state.actionsByIenumber = value
	},

	setRecruitActionCount(state, value) {
		state.recruitActionCount = value
	},

	setDrillDownData(state, value) {
		state.drillDownData = value
	},

	setSelectedIENumber(state, value) {
		state.selectedIENumber = value
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};
import demandas from './fake/demandas'

import OngService from '../services/OngService';

let serviceOng = new OngService();

export const state = () => ({
  list: [],
  perfil: {},
  demandas: [],
  ong: {}
})

export const mutations = {
  UPDATE_ONGS(state, payload) {
    state.list = payload
  },
  UPDATE_ONG(state, payload) {
    state.list = payload
  },
  UPDATE_PERFIL(state, payload) {
    state.list = payload
  },
  UPDATE_DEMANDAS(state, payload) {
    state.demandas = payload
  }
}
export const actions = {
  fetchOng(context, id) {
    serviceOng.show(id)
      .then((ong) => context.commit('UPDATE_ONGS', ong.toJSON()))
      .catch((err) => console.log(err))
  },

  fetchOngs(context) {
    this.$OngService.index()
      .then((response) => context.commit('UPDATE_ONGS', response))
      .catch((err) => console.log(err))
  },

  fetchPerfilOng(context, id) {
    context.commit('UPDATE_PERFIL', this.$OngService.show(id))
  },

  fetchDemandas(context) {
    context.commit('UPDATE_DEMANDAS', demandas)
  }
}

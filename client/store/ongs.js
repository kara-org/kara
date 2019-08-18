import demandas from './fake/demandas'

export default {
  state() {
    return {
      ongs: [],
      perfil: {},
      demandas: []
    }
  },
  mutations: {
    UPDATE_ONGS(state, payload) {
      state.ongs = payload
    },
    UPDATE_PERFIL(state, payload) {
      state.ongs = payload
    },
    UPDATE_DEMANDAS(state, payload) {
      state.demandas = payload
    },
  },
  actions: {
    fetchOngs(context) {
      context.commit('UPDATE_ONGS', this.$OngService.index())
    },

    fetchPerfilOng(context, id) {
      context.commit('UPDATE_PERFIL', this.$OngService.show(id))
    },

    fetchDemandas(context) {
      context.commit('UPDATE_DEMANDAS', demandas)
    }
  }
}
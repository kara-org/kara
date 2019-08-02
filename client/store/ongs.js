import demandas from './fake/demandas'

export const states = {
  ongs: [],
  perfil: {},
  demandas: []
}

export const mutations = {
  UPDATE_ONGS (state, payload) {
    state.ongs = payload
  },
  UPDATE_PERFIL (state, payload) {
    state.ongs = payload
  },
  UPDATE_DEMANDAS (state, payload) {
    state.demandas = payload
  }
}

export const actions = {
  fetchOngs (context) {
    context.commit('UPDATE_ONGS', this.$OngService.index())
  },

  fetchPerfilOng (id) {
    context.commit('UPDATE_PERFIL', this.$OngService.show(id))
  },

  fetchDemandas (id) {
    context.commit('UPDATE_DEMANDAS', demandas)
  }
}

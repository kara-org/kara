import demandas from './fake/demandas'

export const state = () => ({
  list: [],
  perfil: {},
  demandas: []
})

export const mutations = {
  UPDATE_ONGS(state, payload) {
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
export const state = () => ({
  ongSelecionada: {},
  list: [],
  demanda: {}
})

export const mutations = {
  UPDATE_ONG(state, payload) {
    state.ongSelecionada = payload
  },
  UPDATE_DEMANDAS(state, payload) {
    state.list = payload
  },
  SET_DEMANDA(state, demanda) {
    state.list = state.list.map((i) => {
      if (i.id === demanda.id) {
        i.data_fim = demanda.data_fim
        i.data_inicio = demanda.data_inicio
        i.descricao = demanda.descricao
        i.quantidade_solicitada = demanda.quantidade_solicitada
      }
      return i
    })
  },
  ADD_DEMANDA(state, payload) {
    state.list.push(payload)
  },
  INATIVA_DEMANDA(state, demanda) {
    state.list = state.list.map((i) => {
      if (i.id === demanda.id) {
        i.ativo = false
      }
      return i
    })
  },
}

export const actions = {
  fetchOng(context, id) {
    this.$OngService.show(id)
      .then((payload) => {
        context.commit('UPDATE_ONG', payload)
      })
      .catch((err) => console.log(err))
  },

  createDemanda(_, idComposer, payload) {
    this.$axios.$post(`/ong/${idComposer}/demandas/`, payload)
      .catch((err) => console.log(err))
  },

  fetchDemandas(context) {
    this.$axios.$get('/demandas/')
      .then((response) => context.commit('UPDATE_DEMANDAS', response))
      .catch((err) => console.log(err))
  },

  fetchDemandasOng(context, idComposer) {
    this.$axios.$get(`/ong/${idComposer}/demandas/`)
      .then((response) => {
        context.commit('UPDATE_DEMANDAS', response.data);
        context.commit('UPDATE_ONG', response.data[0].ong);
      })
      .catch((err) => console.log(err))
  },

  changeDemanda(_, id, payload) {
    this.$axios.$patch(`/demanda/${id}/`, payload)
      .then((response) =>
        context.commit('SET_DEMANDA', response))
      .catch((err) => console.log(err))
  },

  deleteDemanda(context, id) {
    this.$axios.$delete(`/demanda/${id}/cancelar`)
      .then((response) =>
        context.commit('INATIVA_DEMANDA', response))
      .catch((err) => console.log(err))
  },
}

export const getters = {
  demanda: (state) => {
    return state.demanda
  },
  ong: (state) => {
    return state.ongSelecionada
  },
  demandas: (state) => {
    return state.list
  }
}

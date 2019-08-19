export const state = () => ({
  list: [],
  default: [],
  searchTerm: '',
  tipo: ''
})

export const mutations = {
  ORDER_ITENS(state){
    state.list.sort((a, b) => a.titulo.localeCompare(b.titulo))
  },
  UPDATE_TIPO(state, payload) {
    state.tipo = payload
  },
  UPDATE_SEARCH_TERM(state, payload) {
    state.searchTerm = payload
  },
  UPDATE_RESULTADOS(state, payload) {
    state.list = payload
  },
  TO_DEFEAULT_RESULTADOS(state) {
    state.list = state.default
  },
  SET_DEFEAULT_RESULTADOS(state, payload) {
    state.default = payload
  }
}

export const actions = {
  async buscar({ commit, dispatch }, { tipo, palavraChave }) {
    commit('UPDATE_TIPO', tipo)
    commit('UPDATE_SEARCH_TERM', palavraChave)
    return await this.$BuscarService.buscar(palavraChave).then(response => {
      if (response.length !== 0) {
        commit('UPDATE_RESULTADOS', response)
      } else {
        commit('TO_DEFEAULT_RESULTADOS')
      }
      commit('ORDER_ITENS')
    })
  },
  async fetchBusca({ commit, dispatch }, tipo) {
    return await this.$BuscarService
      .fetch(tipo)
      .then(response => {
        commit('UPDATE_RESULTADOS', response)
        commit('SET_DEFEAULT_RESULTADOS', response)
        commit('ORDER_ITENS')
      })
      .catch(err => {
        console.log(err);
        dispatch('global/addErro', err, { root: true })
      })
      .then(() => dispatch('global/stopLoading', null, { root: true }))
  }
}

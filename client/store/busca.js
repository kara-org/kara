

export const state = () => ({
  list: []
})

export const mutations = {
  UPDATE_RESULTADOS(state, payload) {
    state.list = payload
  }
}

export const actions = {
  async fetchBusca({ commit, dispatch }, params) {
    return await this.$BuscarService
      .buscar(params)
      .then(response => {
        console.log(response);
        commit('UPDATE_RESULTADOS', response)
      })
      .catch(err => {

        dispatch('global/addErro', err, { root: true })
      })
      .then( () => dispatch('global/stopLoading', null, { root: true }))
  }
}

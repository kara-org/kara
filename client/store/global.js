
export const state = () => ({
  loading: false,
  erros: []
})

export const mutations = {
  ADD_ERRO (state, payload) {
    state.erros.push(payload)
  },
  START_LOAGING (state) {
    state.loading = true
  },
  STOP_LOAGING (state) {
    state.loading = false
  }
}

export const actions = {
  addErro (context, erro) {
    context.commit('ADD_ERRO', erro)
  },
  startLoading (context) {
    context.commit('START_LOAGING')
  },
  stopLoading (context) {
    context.commit('STOP_LOAGING')
  }
}

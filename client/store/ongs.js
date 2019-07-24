export const states = {
  ongs: [],
  perfil: {}
}

export const mutations = {
  UPDATE_ONGS (state, payload) {
    state.ongs = payload
  },
  UPDATE_PERFIL (state, payload) {
    state.ongs = payload
  }
}

export const actions = {
  fetchOngs () {
    context.commit('UPDATE_ONGS', this.$OngService.index())
  },

  fetchPerfilOng (id) {
    context.commit('UPDATE_PERFIL', this.$OngService.show(id))
  }
}

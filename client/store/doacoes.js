export const state = () => ({
  ong: {},
  list: [],
  list_item: [],
  usuario: {}
})

export const mutations = {
  UPDATE_ONG(state, payload) {
    state.ong = payload
  },

  UPDATE_USUARIO(state, payload) {
    state.usuario = payload
  },

  UPDATE_DOACOES(state, payload) {
    state.list = payload
  },

  SET_ITEM_DOACAO(state, item) {
    state.list = state.list.map((d) => {
      if (d.id === doacao.id) {
        d.item_doacao = state.list.map((i) => {
          if (i.id === id) {
            i.quantidade_prometida = item.quantidade_prometida
          }
          return i
        })
      }
      return d
    })
  },

  ADD_DOACAO(state, payload) {
    state.list.push(payload)
  },

  ADD_ITEM_DOACAO(state, payload) {
    state.list_item.push(payload)
  },

  CANCELA_DOACAO(state, id) {
    state.list = state.list.map((d) => {
      if (d.id === id) {
        d = state.list.map((i) => {
          i.status.codigo_status = 3
          i.status.mensagem = "CANCELADA"
          return i
        })
      }
      return d
    })
  },

  CANCELA_ITEM_DOACAO(state, id) {
    state.list = state.list.map((d) => {
      return d.item_doacao = d.item_doacao.map((i) => {
        if (i.id === id) {
          i.status.codigo_status = 3
          i.status.mensagem = "CANCELADA"
        }
        return i
      })
    })
  },

  CONFIRMA_DOACAO(state, id) {
    state.list = state.list.map((d) => {
      if (d.id === id) {
        d = state.list.map((i) => {
          i.status.codigo_status = 2
          i.status.mensagem = "ENTREGUE"
          return i
        })
      }
      return d
    })
  },

  CONFIRMA_ITEM_DOACAO(state, id) {
    state.list = state.list.map((d) => {
      return d.item_doacao = d.item_doacao.map((i) => {
        if (i.id === id) {
          i.status.codigo_status = 2
          i.status.mensagem = "ENTREGUE"
        }
        return i
      })
    })
  },
}

export const actions = {
  createDoacao(_, payload) {
    this.$axios.$post(`/doacao/`, payload)
      .then((response) => {
        context.commit('ADD_DOACAO', response)
      })
      .catch((err) => console.log(err))
  },

  fetchDoacoesOng(context, idComposer) {
    this.$axios.$get(`/ong/${idComposer}/doacoes/`)
      .then((response) => {
        context.commit('UPDATE_DOACOES', response)
        context.commit('UPDATE_ONG', response[0].item_doacao[0].demanda.ong)
      })
      .catch((err) => console.log(err))
  },

  fetchDoacoesDoador(context, idComposer) {
    this.$axios.$get(`/doador/${idComposer}/doacoes/`)
      .then((response) => {
        context.commit('UPDATE_DOACOES', response)
        context.commit('UPDATE_USUARIO', response[0].usuario)
      })
      .catch((err) => console.log(err))
  },

  changeItemDoacao(_, payload) {
    this.$axios.$patch(`/item/${payload.id}/`, payload)
      .then((_) =>
        context.commit('SET_ITEM_DOACAO', payload))
      .catch((err) => console.log(err))
  },

  deleteItemDoacao(context, id) {
    this.$axios.$delete(`/item/${id}/cancelar`)
      .then((_) =>
        context.commit('CANCELA_ITEM_DOACAO', id))
      .catch((err) => console.log(err))
  },

  deleteDoacao(context, id) {
    this.$axios.$delete(`/doacao/${id}/cancelar`)
      .then((_) =>
        context.commit('CANCELA_DOACAO', id))
      .catch((err) => console.log(err))
  },

  confirmaItemDoacao(context, id) {
    this.$axios.$post(`/item/${id}/confirmar/`)
      .then((_) =>
        context.commit('CONFIRMA_ITEM_DOACAO', id))
      .catch((err) => console.log(err))
  },

  confirmaDoacao(context, id) {
    this.$axios.$post(`/doacao/${id}/confirmar/`)
      .then((_) =>
        context.commit('CONFIRMA_DOACAO', id))
      .catch((err) => console.log(err))
  },
}

export const getters = {
  item_doacao: (state) => {
    return state.list_item
  },
  ong: (state) => {
    return state.ong
  },
  ong: (state) => {
    return state.usuario
  },
  doacoes: (state) => {
    return state.list
  }
}
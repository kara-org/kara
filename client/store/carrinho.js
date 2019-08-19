export const state = () => ({
  ong: {},
  itensSelecionados: [],
})

export const mutations = {
  UPDATE_ONG (state, payload) {
    state.ong = payload
  },
  ADD_ITEM (state, item) {
    state.itensSelecionados.push(item)
  },
  REMOVE_ITEM (state, item) {
    state.itensSelecionados = state.itensSelecionados.filter(i => i.item.id !== item.id)
  }
}

export const actions = {
  fetchOng (context, idOng) {
    this.$OngService.show(idOng).then((payload) => {
      context.commit('UPDATE_ONG', payload)
    })
  },

  adicionarItemNoCarrinho (context, item) {
    context.commit('ADD_ITEM', item)
    context.commit('busca/REMOVE_RESULTADO', item.item, { root: true })
  },

  removerItemNoCarrinho (context, item) {
    context.commit('REMOVE_ITEM', item)
    context.commit('busca/ADD_RESULTADO', item, { root: true })
  },
}

export const getters = {
  isEmpty: (state) => {
    return state.itensSelecionados.length > 0
  },
  itensNoCarrinho: (state) =>{
    return state.itensSelecionados ? state.itensSelecionados.map(i => i.item) : []
  }
}

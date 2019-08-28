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
    state.itensSelecionados = state.itensSelecionados.filter(i => i.demanda.id !== item.id)
  },
}

export const actions = {
  fetchOng (context, idOng) {
    this.$OngService.show(idOng).then((payload) => {
      context.commit('UPDATE_ONG', payload)
    })
  },

  sendDoacao (context) {
    let doacao = {
      'item_doacao' : context.state.itensSelecionados.map( i => { return { "demanda": i.demanda.id, 'quantidade_prometida' : i.quantidade_prometida } }),
      'id_usuario' : context.rootState.auth.user.id,
      'data_agendamento': '2019-12-30'
    }

    this.$DoacaoService.create(doacao);
  },

  adicionarItemNoCarrinho (context, item) {
    context.commit('ADD_ITEM', item)
  },

  removerItemNoCarrinho (context, item) {
    context.commit('REMOVE_ITEM', item)
  },
}

export const getters = {
  isEmpty: (state) => {
    return state.itensSelecionados.length > 0
  },
  itensNoCarrinho: (state) => {
    return state.itensSelecionados ? state.itensSelecionados.map(i => i.demanda) : []
  },
  itensForaDoCarrinho: (state, getters) => {
    return state.ong.demandas.filter(x => ! getters.itensNoCarrinho.map(y => y.id).includes(x.id));
  }
}

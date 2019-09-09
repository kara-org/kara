export const state = () => ({
  ong: {
    demandas: []
  },
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
  ESVAZIAR_CARRINHO (state) {
    state.itensSelecionados = []
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
      'item_doacao' : context.state.itensSelecionados.map(item => {
        return {
          'id_demanda': item.demanda.id,
          'quantidade_prometida' : item.quantidade_prometida
        }
      }),
      'id_usuario' : context.rootState.auth.user.id,
      'data_agendamento': '2019-12-30'
    }

    return this.$DoacaoService.create(doacao).then(() => {
      context.commit('ESVAZIAR_CARRINHO')
    });
  },

  adicionarItemNoCarrinho (context, item) {
    if(context.state.itensSelecionados.map(i => i.id).includes(item.id)){
      return
    }
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
    return state.itensSelecionados || []
  },
  itensForaDoCarrinho: (state, getters) => {
    return state.ong.demandas.filter(x => ! getters.itensNoCarrinho.map(i => i.demanda.id).includes(x.id));
  }
}

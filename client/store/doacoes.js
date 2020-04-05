import DoacaoService from "../services/DoacaoService"

let serviceDoacao = new DoacaoService();

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

  SET_ITEM_DOACAO(state, { objectId, quantidadePrometida }) {
    state.list = state.list.map((d) => {
      d.demandas = state.list.map((i) => {
        if (i.objectId === objectId) {
          i.quantidadePrometida = quantidadePrometida
        }
        return i
      })
      return d
    })
  },

  ADD_DOACAO(state, payload) {
    state.list.push(payload)
  },

  ADD_ITEM_DOACAO(state, payload) {
    state.list_item.push(payload)
  },

  CANCELA_DOACAO(state, objectId) {
    state.list = state.list.forEach((d) => {
      if (d.objectId === objectId) {
        d = state.list.map((i) => {
          i.cancelado = true
          return i
        })
      }
    })
  },

  CANCELA_ITEM_DOACAO(state, objectId) {
    state.list = state.list.map((i) => {
      if (i.objectId === objectId)
        i.cancelado = true
      return i
    })
  },

  CONFIRMA_DOACAO(state, objectId) {
    state.list = state.list.forEach((d) => {
      if (d.objectId === objectId) {
        d = state.list.map((i) => {
          i.entregue = true
          return i
        })
      }
    })
  },

  CONFIRMA_ITEM_DOACAO(state, objectId) {
    state.list = state.list.forEach((d) => {
      d.demandas = d.demandas.map((i) => {
        if (i.objectId === objectId)
          i.entregue = true
        return i
      })
    })
  },
}

export const actions = {
  fetchDoacoesOng(context, objectId) {
    serviceDoacao.indexOng(objectId)
      .then((doacoes) => {
        context.commit('UPDATE_DOACOES', doacoes.map(doacao => doacao.toJSON()))
      })
      .catch((err) => console.log(err))
  },

  fetchDoacoesDoador(context, objectId) {
    serviceDoacao.indexDoador(objectId)
      .then((doacoes) => {
        context.commit('UPDATE_DOACOES', doacoes.map(doacao => doacao.toJSON()))
      })
      .catch((err) => console.log(err))
  },

  changeItemDoacao(context, { objectId, quantidadePrometida }) {
    serviceDoacao.updateItemDoacao({ objectId, quantidadePrometida })
      .then(/* (_) =>
        context.commit('SET_ITEM_DOACAO', { objectId, quantidadePrometida }) */)
      .catch((err) => console.log(err));
  },

  deleteItemDoacao(context, objectId) {
    serviceDoacao.setStatusItemDoacao({ objectId, cancelado: true })
      .then((_) => context.commit('CANCELA_ITEM_DOACAO', objectId))
      .catch((err) => console.log(err));
  },

  deleteDoacao(context, objectId) {
    serviceDoacao.setStatusDoacao({ objectId, cancelado: true })
      .then((_) =>
        context.commit('CANCELA_DOACAO', objectId))
      .catch((err) => console.log(err))
  },

  confirmaItemDoacao(context, { objectId, quantidadeEfetivada }) {
    serviceDoacao.setStatusItemDoacao({ objectId, entregue: true, quantidadeEfetivada })
      .then((_) =>
        context.commit('CONFIRMA_ITEM_DOACAO', objectId))
      .catch((err) => console.log(err))
  },

  confirmaDoacao(context, { objectId, quantidadeEfetivada }) {
    serviceDoacao.setStatusDoacao({ objectId, entregue: true, quantidadeEfetivada })
      .then((_) =>
        context.commit('CONFIRMA_DOACAO', objectId))
      .catch((err) => console.log(err))
  },
}

export const getters = {
  demandas: (state) => {
    return state.list_item
  },
  ong: (state) => {
    return state.ong
  },
  usuario: (state) => {
    return state.usuario
  },
  doacoes: (state) => {
    return state.list
  }
}

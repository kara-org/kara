import OngService from '../services/OngService';
import DoacaoService from '../services/DoacaoService';

let serviceOng = new OngService();
let serviceDoacao = new DoacaoService();

export const state = () => ({
  ong: {
    demandas: []
  },
  itensDisponiveis: [],
  itensSelecionados: []
});

export const mutations = {
  UPDATE_ONG(state, payload) {
    state.ong = payload;
  },
  ADD_ITEM(state, item) {
    state.itensSelecionados.push(item);
  },
  REMOVE_ITEM(state, item) {
    state.itensSelecionados = state.itensSelecionados.filter(
      i => i.demanda.objectId !== item.objectId
    );
  },
  UPDATE_ITEM(state, payload) {
    state.itensSelecionados.forEach((element, index) => {
      if (element.demanda.objectId == payload.demanda.objectId) {
        state.itensSelecionados[index].quantidadePrometida =
          payload.quantidadePrometida;
      }
    });
  },
  UPDATE_ITENS_FORA(state, payload) {
    state.itensDisponiveis = payload;
  },
  ESVAZIAR_CARRINHO(state) {
    state.itensSelecionados = [];
  }
};

export const actions = {
  async fetchOng(context, idOng) {
    return serviceOng.show(idOng).then(ong => {
      context.commit('UPDATE_ONG', ong.toJSON());
    });
  },

  fetchItens(context, payload) {
    context.commit('UPDATE_ITENS_FORA', payload);
  },

  async sendDoacao(context) {
    let itensDoacao = context.state.itensSelecionados.map(item => {
      return {
        demanda: item.demanda,
        quantidadePrometida: item.quantidadePrometida,
        quantidadeEfetivada: item.quantidadeEfetivada
      };
    });

    return serviceDoacao.create(itensDoacao).then(() => {
      context.commit('ESVAZIAR_CARRINHO');
    });
  },

  adicionarItemNoCarrinho(context, item) {
    for (const itemSelecionado of context.state.itensSelecionados) {
      if (itemSelecionado.demanda.objectId === item.objectId) {
        return;
      }
    }
    context.commit('ADD_ITEM', item);
  },

  alterarItemNoCarrinho(context, item) {
    context.commit('UPDATE_ITEM', item);
  },

  removerItemNoCarrinho(context, item) {
    context.commit('REMOVE_ITEM', item);
  },

  limparCarrinho(context) {
    context.commit('ESVAZIAR_CARRINHO');
  }
};

export const getters = {
  isEmpty: state => {
    return state.itensSelecionados.length > 0;
  },
  itensNoCarrinho: state => {
    return state.itensSelecionados || [];
  },
  itensForaDoCarrinho: (state, getters) => {
    return (
      state.itensDisponiveis &&
      state.itensDisponiveis.filter(
        x =>
          !getters.itensNoCarrinho
            .map(i => i.demanda.objectId)
            .includes(x.objectId)
      )
    );
  },
  ong: state => {
    return state.ong;
  }
};

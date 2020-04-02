import DemandaService from '../services/DemandaService';

let serviceDemanda = new DemandaService();

export const state = () => ({
  ongSelecionada: {},
  list: [],
  demanda: {}
});

export const mutations = {
  UPDATE_ONG(state, payload) {
    state.ongSelecionada = payload;
  },
  UPDATE_DEMANDAS(state, payload) {
    state.list = payload;
  },
  SET_DEMANDA(state, demanda) {
    state.list = state.list.map(i => {
      if (i.id === demanda.id) {
        i.data_fim = demanda.data_fim;
        i.data_inicio = demanda.data_inicio;
        i.descricao = demanda.descricao;
        i.quantidade_solicitada = demanda.quantidade_solicitada;
      }
      return i;
    });
  },
  ADD_DEMANDA(state, payload) {
    state.list.push(payload);
  },
  INATIVA_DEMANDA(state, demanda) {
    state.list = state.list.map(i => {
      if (i.id === demanda.id) {
        i.ativo = false;
      }
      return i;
    });
  }
};

export const actions = {
  async createDemanda(
    { commit },
    { nome, quantidadeDesejada, categoria, ong }
  ) {
    return await serviceDemanda
      .create({
        nome,
        quantidadeDesejada,
        categoria,
        ong
      })
      .then(demanda => commit('ADD_DEMANDA', demanda));
  },

  fetchDemandas(context) {
    serviceDemanda
      .index()
      .then(demandas => context.commit('UPDATE_DEMANDAS', demandas))
      .catch(err => console.log(err));
  },

  fetchDemandasOng(context, idOng) {
    serviceDemanda
      .indexOng({ idOng })
      .then(demandas => context.commit('UPDATE_DEMANDAS', demandas))
      .catch(err => console.log(err));
  },

  changeDemanda(_, id, payload) {},

  deleteDemanda(context, id) {}
};

export const getters = {
  demanda: state => {
    return state.demanda;
  },
  demandas: state => {
    return state.list;
  }
};

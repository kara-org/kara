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
    state.demanda = demanda;
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
    return serviceDemanda
      .create({
        nome,
        quantidadeDesejada,
        categoria,
        ong
      })
      .then(demanda => commit('ADD_DEMANDA', demanda));
  },

  async fetchDemandas(context) {
    return serviceDemanda
      .index()
      .then(demandas => {
        let demandasJson = demandas.map(demanda => demanda.toJSON());
        context.commit('UPDATE_DEMANDAS', demandasJson);
      })
      .catch(err => console.log(err));
  },

  async fetchDemanda(context, id) {
    return serviceDemanda.show(id)
      .then(demanda => {
        context.commit('SET_DEMANDA', demanda.toJSON());
      })
      .catch(err => console.log(err));
  },

  async fetchDemandasOng(context, idOng) {
    return serviceDemanda
      .indexOng({ idOng })
      .then(demandas => {
        let demandasJson = demandas.map(demanda => demanda.toJSON());
        context.commit('UPDATE_DEMANDAS', demandasJson);
      })
      .catch(err => console.log(err));
  },

  deleteDemanda(_, id, payload) {},

  async updateDemanda(
    { commit },
    { objectId, nome, quantidadeAlcancada, quantidadeDesejada, categoria, ativo, ong }
  ) {


    return serviceDemanda.update({
      objectId,
      nome,
      quantidadeDesejada,
      quantidadeAlcancada,
      categoria,
      ativo,
      ong
    })
    // .then(demanda => commit('ADD_DEMANDA', demanda));
  },

  async inativaAtiva(
    { commit },
    { objectId, nome, quantidadeAlcancada, quantidadeDesejada, categoria, ativo, ong }
  ) {

    ativo = !ativo;

    return serviceDemanda.update({
      objectId,
      nome,
      quantidadeDesejada,
      quantidadeAlcancada,
      categoria,
      ativo,
      ong
    })
    // .then(demanda => commit('ADD_DEMANDA', demanda));
  }


};

export const getters = {
  demanda: state => {
    return state.demanda;
  },
  demandas: state => {
    return state.list;
  }
};

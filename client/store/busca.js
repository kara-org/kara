import DemandaService from '../services/DemandaService';
import BuscarService from '../services/BuscarService';
import OngService from '../services/OngService';

let serviceBuscar = new BuscarService();
let serviceDemanda = new DemandaService();
let serviceOng = new OngService();

export const state = () => ({
  list: [],
  default: [],
  searchTerm: '',
  tipo: ''
});

export const mutations = {
  ORDER_ITENS(state) {
    state.list.sort((a, b) => a.nome.localeCompare(b.nome));
  },
  UPDATE_TIPO(state, payload) {
    state.tipo = payload;
  },
  UPDATE_SEARCH_TERM(state, payload) {
    state.searchTerm = payload;
  },
  UPDATE_RESULTADOS(state, payload) {
    state.list = payload;
  },
  TO_DEFEAULT_RESULTADOS(state) {
    state.list = state.default;
  },
  SET_DEFEAULT_RESULTADOS(state, payload) {
    state.default = payload;
  }
};

export const actions = {
  async buscar({ commit, dispatch }, { tipo, palavraChave }) {
    commit('UPDATE_SEARCH_TERM', palavraChave);
    return await serviceBuscar.buscar(palavraChave).then(items => {
      if (items.length !== 0) {
        commit('UPDATE_RESULTADOS', items);
      } else {
        commit('TO_DEFEAULT_RESULTADOS');
      }
      commit('ORDER_ITENS');
    });
  },
  async fetchBusca({ commit, dispatch }, tipo) {
    return await serviceDemanda
      .index()
      .then(demandas => {
        let demandasJson = demandas.map(demanda => demanda.toJSON())
        demandasJson = demandasJson.filter(demanda => demanda.ativo)
        serviceBuscar.indexAdd(demandasJson);
        commit('UPDATE_RESULTADOS', demandasJson);
        commit('SET_DEFEAULT_RESULTADOS', demandasJson);
        commit('ORDER_ITENS');
      })
      .catch(err => {
        console.log(err);
        dispatch('global/addErro', err, { root: true });
      })
      .then(() => dispatch('global/stopLoading', null, { root: true }));
  },

  async fetchBuscaOng({ commit, dispatch }, tipo) {
    return await serviceOng
      .index()
      .then(ongs => {
        let ongsJson = ongs.map(ong => ong.toJSON())
        ongsJson = ongsJson.filter(ong => ong.ativo)
        serviceBuscar.indexAdd(ongsJson);
        commit('UPDATE_RESULTADOS', ongsJson);
        commit('SET_DEFEAULT_RESULTADOS', ongsJson);
        commit('ORDER_ITENS');
      })
      .catch(err => {
        console.log(err);
        dispatch('global/addErro', err, { root: true });
      })
      .then(() => dispatch('global/stopLoading', null, { root: true }));
  }
};

export const getters = {
  demandasPorOng: state => idOng => {
    return state.default.filter(i => i.ong.objectId === idOng);
  },
  list: state => {
    return state.list;
  },
  searchTerm: state => {
    return state.searchTerm;
  }
};

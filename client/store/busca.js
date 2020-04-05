import DemandaService from "../services/DemandaService"
import BuscarService from "../services/BuscarService"

let serviceBuscar = new BuscarService();
let serviceDemanda = new DemandaService();

export const state = () => ({
  list: [],
  default: [],
  searchTerm: '',
  tipo: ''
})

export const mutations = {
  ORDER_ITENS(state){
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
}

export const actions = {
  async buscar({ commit, dispatch }, { tipo, palavraChave }) {
    commit('UPDATE_SEARCH_TERM', palavraChave);
    return await serviceBuscar.buscar(palavraChave).then(demandas => {
      if (demandas.length !== 0) {
        commit('UPDATE_RESULTADOS', demandas);
      } else {
        commit('TO_DEFEAULT_RESULTADOS');
      }
      commit('ORDER_ITENS');
    })
  },
  async fetchBusca({ commit, dispatch }, tipo) {
    return await serviceDemanda.index()
      .then(demandas => {
        let demandasJson = demandas.map(demanda => demanda.toJSON())
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
  }
}

export const getters = {
  demandasPorOng: (state) => idOng => {
    return state.default.filter(i => i.ong.objectId === idOng);
  },
}

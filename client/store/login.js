import LoginService from '../services/LoginService';

let serviceUser = new LoginService();

export const state = () => ({
  usuario: null
});

export const mutations = {
  SET(state, user) {
    state.usuario = user;
  }
};

export const actions = {
  async login({ commit }, { login, senha }) {
    return serviceUser.login(login, senha).then(response => commit('SET', response.toJSON()));
  },

  async signUp(_, { email, password, nome, telefones }) {
    return serviceUser.signUp(email, password, nome, telefones);
  },

  async update({ commit }, { email, nome, telefones }) {
    return serviceUser.update(email, nome, telefones).then(response => commit('SET', response.toJSON()));
  },

  async logout({ commit }) {
    return serviceUser.logout().then(() => commit('SET', null));
  },
  async resetPassword(_, email) {
    return serviceUser.resetPassword(email);
  },

  async fetch({ commit }) {
    let user = await serviceUser.currentUser();
    commit('SET', user);
  }
};

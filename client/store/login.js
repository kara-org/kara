import UserService from '../services/UserService';
import OngService from '../services/OngService';

let serviceUser = new UserService();
let serviceOng = new OngService();

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
    return serviceUser
      .login(login, senha)
      .then(user => commit('SET', user.toJSON()));
  },

  async signUp(_, { email, password, nome, telefones }) {
    return serviceUser.signUp(email, password, nome, telefones);
  },

  async signUpOng(_, { email, password, nome, telefones, nomeDaOng }) {
    let ong = serviceOng.build({ nomeDaOng });
    return serviceUser
      .signUp(email, password, nome, telefones, ong)
      .then(user => commit('SET', user.toJSON()));
  },

  async update({ commit }, { email, nome, telefones }) {
    return serviceUser
      .update(email, nome, telefones)
      .then(user => commit('SET', user.toJSON()));
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

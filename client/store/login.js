import UserService from '../services/UserService';
import OngService from '../services/OngService';

let serviceUser = new UserService();
let serviceOng = new OngService();

let usuarioDefaut = {
  nome: '',
  email: '',
  telefones: [null],
  ong: {
    nome: ' ',
    objectId: ''
  }
};

export const state = () => ({
  usuario: usuarioDefaut
});

export const mutations = {
  SET(state, user) {
    state.usuario = user;
  },
  SET_ONG(state, ong) {
    state.usuario.ong = ong;
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

  async signUpOng({ commit }, { email, password, nome, telefones, nomeDaOng, biografia, linkParaContato, fotoDoPerfil }) {
    let ong = await serviceOng.build({ nomeDaOng, email, telefones, biografia, linkParaContato, fotoDoPerfil });
    return serviceUser
      .signUp(email, password, nome, telefones, ong)
      .then(user => commit('SET', user.toJSON()));
  },

  async update({ commit }, { email, nome, telefones }) {
    return serviceUser
      .update(email, nome, telefones)
      .then(user => commit('SET', user.toJSON()));
  },
  
  async updateOng({ commit }, { objectId, nomeDaOng, email, telefones, biografia, linkParaContato, fotoDoPerfil }) {
    return serviceOng
      .update({objectId, nomeDaOng, email, telefones, biografia, linkParaContato, fotoDoPerfil})
      .then(ong => commit('SET_ONG', ong.toJSON()));
  },

  async logout({ commit }) {
    return serviceUser.logout().then(() => commit('SET', usuarioDefaut));
  },

  async resetPassword(_, email) {
    return serviceUser.resetPassword(email);
  },

  async fetch({ commit }) {
    let user = await serviceUser.currentUser();
    commit('SET', user);
  }
};

export const getters = {
  isAuthenticated: state => {
    return state.usuario && state.usuario.email != '';
  },
  isDoador: state => {
    return !(state.usuario.ong && state.usuario.ong.objectId != '');
  },
  usuario: state => {
    return state.usuario;
  },
  ong: state => {
    return state.usuario.ong;
  }
};

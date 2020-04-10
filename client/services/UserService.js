let Parse = require('parse');

export default class UserService {
  async login(username, password) {
    let response = await Parse.User.logIn(username, password);
    await response.fetchWithInclude('ong');
    return response;
  }

  async signUp(email, password, nome, telefones, ong) {
    let response;
    if (ong) {
      response = Parse.User.signUp(email, password, {
        email: email,
        nome: nome,
        telefones: telefones,
        ong: ong
      });
      return response;
    }

    response = Parse.User.signUp(email, password, {
      email: email,
      nome: nome,
      telefones: telefones
    });

    return response;
  }

  async update(email, nome, telefones) {
    let currentUser = Parse.User.current();

    currentUser.setEmail(email);
    currentUser.set('nome', nome);
    currentUser.set('telefones', telefones);

    currentUser.save();
    currentUser.fetch();
    return currentUser;
  }

  async resetPassword(email) {
    return Parse.User.requestPasswordReset(email);
  }

  async currentUser() {
    let user = Parse.User.current();
    return user.toJSON();
  }

  async logout() {
    let response = Parse.User.logOut();
    return response;
  }
}

let Parse = require('parse');

export default class UserService {
  async login(username, password) {
    var response = Parse.User.logIn(username, password);
    return response;
  }

  async signUp(email, password, nome, telefones) {
    var response = Parse.User.signUp(email, password, { email: email, nome: nome, telefones: telefones });
    return response;
  }

  async update(email, nome, telefones) {
    var currentUser = Parse.User.current();

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
    var response = Parse.User.logOut();
    return response;
  }
}

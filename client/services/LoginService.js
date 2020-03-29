let Parse = require('parse');

export default class UserService {
  async login(username, password) {
    var response = Parse.User.logIn(username, password);
    return response;
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

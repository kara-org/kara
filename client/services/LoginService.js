let Parse = require('parse');

export default class UserService {
  async login(username, password) {
    var response = Parse.User.logIn(username, password);
    return response;
  }

  async resetPassword(email) {
    Parse.User.requestPasswordReset(email)
      .then(function() {
        console.log('Password reset request was sent successfully');
      })
      .catch(function(error) {
        console.log(
          'The login failed with error: ' + error.code + ' ' + error.message
        );
      });
  }

  async currentUser() {
    let user = Parse.User.current();
    return user.toJSON();
  }
}

export default $auth => () => ({

  login (email, password) {
    return $auth.loginWith('local', {
      data: {
        email: email,
        password: password
      }
    });
  }
});


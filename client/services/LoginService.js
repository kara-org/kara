export default $auth => $toast => ({

  login (email, password) {
    return $auth.loginWith('local', {
      data: {
        email: email,
        password: password
      }
    })
  }
})


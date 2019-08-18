export default {
  namespaced: true,
  state() {
    return {
      auth: {
        loggedIn: {},
        user: {},
      },
    }
  }
  /* getters: {
    isAuthenticated(state) {
      if (state.auth)
      return state.auth.loggedIn
    },

    loggedInUser(state) {
      if (state.auth)
      return state.auth.user
    },
  }, */
}
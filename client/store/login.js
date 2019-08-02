export const getters = {
    isAuthenticated(state) {
      console.log(state.auth)
      if (!state.auth) return false
      return state.auth.loggedIn
    },

    loggedInUser(state) {
      if (!state.auth) return false
      return state.auth.user
    }
}

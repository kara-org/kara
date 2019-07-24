import createServiceLogin from '~/services/LoginService'

export default function ({ app }, inject) {
  const serviceLogin = createServiceLogin(app.$auth)

  inject('LoginService', serviceLogin(app.$toast))

}

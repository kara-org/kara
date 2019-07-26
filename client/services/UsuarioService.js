export default $axios => resource => ({
  get(id) {
    return $axios.$get(`usuario/${id}`)
  },
  create(payload) {
    return $axios.$post('usuario/', payload)
  },
  changeStatus(id, status) {
    usuario.ativo = status
    return $axios.$patch(`usuario/${id}`, usuario)
  }
})

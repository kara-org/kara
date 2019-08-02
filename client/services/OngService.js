export default $axios => resource => ({
  get(id) {
    return $axios.$get(`ong/${id}`)
  },
  create(payload) {
    return $axios.$post('ong/', payload)
  },
})

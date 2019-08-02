export default $axios => resource => ({

  index() {
    return $axios.$get(resource)
  },

  create(payload) {
    return $axios.$post(resource, payload)
  },

  show(id) {
    return $axios.$get(`/${resource}/${id}`)
  },


  update(payload) {
    return $axios.$put(`${resource}`, payload)
  },

  delete(id) {
    return $axios.$delete(`/${resource}/${id}`)
  },

  getResource () {
    return resource
  },
  getAxios () {
    return $axios
  },

})


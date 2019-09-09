export default ({ $axios, $store }) => resource => ({
  async index() {
    return await $axios
      .$get(resource)
      // .catch(err => {
      //   dispatch('global/addErro', err, { root: true })
      // })
      // .then(() => dispatch('global/stopLoading', null, { root: true }))
  },

  async create(payload) {
    return await $axios.$post(resource, payload)
  },

  async show(id) {
    return await $axios.$get(`${resource}${id}`)
  },

  async update(id, payload) {
    return await $axios.$patch(`${resource}${id}/`, payload)
  },

  async delete(id) {
    return await $axios.$delete(`${resource}${id}/`)
  },

  getResource() {
    return resource
  },
  getAxios() {
    return $axios
  }
})

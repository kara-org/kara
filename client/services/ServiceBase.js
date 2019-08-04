import { nextTick } from 'q'

export default $axios => resource => ({
  async index() {
    return await $axios.$get(resource).catch(err => {
      dispatch('global/addErro', err, { root: true })
    }).then( () => dispatch('global/stopLoading', null, { root: true }))
  },

  create(payload) {
    return $axios.$post(resource, payload).catch(err => {
      dispatch('global/addErro', err, { root: true })
    })
  },

  show(id) {
    return $axios.$get(`/${resource}/${id}`).catch(err => {
      dispatch('global/addErro', err, { root: true })
    })
  },

  update(payload) {
    return $axios.$put(`${resource}`, payload).catch(err => {
      dispatch('global/addErro', err, { root: true })
    })
  },

  delete(id) {
    return $axios.$delete(`/${resource}/${id}`).catch(err => {
      dispatch('global/addErro', err, { root: true })
    })
  },

  getResource() {
    return resource
  },
  getAxios() {
    return $axios
  }
})

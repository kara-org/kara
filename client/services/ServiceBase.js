export default ({ $axios, $store }) => resource => ({
  async index() {
    return await $axios.$get(resource).then((response) => {
      return response.data;
    });
  },

  async create(payload) {
    return await $axios.$post(resource, payload);
  },

  async show(id) {
    return await $axios.$get(`${resource}${id}`).then((response) => {
      return response.data;
    });
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

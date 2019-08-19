export default $axios => resource => ({
  index (id) {
    return $axios.$get(`/ong/${id}/demandas/`)
  },
  create(id, payload) {
    return $axios.$post(`/ong/${id}/demandas/`, payload)
  },
  change(id, payload) {
    return $axios.$patch(`/demanda/${id}`, payload)
  }
})

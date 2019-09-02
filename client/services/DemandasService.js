export default $axios => resource => ({
  getDemandasOng(idComposer) {
    return $axios.$get(`ong/${idComposer}${resource}`)
  },
  create(idComposer, payload) {
    return $axios.$post(`${resource}/ong/${idComposer}/demandas/`, payload)
  },
  change(id, payload) {
    return $axios.$patch(`${resource}/demanda/${id}/`, payload)
  },
  delete(id) {
    return $axios.$delete(`${resource}/demanda/${id}/cancelar`)
  }
})

export default $axios => resource => ({
  index (idComposer) {
    return $axios.$get(`${resource}${idComposer}/doacoes/`).then((response) => {
      return response.data;
    });
  },
  create(idComposer, payload) {
    return $axios.$post(`${resource}${idComposer}/doacao/`, payload);
  },
  changeStatus(idComposer, id, status) {
    doacao.status = status;
    return $axios.$patch(`${resource}${idComposer}/doacao/${id}`, doacao);
  }
});

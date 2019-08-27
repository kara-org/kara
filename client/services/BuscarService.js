import data from '../store/fake/demandas'
import Flexsearch from "flexsearch";
import { nextTick } from 'q';

let index = new Flexsearch({
    encode: "extra",
    tokenize: "full",
    threshold: 1,
    resolution: 3,
    doc: {
      id: "id",
      field: "descricao"
    }
});

// this.index.add(JSON.parse(JSON.stringify( this.$store.state.busca.list)))

export default $axios => ({
  async buscar(palavraChave) {
    if (index === null || palavraChave.length < 2) return [];
    return await index.search({
      query: palavraChave,
      limit: 10
    });
  },
  async fetch(tipo) {
    return await $axios.$get(`/busca/${tipo}`)
      .then(response => { index.add(response); return (response) });
  },

  getResource () {
    return resource
  },
  getAxios () {
    return $axios
  },

})


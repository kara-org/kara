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
    field: "titulo"
  }
});

// this.index.add(JSON.parse(JSON.stringify( this.$store.state.busca.list)))

export default $axios => ({

  async buscar(palavraChave) {
    console.log(index)
    if (index === null || palavraChave.length < 2) return [];
    return await index.search({
      query: palavraChave,
      limit: 10
    });
  },
  async fetch(params) {
    // return new Promise(function(resolve){
    //   resolve(data)
    // }).then(response => { index.add(response); console.log(index); return (response) })
    return await $axios.$get('/buscar', { params: params });
  },

  getResource () {
    return resource
  },
  getAxios () {
    return $axios
  },

})


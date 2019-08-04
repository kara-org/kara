import data from '../store/fake/demandas'
import { resolve } from 'url';

export default $axios => ({

  async buscar(params) {
    return new Promise(function(resolve){
      resolve(data)
    })
    // return await $axios.$get('/buscar', { params: params });
  },

  getResource () {
    return resource
  },
  getAxios () {
    return $axios
  },

})


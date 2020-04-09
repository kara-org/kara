import data from '../store/fake/demandas';
import Flexsearch from 'flexsearch';
import { nextTick } from 'q';

let index = new Flexsearch({
  encode: 'extra',
  tokenize: 'full',
  threshold: 1,
  resolution: 3,
  doc: {
    id: 'objectId',
    field: 'nome'
  }
});

export default class BuscarService {
  async buscar(palavraChave) {
    if (index === null || palavraChave.length < 2) return [];
    return await index.search({
      query: palavraChave,
      limit: 10
    });
  }

  async indexAdd(data) {
    return index.add(data);
  }
}

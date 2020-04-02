let Parse = require('parse');

const Demanda = Parse.Object.extend('Demanda');

export default class DemandaService {
  async index() {
    let query = new Parse.Query(Demanda);
    return await query.find();
  }

  async indexOng({ idOng }) {
    const Ong = Parse.Object.extend('Ong');
    let ong = new Ong();
    ong.id = idOng;

    let query = new Parse.Query(Demanda);
    query.equalTo('ong', ong);
    return await query.find();
  }

  async create({ nome, quantidadeDesejada, categoria, ong }) {
    const demanda = this.build({ nome, quantidadeDesejada, categoria, ong });
    return await demanda.save();
  }

  async show(id) {
    return await query.include('ong').get(id);
  }

  async update({
    id,
    nome,
    quantidadeAlcancada,
    quantidadeDesejada,
    categoria,
    ativo
  }) {
    const demanda = Parse.Object.createWithoutData(id);
    demanda.set('nome', nome);
    demanda.set('quantidadeAlcancada', quantidadeAlcancada);
    demanda.set('quantidadeDesejada', quantidadeDesejada);
    demanda.set('categoria', categoria);
    demanda.set('ativo', ativo);
    demanda.set('ong', ong);
    await demanda.save();
    return await demanda.fetch();
  }

  async delete(id) {
    const demanda = Parse.Object.createWithoutData(id);
    return demanda.destroy();
  }

  build({
    nome,
    quantidadeDesejada,
    categoria,
    ong,
    ativo,
    quantidadeAlcancada
  }) {
    quantidadeAlcancada = quantidadeAlcancada || 0;
    ativo = ativo || true;

    const demanda = new Demanda();

    demanda.set('nome', nome);
    demanda.set('quantidadeAlcancada', quantidadeAlcancada);
    demanda.set('quantidadeDesejada', quantidadeDesejada);
    demanda.set('categoria', categoria);
    demanda.set('ativo', ativo);
    demanda.set('ong', ong);

    return demanda;
  }
}

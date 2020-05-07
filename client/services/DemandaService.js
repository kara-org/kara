let Parse = require('parse');

const Demanda = Parse.Object.extend('Demanda');

export default class DemandaService {
  async index() {
    let query = new Parse.Query(Demanda);
    query.include('ong');
    return await query.find();
  }

  async indexOng({ idOng }) {
    let ong;
    // if (!idOng) ong = Parse.User.current().get('ong');
    // else {
    const Ong = Parse.Object.extend('Ong');
    ong = new Ong();
    ong.id = idOng;
    // }

    let query = new Parse.Query(Demanda);
    query.equalTo('ong', ong);
    return await query.find();
  }

  async create({ nome, quantidadeDesejada, categoria, ong }) {
    const demanda = this.build({ nome, quantidadeDesejada, categoria, ong });
    return await demanda.save();
  }

  async show(id) {
    let query = new Parse.Query(Demanda);
    return await query.include('ong').get(id);
  }

  async update({
    objectId,
    nome,
    quantidadeDesejada,
    quantidadeAlcancada,
    categoria,
    ativo,
    ong
  }) {
    let query = new Parse.Query(Demanda);
    let demanda = new Demanda();
    demanda.set('objectId', objectId);
    demanda.set('nome', nome);
    demanda.set('quantidadeAlcancada', quantidadeAlcancada);
    demanda.set('quantidadeDesejada', quantidadeDesejada);
    demanda.set('categoria', categoria);
    demanda.set('ativo', ativo);
    return demanda.save();
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

    if (ong) {
      let Ong = Parse.Object.extend('Ong');
      let ongPoint = Ong.createWithoutData(ong.objectId);
      demanda.set('ong', ongPoint);
    }

    return demanda;
  }
}

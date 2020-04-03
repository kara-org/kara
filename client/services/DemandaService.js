let Parse = require('parse');

const Demanda = Parse.Object.extend('Demanda');

export default class DemandaService {
  async index() {
    let query = new Parse.Query(Demanda);
    query.include("ong");
    return await query.find();
  }

  async indexOng({ idOng }) {
    let ong;
    if (!idOng)
      ong = Parse.User.current().currentUser.get('ong');
    else {
      const Ong = Parse.Object.extend('Ong');
      ong = new Ong();
      ong.id = idOng;
    }

    let query = new Parse.Query(Demanda);
    query.equalTo('ong', ong);
    return await query.get();
  }

  async create({ nome, quantidadeDesejada, categoria, ong }) {
    const demanda = this.build({ nome, quantidadeDesejada, categoria, ong });
    return await demanda.save();
  }

  async show(id) {
    return await query.include('ong').get(id).toJSON();
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

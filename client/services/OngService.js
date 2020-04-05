let Parse = require('parse');

const Ong = Parse.Object.extend('Ong');

export default class OngService {
  async index() {
    let query = new Parse.Query(Ong);
    return await query.find();
  }

  async create({ nome }) {
    let ong = build({ nome });
    return await ong.save();
  }

  async show(id) {
    let query = new Parse.Query(Ong);
    return await query.get(id);
  }

  async update({ id, nome }) {
    const ong = Parse.Object.createWithoutData(id);
    ong.set('nome', nome);
    await ong.save();
    return await ong.fetch();
  }

  async delete(id) {
    const ong = Parse.Object.createWithoutData(id);
    return ong.destroy();
  }

  build({ nome }) {
    const ong = new Ong();
    ong.set('nome', nome);
    return ong;
  }
}

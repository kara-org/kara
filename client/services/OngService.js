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

  async update({
    objectId,
    nomeDaOng,
    biografia,
    linkParaContato,
    fotoDoPerfil
  }) {
    const ong = Parse.Object.createWithoutData(objectId);
    ong.set('nome', nomeDaOng);
    ong.set('biografia', biografia);
    ong.set('linkParaContato', linkParaContato);

    if (fotoDoPerfil && !fotoDoPerfil.url) {
      var fotoBase64 = await this.readFileAsDataURL(fotoDoPerfil);
      var file = new Parse.File(fotoDoPerfil.name, { base64: fotoBase64 });
      ong.set('fotoDoPerfil', file);
    }

    await ong.save();
    return await ong.fetch();
  }

  async delete(id) {
    const ong = Parse.Object.createWithoutData(id);
    return ong.destroy();
  }

  async build({
    nomeDaOng,
    email,
    telefones,
    biografia,
    linkParaContato,
    fotoDoPerfil
  }) {
    var fotoBase64 = await this.readFileAsDataURL(fotoDoPerfil);
    var file = new Parse.File(fotoDoPerfil.name, { base64: fotoBase64 });

    const ong = new Ong();
    ong.set('nome', nomeDaOng);
    ong.set('email', email);
    ong.set('telefones', telefones);
    ong.set('biografia', biografia);
    ong.set('linkParaContato', linkParaContato);
    ong.set('fotoDoPerfil', file);
    return ong;
  }

  async readFileAsDataURL(inputFile) {
    const reader = new FileReader();

    return new Promise((resolve, reject) => {
      reader.onerror = () => {
        reader.abort();
        reject(new DOMException('Erro ao converter arquivo.'));
      };

      reader.onload = () => {
        resolve(reader.result);
      };
      reader.readAsDataURL(inputFile);
    });
  }
}

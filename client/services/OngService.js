let Parse = require('parse');

const Ong = Parse.Object.extend('Ong');

export default class OngService {
  async index() {
    let query = new Parse.Query(Ong);
    return await query.find();
  }

  async create({ nome }) {
    let ong = await build({ nome });
    return await ong.save();
  }

  async show(id) {
    let query = new Parse.Query(Ong);
    return await query.get(id);
  }

  async showBySlug(slug) {
    let query = new Parse.Query(Ong);
    query.equalTo("slug", slug)
    return await query.first();
  }

  async update({
    objectId,
    nomeDaOng,
    email,
    telefones,
    biografia,
    linkParaContato,
    fotoDoPerfil
  }) {
    const ong = await this.build({
      objectId,
      nomeDaOng,
      email,
      telefones,
      biografia,
      linkParaContato,
      fotoDoPerfil
    });

    await ong.save();
    return await ong.fetch();
  }

  async delete(id) {
    const ong = Parse.Object.createWithoutData(id);
    return ong.destroy();
  }

  async build({
    objectId,
    nomeDaOng,
    email,
    telefones,
    biografia,
    linkParaContato,
    fotoDoPerfil
  }) {
    let ong = new Ong();

    let slug = convertToSlug(nomeDaOng);

    if (fotoDoPerfil && !fotoDoPerfil.url) {
      let fotoBase64 = await this.readFileAsDataURL(fotoDoPerfil);
      let file = new Parse.File(fotoDoPerfil.name, { base64: fotoBase64 });
      ong.set('fotoDoPerfil', file);
    }

    if (objectId && objectId != '') ong.set('objectId', objectId);
    if (nomeDaOng && nomeDaOng != '') ong.set('nome', nomeDaOng);
    if (email && email != '') ong.set('email', email);
    if (telefones && telefones[0] && telefones[0] != '')
      ong.set('telefones', telefones);
    if (biografia && biografia != '') ong.set('biografia', biografia);
    if (linkParaContato && linkParaContato != '')
      ong.set('linkParaContato', linkParaContato);

    if (slug && slug != '') ong.set('slug', slug);

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

  convertToSlug(Text) {
    return Text.toLowerCase()
      .replace(/ /g, '-')
      .replace(/[^\w-]+/g, '');
  }
}

let Parse = require('parse');

const Doacao = Parse.Object.extend('Doacao');
const ItemDoacao = Parse.Object.extend('ItemDoacao');
const Ong = Parse.Object.extend('Ong');
const Demanda = Parse.Object.extend('Demanda');

export default class DoacaoService {
  async index() {
    let query = new Parse.Query(Doacao);
    query.include('ong');
    query.include('user');
    query.include('demandas');
    return await query.find();
  }

  async indexOng({ idOng }) {
    let ong;
    if (!idOng)
      ong = Parse.User.current().get('ong');
    else {
      ong = new Ong();
      ong.objectId = idOng;
    }

    let query = new Parse.Query(Doacao);
    query.equalTo('ong', ong);
    query.include('ong');
    query.include('user');
    query.include('demandas');
    return await query.find();
  }

  async indexDoador() {
    let user = Parse.User.current();

    let query = new Parse.Query(Doacao);
    query.equalTo('user', user);
    query.include('ong');
    query.include('user');
    query.include('demandas');
    return await query.find();
  }

  async create(itensDoacao) {
    let demandas = [];
    let user = Parse.User.current();

    let ong = new Ong();
    ong.set('objectId', itensDoacao[0].demanda.ong.objectId)

    itensDoacao.forEach(item => {
      demandas.push(this.buildItemDoacao({ demanda: item.demanda, quantidadePrometida: item.quantidadePrometida, quantidadeEfetivada: item.quantidadeEfetivada }))
    });
    const doacao = this.build({ ong, user, demandas });
    return await doacao.save();
  }

  async show(objectId) {
    let query = new Parse.Query(Doacao);
    return await query.includeAll().get(objectId).toJSON();
  }

  async updateItemDoacao({
    objectId,
    quantidadePrometida
  }) {

    const itemDoacao = new ItemDoacao();
    itemDoacao.set('objectId', objectId)
    itemDoacao.set('quantidadePrometida', quantidadePrometida);

    await itemDoacao.save();
    return await itemDoacao.fetch();
  }

  async setStatusItemDoacao({ objectId, entregue, quantidadeEfetivada, cancelado }) {
    const itemDoacao = new ItemDoacao();

    itemDoacao.set('objectId', objectId);

    if (entregue) {
      itemDoacao.set('entregue', entregue);
      itemDoacao.set('quantidadeEfetivada', quantidadeEfetivada);
    }
    if (cancelado) {
      itemDoacao.set('cancelado', cancelado);
    }

    await itemDoacao.save();
    return await itemDoacao.fetch();
  }

  async setStatusDoacao({ objectId, entregue, cancelado }) {
    const doacao = new Doacao();

    doacao.set('objectId', objectId);

    if (entregue) {
      doacao.set('entregue', entregue);
    }
    if (cancelado) {
      doacao.set('cancelado', cancelado);
    }

    await doacao.save();
    return await doacao.fetch();
  }

  build({ ong, user, demandas }) {

    const doacao = new Doacao();

    doacao.set('ong', ong);
    doacao.set('user', user);
    doacao.set('demandas', demandas);

    return doacao;
  }

  buildItemDoacao({ demanda, quantidadePrometida, quantidadeEfetivada }) {
    quantidadeEfetivada = quantidadeEfetivada || 0;

    const itemDoacao = new ItemDoacao();
    let pDemanda = new Demanda();
    pDemanda.set('objectId', demanda.objectId)

    itemDoacao.set('demanda', pDemanda);
    itemDoacao.set('quantidadePrometida', quantidadePrometida);
    itemDoacao.set('quantidadeEfetivada', quantidadeEfetivada);

    return itemDoacao;
  }
}
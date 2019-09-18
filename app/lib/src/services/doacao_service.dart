import 'package:kara/src/interfaces/i_doacao_service.dart';
import 'package:kara/src/models/doacao.dart';

import 'service_base.dart';

class DoacaoService extends ServiceBase<Doacao> implements IDoacaoService {
  DoacaoService(accessToken, {apiRoot, dio})
      : super(accessToken: accessToken, dio: dio, apiRoot: apiRoot);

  final endpointDoacao = 'doacao';
  final endpointDoacoes = 'doacoes';
  final endpointConfirmacao = 'confirmar';
  final endpointCancelamento = 'cancelar';
  final endpointDoador = 'doador';
  final endpointOng = 'ong';

  @override
  Future<List<Doacao>> getDoacoesDoador(int id, {endpoint}) async {
    var url = endpoint ?? '$endpointDoador/$id/$endpointDoacoes';
    return await this.getAll(url);
  }

  @override
  Future<List<Doacao>> getDoacoesOng(int id, {endpoint}) async {
    var url = endpoint ?? '$endpointOng/$id/$endpointDoacoes';
    return await this.getAll(url);
  }

  @override
  Future<String> confirmarDoacao(int id, {endpoint}) async {
    var url = endpoint ?? '$endpointDoacao/$id/$endpointConfirmacao';
    return await this.post(url);
  }

  @override
  Future<String> cancelarDoacao(int id, {endpoint}) async {
    var url = endpoint ?? '$endpointDoacao/$id/$endpointCancelamento';
    return await this.delete(url);
  }

  @override
  Future<Doacao> cadastrarDoacao(doacao, {endpoint}) async {
    var url = endpoint ?? '$endpointDoacao';
    return await this.postData(url, params: doacao.toJson());
  }

  @override
  Doacao toModel(Map map) => Doacao.fromJson(map);
}

import 'package:kara/src/interfaces/i_doacao_service.dart';
import 'package:kara/src/models/doacao.dart';

import 'service_base.dart';

class DoacaoService extends ServiceBase<Doacao> implements IDoacaoService {
  DoacaoService(accessToken, {apiRoot, dio})
      : super(accessToken: accessToken, dio: dio, apiRoot: apiRoot);

  final endpointDoacao = 'doacao';
  final endpointDoacoes = 'doacoes';
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
  Doacao toModel(Map map) => Doacao.fromJson(map);
}

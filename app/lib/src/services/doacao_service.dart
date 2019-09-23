import 'package:kara/src/interfaces/i_doacao_service.dart';
import 'package:kara/src/models/doacao.dart';
import 'package:kara/src/utils/constants.dart';

import 'service_base.dart';

class DoacaoService extends ServiceBase<Doacao> implements IDoacaoService {
  DoacaoService(accessToken, {apiRoot, dio})
      : super(accessToken: accessToken, dio: dio, apiRoot: apiRoot);

  @override
  Future<List<Doacao>> getDoacoesDoador(int id, {endpoint}) async {
    var url = endpoint ?? '$ENDPOINT_DONATOR/$id/$ENDPOINT_DONATIONS';
    return await this.getAll(url);
  }

  @override
  Future<List<Doacao>> getDoacoesOng(int id, {endpoint}) async {
    var url = endpoint ?? '$ENDPOINT_ONG/$id/$ENDPOINT_DONATIONS';
    return await this.getAll(url);
  }

  @override
  Future<String> confirmarDoacao(int id, {endpoint}) async {
    var url = endpoint ?? '$ENDPOINT_DONATION/$id/$ENDPOINT_CONFIRMATION';
    return await this.post(url);
  }

  @override
  Future<String> cancelarDoacao(int id, {endpoint}) async {
    var url = endpoint ?? '$ENDPOINT_DONATION/$id/$ENDPOINT_CANCELATION';
    return await this.delete(url);
  }

  @override
  Future<Doacao> cadastrarDoacao(doacao, {endpoint}) async {
    var url = endpoint ?? '$ENDPOINT_DONATION';
    return await this.postData(url, params: doacao.toJson());
  }

  @override
  Doacao toModel(Map map) => Doacao.fromJson(map);
}

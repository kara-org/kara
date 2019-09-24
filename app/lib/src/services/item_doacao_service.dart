import 'package:kara/src/interfaces/i_item_doacao_service.dart';
import 'package:kara/src/models/item_doacao.dart';
import 'package:kara/src/utils/constants.dart';

import 'service_base.dart';

class ItemDoacaoService extends ServiceBase<ItemDoacao>
    implements IItemDoacaoService {
  ItemDoacaoService(accessToken, {apiRoot, dio})
      : super(accessToken: accessToken, dio: dio, apiRoot: apiRoot);

  final endpointItemDoacao = ENDPOINT_ITEM;

  @override
  ItemDoacao toModel(Map map) => ItemDoacao.fromJson(map);

  @override
  Future<ItemDoacao> alterarItemDoacao(id, quantidadePrometida, {endpoint}) async {
    var url = endpoint ?? '$ENDPOINT_ITEM/$id/$ENDPOINT_CANCELATION';
    return await this.patchData(url, params: {"quantidade_prometida": quantidadePrometida});
    //TODO resolver retorno da chamada (tá dando exceção, pois o status_code tá vindo 200)
  }

  @override
  Future<String> cancelarItemDoacao(id, {endpoint}) async {
    var url = endpoint ?? '$ENDPOINT_ITEM/$id/$ENDPOINT_CANCELATION';
    return await this.delete(url);
    //TODO resolver retorno da chamada (tá dando exceção, pois a String está sendo retornada como body)
  }

  @override
  Future<String> confirmarItemDoacao(id, quantidadeEfetivada,
      {endpoint}) async {
    var url = endpoint ?? '$ENDPOINT_ITEM/$id/$ENDPOINT_CONFIRMATION';
    return (await this.postData(url,
            params: {"quantidade_efetivada": quantidadeEfetivada}))
        .toString();
    //TODO resolver retorno da chamada
  }
}

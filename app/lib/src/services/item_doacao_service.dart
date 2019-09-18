import 'package:kara/src/interfaces/i_item_doacao_service.dart';
import 'package:kara/src/models/item_doacao.dart';

import 'service_base.dart';

class ItemDoacaoService extends ServiceBase<ItemDoacao> implements IItemDoacaoService {
  ItemDoacaoService(accessToken, {apiRoot, dio})
      : super(accessToken: accessToken, dio: dio, apiRoot: apiRoot);

  final endpointItemDoacao = 'item';

  @override
  Future<ItemDoacao> getItemDoacao({endpoint}) async {
    var url = endpoint ?? endpointItemDoacao;
    return await this.getOne(url);
  }

  @override
  ItemDoacao toModel(Map map) => ItemDoacao.fromJson(map);
}

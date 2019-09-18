import 'package:kara/src/models/item_doacao.dart';

import 'i_service.dart';

abstract class IItemDoacaoService implements IService<ItemDoacao> {
  Future<ItemDoacao> getItemDoacao({endpoint});
}

import 'package:kara/src/models/item_doacao.dart';

import 'i_service.dart';

abstract class IItemDoacaoService implements IService<ItemDoacao> {
  Future<String> cancelarItemDoacao(int id, {String endpoint});
  Future<String> confirmarItemDoacao(int id, double quantidadeEfetivada,
      {String endpoint});
  Future<ItemDoacao> changeItemDoacao(int id, double quantidadePrometida,
      {String endpoint});
}

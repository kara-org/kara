import 'package:kara/src/models/doacao.dart';

import 'i_service.dart';

abstract class IDoacaoService implements IService<Doacao> {
  Future<List<Doacao>> getDoacoesOng(int id, {String endpoint});
  Future<List<Doacao>> getDoacoesDoador(int id, {String endpoint});
}

import 'package:kara/src/models/ong.dart';

import 'i_service.dart';

abstract class IOngService implements IService<Ong> {
  Future<List<Ong>> getOngs({String endpoint});
  Future<Ong> getOng(int id, {String endpoint});
  Future<Ong> createOng(Ong ong, {String endpoint});
  Future<Ong> changeOng(int id, Map<String, dynamic> json, {String endpoint});
}

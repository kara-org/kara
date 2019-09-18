import 'package:kara/src/models/ong.dart';

import 'i_service.dart';

abstract class IOngService implements IService<Ong> {
  Future<List<Ong>> getOngs({endpoint});
}

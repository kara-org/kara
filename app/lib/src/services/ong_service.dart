import 'package:kara/src/interfaces/i_ong_service.dart';
import 'package:kara/src/models/ong.dart';

import 'service_base.dart';

class OngService extends ServiceBase<Ong> implements IOngService {
  OngService(accessToken, {apiRoot, dio})
      : super(accessToken: accessToken, dio: dio, apiRoot: apiRoot);

  final endpointOng = 'ong';

  @override
  Ong toModel(Map map) => Ong.fromJson(map);

  @override
  Future<List<Ong>> getOngs({endpoint}) async {
    var url = endpoint ?? endpointOng;
    return await this.getAll(url);
  }
}

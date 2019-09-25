import 'package:kara/src/interfaces/i_ong_service.dart';
import 'package:kara/src/models/ong.dart';
import 'package:kara/src/utils/constants.dart';

import 'service_base.dart';

class OngService extends ServiceBase<Ong> implements IOngService {
  OngService(accessToken, {apiRoot, dio})
      : super(accessToken: accessToken, dio: dio, apiRoot: apiRoot);

  @override
  Ong toModel(Map map) => Ong.fromJson(map);

  @override
  Future<List<Ong>> getOngs({endpoint}) async {
    var url = endpoint ?? ENDPOINT_ONG;
    return await this.getAll(url);
  }

  @override
  Future<Ong> changeOng(id, json, {endpoint}) async {
    var url = endpoint ?? '$ENDPOINT_ONG/$id';
    return await this.patchData(url, params: json);
  }

  @override
  Future<Ong> createOng(ong, {endpoint}) async {
    var url = endpoint ?? ENDPOINT_ONG;
    return await this.postData(url, params: ong.toJson());
    //TODO separar cadastro de ong na api
  }

  @override
  Future<Ong> getOng(id, {endpoint}) async {
    var url = endpoint ?? '$ENDPOINT_ONG/$id';
    return await this.getOne(url);
  }
}

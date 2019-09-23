import 'package:kara/src/interfaces/i_demanda_service.dart';
import 'package:kara/src/models/demanda.dart';
import 'package:kara/src/utils/constants.dart';

import 'service_base.dart';

class DemandaService extends ServiceBase<Demanda> implements IDemandaService {
  DemandaService(accessToken, {apiRoot, dio})
      : super(accessToken: accessToken, dio: dio, apiRoot: apiRoot);

  @override
  Demanda toModel(Map map) => Demanda.fromJson(map);

  @override
  Future<List<Demanda>> getDemandas({endpoint}) async {
    var url = endpoint ?? ENDPOINT_DEMANDS;
    return await this.getAll(url);
  }

  @override
  Future<Demanda> alterarDemanda(int id, Demanda demanda, {String endpoint}) async {
    var url = endpoint ?? '$ENDPOINT_DEMAND/$id';
    return await this.putData(url, params: demanda.toJson());
  }

  @override
  Future<Demanda> cadastrarDemanda(int id, Demanda demanda, {String endpoint}) async {
    var url = endpoint ?? '$ENDPOINT_ONG/$id/$ENDPOINT_DEMANDS';
    return await this.postData(url, params: demanda.toJson());
  }

  @override
  Future<String> cancelarDemanda(int id, {String endpoint}) async {
    var url = endpoint ?? '$ENDPOINT_DEMAND/$id/$ENDPOINT_CANCELATION';
    return await this.delete(url);
  }

  @override
  Future<List<Demanda>> getDemandasOng(int id, {String endpoint}) async {
    var url = endpoint ?? '$ENDPOINT_ONG/$id/$ENDPOINT_DEMANDS';
    return await this.getAll(url);
  }
}

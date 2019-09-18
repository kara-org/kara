import 'package:kara/src/interfaces/i_demanda_service.dart';
import 'package:kara/src/models/demanda.dart';

import 'service_base.dart';

class DemandaService extends ServiceBase<Demanda> implements IDemandaService {
  DemandaService({dio, apiRoot}) : super(dio: dio, apiRoot: apiRoot);

  final endpointDemanda = 'demandas';

  @override
  Demanda toModel(Map map) => Demanda.fromJson(map);

  @override
  Future<List<Demanda>> getDemandas({endpoint}) async {
    var url = endpoint ?? endpointDemanda;
    return await this.getAll(url);
  }
}

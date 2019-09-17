import 'package:kara/src/models/demanda.dart';
import 'i_service.dart';

abstract class IDemandaService implements IService<Demanda> {
  Future<List<Demanda>> getDemandas({endpoint});
}

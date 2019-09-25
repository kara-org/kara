import 'package:kara/src/models/demanda.dart';

import 'i_service.dart';

abstract class IDemandaService implements IService<Demanda> {
  Future<List<Demanda>> getDemandas({String endpoint});
  Future<List<Demanda>> getDemandasOng(int ongId, {String endpoint});
  Future<String> cancelarDemanda(int id, {String endpoint});
  Future<Demanda> cadastrarDemanda(int ongId, Demanda demanda, {String endpoint});
  Future<Demanda> changeDemanda(int id, Demanda demanda, {String endpoint});
}
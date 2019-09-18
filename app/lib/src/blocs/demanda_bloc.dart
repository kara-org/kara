import 'package:bloc_pattern/bloc_pattern.dart';
import 'package:kara/src/models/demanda.dart';
import 'package:kara/src/services/demanda_service.dart';
import 'package:rxdart/rxdart.dart';

class DemandaBloc extends BlocBase {
  DemandaService _demandaService;

  final _demandsController = BehaviorSubject<List<Demanda>>();
  Observable<List<Demanda>> get demandsStream => _demandsController.stream;
  Function(List<Demanda>) get updateDemands => _demandsController.sink.add;

  loadData() async {
    try {
      _demandaService = DemandaService();

      var demandas = await _demandaService.getDemandas();
      updateDemands(demandas);
    } catch (e) {
      _demandsController.addError(e.message);
    }
  }

  @override
  dispose() {
    _demandsController.close();
    super.dispose();
  }
}

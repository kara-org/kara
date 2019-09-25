import 'package:kara/src/models/demanda.dart';
import 'package:test/test.dart';
import 'package:kara/src/models/access_token.dart';
import 'package:kara/src/services/demanda_service.dart';

Future main() async {
  final accessToken = AccessToken(
    token:
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImprX3ZpZGExOUBob3RtYWlsLmNvbSIsImV4cCI6MTU2NzU4Mzg1NSwiZW1haWwiOiJqa192aWRhMTlAaG90bWFpbC5jb20ifQ.tfevZ-zUQLQS8oZ7vcGi9qqmItUUTaBJKzch-X3qRo8",
  );
  final service = DemandaService(accessToken);

  group('DemandaService tests:', () {
    test('verify if the api is returning data for all demandas request',
        () async {
      await service.getDemandas();
    });
    test('verify if the api is returning data for demandas from ong', () async {
      await service.getDemandasOng(1);
    });
    test(
        'verify if cancelation of a donation that was already confirmed|canceled is not working',
        () async {
      expect(
          () => service.cancelarDemanda(1), throwsA(TypeMatcher<Exception>()));
    });
    test('verify if registration of a demand is working', () async {
      var json = {
        "id_categoria": 1,
        "quantidade_solicitada": 2.2,
        "descricao": "Pinha"
      };
      await service.cadastrarDemanda(1, Demanda.fromJson(json));
    });
    test('verify if changes a demand is working', () async {
      var json = {
        "id": 13,
        "id_ong": 1,
        "id_categoria": 1,
        "quantidade_solicitada": 250.2,
        "quantidade_alcancada": null,
        "descricao": "Arroz",
        "ativo": true
      };
      await service.changeDemanda(13, Demanda.fromJson(json));
    });
  });
}

import 'package:kara/src/models/doacao.dart';
import 'package:test/test.dart';
import 'package:kara/src/models/access_token.dart';
import 'package:kara/src/services/doacao_service.dart';

Future main() async {
  final accessToken = AccessToken(
    token:
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImprX3ZpZGExOUBob3RtYWlsLmNvbSIsImV4cCI6MTU2NzU4Mzg1NSwiZW1haWwiOiJqa192aWRhMTlAaG90bWFpbC5jb20ifQ.tfevZ-zUQLQS8oZ7vcGi9qqmItUUTaBJKzch-X3qRo8",
  );
  final service = DoacaoService(accessToken);

  group('DoacaoService tests:', () {
    test('verify if the api is returning data for doacoes from doador',
        () async {
      expect((await service.getDoacoesDoador(1)).length >= 0, true);
    });
    test('verify if the api is returning data for doacoes from ong', () async {
      expect((await service.getDoacoesOng(1)).length >= 0, true);
    });
    test(
        'verify if confirmation of a donation that was already confirmed|canceled is not working',
        () async {
      expect(
          () => service.confirmarDoacao(1), throwsA(TypeMatcher<Exception>()));
    });
    test(
        'verify if cancelation of a donation that was already confirmed|canceled is not working',
        () async {
      expect(
          () => service.cancelarDoacao(2), throwsA(TypeMatcher<Exception>()));
    });
    test('verify if registration of a donation is working', () async {
      var json = {
        "id_usuario": 3,
        "item_doacao": [
          {"quantidade_prometida": "8", "id_demanda": 1},
          {"quantidade_prometida": "9", "id_demanda": 2},
          {"quantidade_prometida": "6", "id_demanda": 3}
        ]
      };
      await service.cadastrarDoacao(
        Doacao.fromJson(json),
      );
    });
  });
}

import 'package:kara/src/models/doacao.dart';
import 'package:test/test.dart';
import 'package:kara/src/models/access_token.dart';
import 'package:kara/src/services/doacao_service.dart';

Future main() async {
  final accessToken = AccessToken(
    token:
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Impfa2VsdmluMTk5N0Bob3RtYWlsLmNvbSIsImV4cCI6MTU2ODUwMzk5MywiZW1haWwiOiJqX2tlbHZpbjE5OTdAaG90bWFpbC5jb20ifQ.WiuoPe87fgGTjbbn9P9CZg3-DoHS5IyCNV1_PS_0B9k",
  );
  final service = DoacaoService(accessToken);

  group('Complete DoacaoService tests', () {
    test('Verify if the api is returning data for doacoes from doador',
        () async {
      expect((await service.getDoacoesDoador(1)).length >= 0, true);
    });
    test('Verify if the api is returning data for doacoes from ong', () async {
      expect((await service.getDoacoesOng(1)).length >= 0, true);
    });
    test(
        'Verify if confirmation of a donation that was already confirmed|canceled is not working',
        () async {
      expect(
          () => service.confirmarDoacao(1), throwsA(TypeMatcher<Exception>()));
    });
    test(
        'Verify if cancelation of a donation that was already confirmed|canceled is not working',
        () async {
      expect(
          () => service.cancelarDoacao(2), throwsA(TypeMatcher<Exception>()));
    });
    test('Verify if registration of a donation is working', () async {
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

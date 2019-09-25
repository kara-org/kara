import 'package:kara/src/services/usuario_service.dart';
import 'package:kara/src/models/access_token.dart';
import 'package:kara/src/models/usuario.dart';
import 'package:test/test.dart';

Future main() async {
  group('UsuarioService tests:', () {
    test('verify if the api is creating an usuario', () async {
      final service = UsuarioService(null);
      await service.createUsuario(Usuario.fromJson(
        {
          "email": "jz@j.jj",
          "password": "1234",
          "nome_completo": "Jonathan Kelvin",
          "cpf": "06382375560"
        },
      ));
    });
    test('verify if the api is changeing an usuario', () async {
      final accessToken = AccessToken(
        token:
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Impfa2VsdmluMTk5N0Bob3RtYWlsLmNvbSIsImV4cCI6MTU2OTM4NDU4NCwiZW1haWwiOiJqX2tlbHZpbjE5OTdAaG90bWFpbC5jb20ifQ.v9PNns2sp3vEX7OElTFHF8Yqlvt491YCuY9xpsAWSzg",
      );
      final service = UsuarioService(accessToken);
      final json = {
        "email": "j_kelvin1997@hotmail.com",
        "nome_completo": "Jonathan Santos",
        "senha": "j_kelvin1997"
      };
      expect((await service.changeUsuario(2, json)) is Usuario, true);
    });
    test('verify if the api is returning an usuario', () async {
      final accessToken = AccessToken(
        token:
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImprX3ZpZGExOUBob3RtYWlsLmNvbSIsImV4cCI6MTU2NzU4Mzg1NSwiZW1haWwiOiJqa192aWRhMTlAaG90bWFpbC5jb20ifQ.tfevZ-zUQLQS8oZ7vcGi9qqmItUUTaBJKzch-X3qRo8",
      );
      final service = UsuarioService(accessToken);
      expect((await service.getUsuario()) is Usuario, true);
    });
  });
}

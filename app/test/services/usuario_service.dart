import 'package:kara/src/services/usuario_service.dart';
import 'package:kara/src/models/access_token.dart';
import 'package:kara/src/models/usuario.dart';
import 'package:test/test.dart';

Future main() async {
  group('UsuarioService tests:', () {
    test('verify if the api is creating an usuario',
        () async {
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
    test('verify if the api is returning an usuario', () async {
      final accessToken = AccessToken(
        token:
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImprX3ZpZGExOUBob3RtYWlsLmNvbSIsImV4cCI6MTU2NzU4Mzg1NSwiZW1haWwiOiJqa192aWRhMTlAaG90bWFpbC5jb20ifQ.tfevZ-zUQLQS8oZ7vcGi9qqmItUUTaBJKzch-X3qRo8",
      );
      final service = UsuarioService(accessToken);
      await service.getUsuario();
    });
  });
}

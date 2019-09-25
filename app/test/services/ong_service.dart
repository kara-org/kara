import 'package:kara/src/services/ong_service.dart';
import 'package:kara/src/models/access_token.dart';
import 'package:kara/src/models/ong.dart';
import 'package:test/test.dart';

Future main() async {
  group('OngService tests:', () {
    /* test('verify if the api is creating an ong', () async {
      final service = OngService(null);
      await service.createOng(Ong.fromJson(
        {
          "nome": "Banco do Brasil",
          "cnpj": "00000000000191",
          "historia": "dsadsadsadsadsa",
        },
      ));
    }); */
    test('verify if the api is returning an ong', () async {
      final accessToken = AccessToken(
        token:
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImprX3ZpZGExOUBob3RtYWlsLmNvbSIsImV4cCI6MTU2NzU4Mzg1NSwiZW1haWwiOiJqa192aWRhMTlAaG90bWFpbC5jb20ifQ.tfevZ-zUQLQS8oZ7vcGi9qqmItUUTaBJKzch-X3qRo8",
      );
      final service = OngService(accessToken);
      expect((await service.getOng(1)) is Ong, true);
    });
    test('verify if the api is changeing an ong', () async {
      final accessToken = AccessToken(
        token:
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Impfa2VsdmluMTk5N0Bob3RtYWlsLmNvbSIsImV4cCI6MTU2OTM4NDU4NCwiZW1haWwiOiJqX2tlbHZpbjE5OTdAaG90bWFpbC5jb20ifQ.v9PNns2sp3vEX7OElTFHF8Yqlvt491YCuY9xpsAWSzg",
      );
      final service = OngService(accessToken);
      final json = {
        "nome": "GAAC",
        "cnpj": "00.000.000/0001-91",
        "historia":
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
      };
      expect((await service.changeOng(1, json)) is Ong, true);
    });
    test('verify if the api is returning ongs', () async {
      final accessToken = AccessToken(
        token:
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImprX3ZpZGExOUBob3RtYWlsLmNvbSIsImV4cCI6MTU2NzU4Mzg1NSwiZW1haWwiOiJqa192aWRhMTlAaG90bWFpbC5jb20ifQ.tfevZ-zUQLQS8oZ7vcGi9qqmItUUTaBJKzch-X3qRo8",
      );
      final service = OngService(accessToken);
      expect((await service.getOngs()).length, 2);
    });
  });
}

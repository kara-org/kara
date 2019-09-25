import 'package:kara/src/services/item_doacao_service.dart';
import 'package:test/test.dart';
import 'package:kara/src/models/access_token.dart';

Future main() async {
  final accessToken = AccessToken(
    token:
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImprX3ZpZGExOUBob3RtYWlsLmNvbSIsImV4cCI6MTU2NzU4Mzg1NSwiZW1haWwiOiJqa192aWRhMTlAaG90bWFpbC5jb20ifQ.tfevZ-zUQLQS8oZ7vcGi9qqmItUUTaBJKzch-X3qRo8",
  );
  final service = ItemDoacaoService(accessToken);

  group('ItemDoacaoService tests:', () {
    test('verify if the api is confirming an especify item_doacao', () async {
      await service.confirmarItemDoacao(15, 15);
    });
    test('verify if the api is canceling an especify item_doacao', () async {
      await service.cancelarItemDoacao(16);
    });
    test('verify if the api is altering an especify item_doacao', () async {
      await service.changeItemDoacao(37, 35.5);
    });
  });
}

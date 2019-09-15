import 'i_service.dart';
import '../models/access_token.dart';
import 'package:meta/meta.dart';

abstract class IAccessToken implements IService<AccessToken> {
  Future<AccessToken> getAccessToken(
      {@required email, @required password, endpoint, params});
}

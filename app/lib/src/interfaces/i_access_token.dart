import 'package:meta/meta.dart';

import 'package:kara/src/models/access_token.dart';

import 'i_service.dart';

abstract class IAccessToken implements IService<AccessToken> {
  Future<AccessToken> getAccessToken(
      {@required email, @required password, endpoint, params});
}

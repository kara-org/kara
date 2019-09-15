import 'package:meta/meta.dart';

import '../interfaces/i_access_token.dart';
import '../models/access_token.dart';
import '../utils/constants.dart';

import 'service_base.dart';

class AccessTokenService extends ServiceBase<AccessToken>
    implements IAccessToken {
  final endpointAccessToken = 'login';

  AccessTokenService({dio, apiRoot}) : super(dio: dio, apiRoot: apiRoot);

  @override
  Future<AccessToken> getAccessToken(
      {@required email, @required password, endpoint, params}) async {
    if (email == null || password == null)
      throw Exception(errorCampoLoginOrSenhaNull);

    final jsonStr = '{"email": "$email", "password": "$password"}';
    final url = endpoint ?? endpointAccessToken;

    return await this.postData(url, params: jsonStr);
  }

  @override
  AccessToken toModel(Map map) => AccessToken.fromJson(map);
}

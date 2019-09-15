import 'package:dio/dio.dart';
import '../models/access_token.dart';

const int HTTP_OK = 200;
const int HTTP_CREATED = 201;
const int HTTP_ACCEPTED = 202;
const int HTTP_NOT_AUTHORITATIVE = 203;
const int HTTP_NO_CONTENT = 204;
const int HTTP_RESET = 205;
const int HTTP_PARTIAL = 206;
const int HTTP_MULT_CHOICE = 300;
const int HTTP_MOVED_PERM = 301;
const int HTTP_MOVED_TEMP = 302;
const int HTTP_SEE_OTHER = 303;
const int HTTP_NOT_MODIFIED = 304;
const int HTTP_USE_PROXY = 305;
const int HTTP_BAD_REQUEST = 400;
const int HTTP_UNAUTHORIZED = 401;
const int HTTP_PAYMENT_REQUIRED = 402;
const int HTTP_FORBIDDEN = 403;
const int HTTP_NOT_FOUND = 404;
const int HTTP_BAD_METHOD = 405;
const int HTTP_NOT_ACCEPTABLE = 406;
const int HTTP_PROXY_AUTH = 407;
const int HTTP_CLIENT_TIMEOUT = 408;
const int HTTP_CONFLICT = 409;
const int HTTP_GONE = 410;
const int HTTP_LENGTH_REQUIRED = 411;
const int HTTP_PRECON_FAILED = 412;
const int HTTP_ENTITY_TOO_LARGE = 413;
const int HTTP_REQ_TOO_LONG = 414;
const int HTTP_UNSUPPORTED_TYPE = 415;
const int HTTP_INTERNAL_ERROR = 500;
const int HTTP_NOT_IMPLEMENTED = 501;
const int HTTP_BAD_GATEWAY = 502;
const int HTTP_UNAVAILABLE = 503;
const int HTTP_GATEWAY_TIMEOUT = 504;
const int HTTP_VERSION = 505;

InterceptorsWrapper configInterceptor({AccessToken accessToken}) {
  return InterceptorsWrapper(onRequest: (RequestOptions options) async {
    if (accessToken != null)
      options.headers["Authorization"] =
          '${accessToken.type} ${accessToken.token}';
    if (['POST', 'GET', 'PATCH', 'PUT'].contains(options.method))
      options.headers['Content-Type'] = 'application/json';
    return options;
  });
}

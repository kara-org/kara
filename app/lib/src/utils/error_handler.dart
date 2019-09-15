import 'package:dio/dio.dart';

Exception handleError(e) {
  if (e is DioError) {
    if (e.response != null) {
      return Exception('${e.response.statusCode}');
    } else {
      return Exception('${e.message}');
    }
  } else {
    return Exception('Tretas');
  }
}

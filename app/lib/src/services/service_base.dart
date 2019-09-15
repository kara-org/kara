import 'package:dio/dio.dart';
import 'package:kara/src/models/access_token.dart';
import 'package:kara/src/utils/constants.dart';
import 'package:kara/src/utils/error_handler.dart';
import 'package:kara/src/utils/http_connection.dart';

import '../interfaces/i_service.dart';

abstract class ServiceBase<M> implements IService<M> {
  String apiRoot;
  Dio dio;

  ServiceBase({this.apiRoot, AccessToken accessToken, this.dio}) {
    this.dio = dio ?? Dio();
    this.apiRoot = apiRoot ?? URL_API;
    this.dio.options.connectTimeout = 5000;
    this.dio.options.receiveTimeout = 3000;
    this.dio.options.sendTimeout = 3000;
    if (this.dio.interceptors != null) {
      var interceptor = configInterceptor(accessToken: accessToken);
      this.dio.interceptors.add(interceptor);
    }
  }

  @override
  Future<M> putData(endpoint, {params}) {
    // TODO: implement putData
    return null;
  }

  @override
  Future<M> patchData(endpoint, {params}) {
    // TODO: implement putData
    return null;
  }

  @override
  Future<M> deleteData(endpoint, {params}) {
    // TODO: implement deleteData
    return null;
  }

  @override
  Future<M> postData(endpoint, {params}) async {
    final url = '$apiRoot/$endpoint/';
    try {
      var options = RequestOptions(headers: {
        'Content-Type': 'application/json',
      });
      Response response = await dio.post(url, data: params, options: options);
      if (response != null && response?.statusCode == HTTP_OK)
        return toModel(response.data);

      throw handleError(DioError(response: response));
    } catch (e) {
      throw handleError(e);
    }
  }

  @override
  Future<M> getOne(endpoint, {params}) async {
    final url = '$apiRoot/$endpoint';
    try {
      final response = await dio.get(url, queryParameters: params);
      if (response != null && response.statusCode == HTTP_OK)
        return toModel(response.data);

      throw handleError(DioError(response: response));
    } catch (e) {
      throw handleError(e);
    }
  }

  @override
  Future<List<M>> getAll(endpoint, {params}) async {
    final url = '$apiRoot/$endpoint';
    try {
      final response = await dio.get(url, queryParameters: params);

      if (response != null && response.statusCode == HTTP_OK)
        return response.data.map<M>((r) => toModel(r)).toList();

      throw handleError(DioError(response: response));
    } catch (e) {
      throw handleError(e);
    }
  }

  M toModel(Map map);
}
import 'package:kara/src/interfaces/i_usuario_service.dart';
import 'package:kara/src/models/usuario.dart';
import 'package:kara/src/utils/constants.dart';

import 'service_base.dart';

class UsuarioService extends ServiceBase<Usuario> implements IUsuarioService {
  UsuarioService(accessToken, {apiRoot, dio})
      : super(accessToken: accessToken, dio: dio, apiRoot: apiRoot);

  @override
  Future<Usuario> getUsuario({endpoint}) async {
    var url = endpoint ?? '$ENDPOINT_AUTH/$ENDPOINT_USER';
    return await this.getOne(url);
  }

  @override
  Future<Usuario> changeUsuario(id, json, {endpoint}) async {
    var url = endpoint ?? '$ENDPOINT_USER/$id';
    return await this.patchData(url, params: json);
  }

  @override
  Future<Usuario> createUsuario(usuario, {endpoint}) async {
    var url = endpoint ?? ENDPOINT_USER;
    return await this.postData(url, params: usuario.toJson());
  }

  @override
  Usuario toModel(Map map) => Usuario.fromJson(map);
}

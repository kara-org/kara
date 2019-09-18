import 'package:kara/src/interfaces/i_usuario_service.dart';
import 'package:kara/src/models/usuario.dart';

import 'service_base.dart';

class UsuarioService extends ServiceBase<Usuario> implements IUsuarioService {
  UsuarioService(accessToken, {apiRoot, dio})
      : super(accessToken: accessToken, dio: dio, apiRoot: apiRoot);

  final endpointUsuario = 'auth/usuario';

  @override
  Future<Usuario> getUsuario({endpoint}) async {
    var url = endpoint ?? endpointUsuario;
    return await this.getOne(url);
  }

  @override
  Usuario toModel(Map map) => Usuario.fromJson(map);
}

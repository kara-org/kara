import 'package:kara/src/models/usuario.dart';

import 'i_service.dart';

abstract class IUsuarioService implements IService<Usuario> {
  Future<Usuario> getUsuario({endpoint});
}

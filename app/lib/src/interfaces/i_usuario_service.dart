import 'package:kara/src/models/usuario.dart';

import 'i_service.dart';

abstract class IUsuarioService implements IService<Usuario> {
  Future<Usuario> getUsuario({String endpoint});
  Future<Usuario> createUsuario(Usuario usuario, {String endpoint});
}

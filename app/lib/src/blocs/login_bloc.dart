import 'package:bloc_pattern/bloc_pattern.dart';
import 'package:kara/src/preferences/access_token_preference.dart';
import 'package:kara/src/preferences/usuario_preference.dart';
import 'package:kara/src/services/access_token_service.dart';
import 'package:kara/src/services/usuario_service.dart';
import 'package:kara/src/utils/validator.dart';
import 'package:rxdart/rxdart.dart';

class LoginBloc extends BlocBase with Validator {
  final _tokenService = AccessTokenService();
  UsuarioService _usuarioService;

  LoginBloc() {
    //login('teste@hotmail.com', 'teste');
  }

  final _hidePasswordController = BehaviorSubject<bool>.seeded(true);
  final _controllerLoading = BehaviorSubject<bool>.seeded(false);
  final _emailController = BehaviorSubject<String>();
  final _passwordController = BehaviorSubject<String>();

  Observable<bool> get hidePassword => _hidePasswordController.stream;
  Stream<String> get email => _emailController.stream.transform(validateEmail);
  Stream<String> get password =>
      _passwordController.stream.transform(validatePassword);
  Stream<bool> get outLoading => _controllerLoading.stream;
  Stream<bool> get submitValid =>
      Observable.combineLatest2(email, password, (e, p) => true);

  Function(String) get changeEmail => _emailController.sink.add;
  Function(String) get changePassword => _passwordController.sink.add;
  Function(bool) get changeHidePassword => _hidePasswordController.sink.add;

  Future<String> login(String email, String password) async {
    _controllerLoading.add(true);
    try {
      var accessToken =
          await _tokenService.getAccessToken(email: email, password: password);
      _usuarioService = UsuarioService(accessToken);

      var user = await _usuarioService.getUsuario();

      await AccessTokenPreference.setToken(accessToken);
      await UsuarioPreference.setUsuario(user);
    } catch (e) {
      _controllerLoading.add(false);
      return e.toString();
    }
    _controllerLoading.add(false);
    return "true";
  }

  logout() async {
    await AccessTokenPreference.clear();
    await UsuarioPreference.clear();
  }

  submit() {
    final validEmail = _emailController.value.trim();
    final validPassword = _passwordController.value.trim();

    return login(validEmail, validPassword);
  }

  @override
  dispose() {
    _emailController.close();
    _passwordController.close();
    _hidePasswordController.close();
    super.dispose();
  }
}

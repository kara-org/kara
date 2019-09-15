import 'dart:async';
import 'dart:convert';
import 'package:kara/src/models/usuario.dart';
import 'package:shared_preferences/shared_preferences.dart';

abstract class UsuarioPreference {
  static final String _usuario = "usuario";

  static Future<bool> setUsuario(Usuario usuario) async {
    final SharedPreferences prefs = await SharedPreferences.getInstance();
    return prefs.setString(_usuario, json.encode(usuario.toJson()));
  }

  static Future<Usuario> getUsuario() async {
    final SharedPreferences prefs = await SharedPreferences.getInstance();
    String jsonPref = prefs.getString(_usuario) ?? null;
    if (jsonPref != null) return Usuario.fromJson(json.decode(jsonPref));
    return null;
  }

  static Future<bool> isAuthenticated() async {
    final SharedPreferences prefs = await SharedPreferences.getInstance();
    return prefs.getString(_usuario) != null;
  }

  static Future<Null> clear() async {
    final SharedPreferences prefs = await SharedPreferences.getInstance();
    prefs.remove(_usuario);
  }
}

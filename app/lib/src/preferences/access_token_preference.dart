import 'dart:async';
import 'dart:convert';
import 'package:kara/src/models/access_token.dart';
import 'package:shared_preferences/shared_preferences.dart';

abstract class AccessTokenPreference {
  static final String _token = "token";

  static Future<bool> setToken(AccessToken accessToken) async {
    final SharedPreferences prefs = await SharedPreferences.getInstance();
    return prefs.setString(_token, json.encode(accessToken.toJson()));
  }

  static Future<AccessToken> getToken() async {
    final SharedPreferences prefs = await SharedPreferences.getInstance();
    String jsonPref = prefs.getString(_token) ?? null;
    if (jsonPref != null) return AccessToken.fromJson(json.decode(jsonPref));
    return null;
  }

  static Future<Null> clear() async {
    final SharedPreferences prefs = await SharedPreferences.getInstance();
    prefs.remove(_token);
  }
}

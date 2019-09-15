import 'package:flutter/material.dart';

class KaraThemes {
  static const Map<int, Color> primaryColor = {
    50: Color(0xff79d9bc),
    100: Color(0xff62d2b1),
    200: Color(0xff4be1b4),
    300: Color(0xff36ddab),
    400: Color(0xff24d6a0),
    500: Color(0xff20c090),
    600: Color(0xff1caa80),
    700: Color(0xff19946f),
    800: Color(0xff157e5f),
    900: Color(0xff137356),
  };

  static const Map<int, Color> secundaryColor = {
    50: Color(0xffecbcca),
    100: Color(0xffdf8fa7),
    200: Color(0xffe14b78),
    300: Color(0xffdd3668),
    400: Color(0xffd62459),
    500: Color(0xffc02050),
    600: Color(0xffaa1c47),
    700: Color(0xff94193e),
    800: Color(0xff7e1535),
    900: Color(0xff601028),
  };

  static const appBarTheme = const AppBarTheme(
    brightness: Brightness.light,
    textTheme: TextTheme(
      title: TextStyle(color: Color(0xff20c090), fontSize: 20),
    ),
    color: Colors.white,
    iconTheme: IconThemeData(color: Color(0xff20c090)),
  );

  static const tabBarTheme = const TabBarTheme(
    labelColor: Color(0xffc02050),
    indicator: UnderlineTabIndicator(
      borderSide: BorderSide(color: Color(0xffc02050), width: 2),
    ),
    unselectedLabelColor: Color(0xffc02050),
    labelPadding: EdgeInsets.all(0),
  );
}

import 'dart:async';

import 'package:flutter_svg/flutter_svg.dart';
import 'package:kara/src/preferences/usuario_preference.dart';
import 'package:kara/src/utils/constants.dart';
import 'package:flutter/material.dart';
import 'package:kara/src/utils/kara_themes.dart';

class SplashPage extends StatefulWidget {
  @override
  _SplashPageState createState() => _SplashPageState();
}

class _SplashPageState extends State<SplashPage> {
  startTime() async {
    var _duration = Duration(seconds: 2);
    return Timer(_duration, navigationPage);
  }

  void navigationPage() async {
    bool isAuthenticated = await UsuarioPreference.isAuthenticated();
    await Future.delayed(const Duration(seconds: 2));
    if (isAuthenticated)
      await Navigator.of(context).pushReplacementNamed(DESCRIPTION_PAGE_HOME);
    else
      await Navigator.of(context).pushReplacementNamed(DESCRIPTION_PAGE_LOGIN);
  }

  @override
  void initState() {
    super.initState();
    startTime();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: Container(
        padding: EdgeInsets.all(32),
        child: Center(
          child: SvgPicture.asset(
            DESCRIPTION_KARA_LOGO,
            color: KaraThemes.primaryColor[500],
            fit: BoxFit.fill,
          ),
        ),
      ),
    );
  }
}

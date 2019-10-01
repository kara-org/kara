import 'dart:async';

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
      await Navigator.of(context).pushReplacementNamed(DESCRIPTION_NAV_BAR);
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
      backgroundColor: KaraThemes.primaryColor[500],
      body: Container(
        alignment: Alignment.center,
        padding: EdgeInsets.all(32),
        child: Image.asset(
          DESCRIPTION_KARA_LOGO_PNG,
          color: Colors.white,
          width: MediaQuery.of(context).size.width * .7,
        ),
      ),
    );
  }
}

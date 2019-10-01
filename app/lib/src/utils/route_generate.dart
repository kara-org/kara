import 'package:flutter/material.dart';

import 'constants.dart';
import 'routes.dart';

class RouteGenerator {
  static Route<dynamic> generateRoute(RouteSettings settings) {
    //final args = settings.arguments;

    switch (settings.name) {
      case DESCRIPTION_PAGE_SPLASH:
        return MaterialPageRoute(builder: (_) => SplashPage());
      case DESCRIPTION_PAGE_LOGIN:
        return MaterialPageRoute(builder: (_) => LoginPage());
      case DESCRIPTION_NAV_BAR:
        return MaterialPageRoute(builder: (_) => NavBar());
      case DESCRIPTION_PAGE_HOME:
        return MaterialPageRoute(builder: (_) => HomePage());
      case DESCRIPTION_PAGE_DEMANDS:
        return MaterialPageRoute(builder: (_) => DemandsPage());
      default:
        return MaterialPageRoute(builder: (_) => SplashPage());
    }
  }

  static Route<dynamic> _errorRoute(String error) {
    return MaterialPageRoute(builder: (_) {
      return Scaffold(
        appBar: AppBar(
          title: Text(DESCRIPTION_DIALOG_ERROR),
        ),
        body: Center(
          child: Text(error),
        ),
      );
    });
  }
}

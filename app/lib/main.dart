import 'package:bloc_pattern/bloc_pattern.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:kara/src/blocs/login_bloc.dart';
import 'package:kara/src/ui/pages/home_page.dart';
import 'package:kara/src/ui/pages/login_page.dart';
import 'package:kara/src/ui/pages/splash_page.dart';
import 'package:kara/src/utils/constants.dart';
import 'package:kara/src/utils/kara_themes.dart';

import 'src/utils/constants.dart';

void main() {
  runApp(Main());
}

class Main extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        title: DESCRIPTION_APP_TITLE,
        theme: ThemeData(
            primarySwatch: MaterialColor(
              0xff20c090,
              KaraThemes.primaryColor,
            ),
            brightness: Brightness.light,
            accentColor: KaraThemes.primaryColor[700],
            primaryColor: KaraThemes.primaryColor[500],
            secondaryHeaderColor: KaraThemes.secundaryColor[500],
            appBarTheme: KaraThemes.appBarTheme,
            tabBarTheme: KaraThemes.tabBarTheme),
        home: SplashPage(),
        routes: <String, WidgetBuilder>{
          DESCRIPTION_PAGE_LOGIN: (BuildContext context) => LoginPage(),
          DESCRIPTION_PAGE_HOME: (BuildContext context) => HomePage(),
        },
      ),
      blocs: [
        Bloc((i) => LoginBloc()),
      ],
    );
  }
}

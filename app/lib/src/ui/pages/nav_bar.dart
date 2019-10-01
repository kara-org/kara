import 'package:fancy_bottom_navigation/fancy_bottom_navigation.dart';
import 'package:flutter/material.dart';
import 'package:kara/src/ui/pages/demands_page.dart';
import 'package:kara/src/utils/constants.dart';

import 'home_page.dart';

class NavBar extends StatefulWidget {
  @override
  _NavBarState createState() => _NavBarState();
}

class _NavBarState extends State<NavBar> {
  int currentPage = 0;

  GlobalKey bottomNavigationKey = GlobalKey();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _getPage(currentPage),
      bottomNavigationBar: FancyBottomNavigation(
        tabs: [
          TabData(
              iconData: Icons.home,
              title: DESCRIPTION_PAGE_HOME,
              onclick: () {
                final FancyBottomNavigationState fState =
                    bottomNavigationKey.currentState;
                fState.setPage(0);
              }),
          TabData(
              iconData: Icons.favorite,
              title: DESCRIPTION_DONATES,
              onclick: () {
                final FancyBottomNavigationState fState =
                    bottomNavigationKey.currentState;
                fState.setPage(1);
              }),
          TabData(
            iconData: Icons.search,
            title: 'Busca',
            onclick: () {
              final FancyBottomNavigationState fState =
                  bottomNavigationKey.currentState;
              fState.setPage(2);
            },
          ),
          TabData(
            iconData: Icons.shopping_cart,
            title: 'Carrinho',
            onclick: () {
              final FancyBottomNavigationState fState =
                  bottomNavigationKey.currentState;
              fState.setPage(3);
            },
          ),
        ],
        initialSelection: 0,
        key: bottomNavigationKey,
        onTabChangedListener: (position) {
          setState(() {
            currentPage = position;
          });
        },
      ),
      drawer: Drawer(
        child: ListView(
          children: <Widget>[Text("Hello"), Text("World")],
        ),
      ),
    );
  }

  _getPage(int page) {
    switch (page) {
      case 0:
        return HomePage();
      case 1:
        return DemandsPage();
      case 2:
        return HomePage();
      case 3:
        return DemandsPage();
      case 4:
        return HomePage();
      default:
        return HomePage();
    }
  }
}

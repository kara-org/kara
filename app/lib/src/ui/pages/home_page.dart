import 'package:bloc_pattern/bloc_pattern.dart';
import 'package:flutter/material.dart';
import 'package:kara/src/blocs/login_bloc.dart';
import 'package:kara/src/utils/constants.dart';
import 'package:kara/src/utils/kara_themes.dart';
import 'package:flutter_svg/flutter_svg.dart';

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final primaryColor2 = KaraThemes.primaryColor[200];
  final primaryColor5 = KaraThemes.primaryColor[500];

  @override
  Widget build(BuildContext context) {
    final bloc = BlocProvider.getBloc<LoginBloc>();
    final _screenSize = MediaQuery.of(context).size;

    return Scaffold(
      appBar: AppBar(
        title: Text(DESCRIPTION_APP_BAR_HOME),
        centerTitle: true,
        actions: <Widget>[
          buildIconButton(context, bloc),
        ],
      ),
      body: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            Container(
              padding: EdgeInsets.all(10),
              width: _screenSize.width,
              height: _screenSize.height - 55 - 25,
              decoration: BoxDecoration(
                color: primaryColor2,
                image: DecorationImage(
                  image: AssetImage(DESCRIPTION_VIDEO_BG),
                  fit: BoxFit.fitHeight,
                ),
              ),
              child: buildSearchColumn(),
            ),
            Container(
              height: _screenSize.height - 55 - 25 - 40,
              margin: EdgeInsets.only(top: 30, bottom: 10),
              width: _screenSize.width,
              child: Column(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: <Widget>[
                  Container(
                    child: Text(
                      DESCRIPTION_HOW_WORKS,
                      style: TextStyle(
                        color: primaryColor5,
                        fontSize: 25,
                        fontWeight: FontWeight.w500,
                      ),
                    ),
                  ),
                  buildTutorialRow(
                    _screenSize.width,
                    DESCRIPTION_LADY_PC,
                    '1',
                    DESCRIPTION_TUTORIAL_1,
                    false,
                  ),
                  buildTutorialRow(
                    _screenSize.width,
                    DESCRIPTION_HAPPY_LADY,
                    '2',
                    DESCRIPTION_TUTORIAL_2,
                    true,
                  ),
                  buildTutorialRow(
                    _screenSize.width,
                    DESCRIPTION_MAN,
                    '3',
                    DESCRIPTION_TUTORIAL_3,
                    false,
                  ),
                ],
              ),
            )
          ],
        ),
      ),
    );
  }

  Column buildSearchColumn() {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Container(
          padding: EdgeInsets.all(2),
          margin: EdgeInsets.only(bottom: 20, top: 40),
          color: KaraThemes.primaryColor[500],
          child: Text(
            DESCRIPTION_HELP_BY_DONATE,
            textAlign: TextAlign.start,
            style: TextStyle(
              color: Colors.white,
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
        Container(
          margin: EdgeInsets.only(bottom: 10),
          child: Text(
            DESCRIPTION_SEARCH_DEMANDS,
            style: TextStyle(
              color: Colors.white,
              fontWeight: FontWeight.bold,
            ),
            textAlign: TextAlign.center,
          ),
        ),
        Container(
          height: 50,
          margin: EdgeInsets.only(bottom: 30),
          child: ListTile(
            contentPadding: EdgeInsets.all(0),
            title: Container(
              child: searchField(),
            ),
            trailing: SizedBox(
              height: double.infinity,
              child: buildSearchButton(context),
            ),
          ),
        ),
      ],
    );
  }

  RaisedButton buildSearchButton(BuildContext context) {
    return RaisedButton(
      child: Text(
        DESCRIPTION_SEARCH,
        style: TextStyle(
          color: Colors.white,
        ),
      ),
      color: primaryColor5,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.all(Radius.circular(25)),
      ),
      onPressed: () {
        Navigator.of(context).pushNamed(DESCRIPTION_PAGE_DEMANDS);
      },
    );
  }

  IconButton buildIconButton(BuildContext context, LoginBloc bloc) {
    return IconButton(
      icon: Icon(Icons.exit_to_app),
      onPressed: () async {
        await bloc.logout();
        Navigator.of(context).pushReplacementNamed(DESCRIPTION_PAGE_LOGIN);
      },
    );
  }

  StreamBuilder searchField() {
    return StreamBuilder(
      stream: null,
      builder: (context, snapshot) {
        return TextField(
          cursorColor: primaryColor2,
          onChanged: (_) {},
          keyboardType: TextInputType.text,
          decoration: InputDecoration(
            fillColor: Colors.white,
            filled: true,
            border: OutlineInputBorder(),
            hintText: DESCRIPTION_SEARCH_HINT,
            errorText: snapshot.error,
          ),
        );
      },
    );
  }

  Row buildTutorialRow(
    double _screenWidth,
    String asset,
    String orderNumber,
    String tutorialText,
    bool revertDirection,
  ) {
    return Row(
      textDirection: revertDirection ? TextDirection.rtl : TextDirection.ltr,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: <Widget>[
        Container(
          height: 150,
          width: 150,
          child: SvgPicture.asset(
            asset,
            fit: BoxFit.cover,
          ),
        ),
        Container(
          margin: EdgeInsets.all(15),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Container(
                margin: EdgeInsets.only(bottom: 10),
                height: 25,
                width: 25,
                decoration: BoxDecoration(
                  color: primaryColor5,
                  borderRadius: BorderRadius.circular(5),
                ),
                child: Center(
                  child: Text(
                    orderNumber,
                    style: TextStyle(color: Colors.white),
                  ),
                ),
              ),
              Container(
                width: _screenWidth * .5,
                child: Text(
                  tutorialText,
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}

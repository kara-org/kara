import 'package:kara/src/utils/constants.dart';
import 'package:flutter/material.dart';
import 'package:kara/src/utils/kara_themes.dart';

class ErrorDialog extends StatelessWidget {
  final String title;
  final String error;
  final Function function;
  final primaryColor2 = KaraThemes.secundaryColor[200];

  ErrorDialog({this.title, this.error, this.function});

  @override
  Widget build(BuildContext context) {
    return SimpleDialog(
      contentPadding: EdgeInsets.all(0),
      shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.all(Radius.circular(5))),
      children: <Widget>[
        Container(
          height: 50,
          decoration: BoxDecoration(
            borderRadius: BorderRadius.all(Radius.circular(5)),
            color: primaryColor2,
          ),
          child: Center(
            child: Text(title ?? DESCRIPTION_DIALOG_ERROR,
                style: TextStyle(
                    color: Colors.white,
                    fontSize: 20,
                    fontWeight: FontWeight.bold),
                textAlign: TextAlign.center),
          ),
        ),
        SizedBox(
          height: 20,
        ),
        Container(
          padding: EdgeInsets.all(8),
          child: Column(
            children: <Widget>[
              Center(
                child: Text(
                  error?.toString() ?? DESCRIPTION_ERROR_DEFAULT,
                  style: TextStyle(fontSize: 15),
                ),
              ),
              Divider(
                height: 20,
              ),
              Container(
                child: OutlineButton(
                  child: Text(
                    DESCRIPTION_TRY_AGAIN,
                    style: TextStyle(color: primaryColor2, fontSize: 18),
                  ),
                  onPressed: () {
                    function();
                  },
                ),
              )
            ],
          ),
        )
      ],
    );
  }
}

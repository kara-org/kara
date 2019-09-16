import 'package:bloc_pattern/bloc_pattern.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:kara/src/blocs/login_bloc.dart';
import 'package:kara/src/ui/components/error_dialog.dart';
import 'package:kara/src/utils/constants.dart';
import 'package:kara/src/utils/kara_themes.dart';

class LoginPage extends StatelessWidget {
  final primaryColor5 = KaraThemes.primaryColor[500];
  final primaryColor2 = KaraThemes.primaryColor[200];
  final _focusNode1 = FocusNode();
  final _focusNode2 = FocusNode();

  @override
  Widget build(BuildContext context) {
    final bloc = BlocProvider.getBloc<LoginBloc>();
    final _screenSize = MediaQuery.of(context).size;

    return Scaffold(
      appBar: AppBar(
        elevation: 2,
        title: Text(
          DESCRIPTION_APP_BAR_LOGIN,
        ),
        centerTitle: true,
      ),
      body: Center(
        child: SizedBox(
          width: _screenSize.width * .8,
          child: SingleChildScrollView(
            scrollDirection: Axis.vertical,
            child: Column(
              children: <Widget>[
                Container(
                  margin: EdgeInsets.symmetric(vertical: 30, horizontal: 10),
                  child: SvgPicture.asset(
                    DESCRIPTION_KARA_LOGO,
                    color: primaryColor5,
                    fit: BoxFit.fitHeight,
                    height: 100,
                  ),
                ),
                Card(
                  elevation: 2,
                  child: Container(
                    padding: EdgeInsets.all(20),
                    child: Column(
                      children: <Widget>[
                        Container(
                          margin: EdgeInsets.only(top: 20),
                          child: emailField(bloc),
                        ),
                        Container(
                          margin: EdgeInsets.only(top: 10),
                          child: passwordField(bloc),
                        ),
                        forgotButton(bloc, context),
                        Container(
                          margin: EdgeInsets.only(left: 1, right: 1),
                          child: submitButton(bloc, context),
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget emailField(LoginBloc bloc) {
    return StreamBuilder(
      stream: bloc.email,
      builder: (context, snapshot) {
        return TextField(
          focusNode: _focusNode1,
          textInputAction: TextInputAction.next,
          onSubmitted: (_) {
            _focusNode1.unfocus();
            FocusScope.of(context).requestFocus(_focusNode2);
          },
          cursorColor: primaryColor2,
          onChanged: bloc.changeEmail,
          keyboardType: TextInputType.emailAddress,
          decoration: InputDecoration(
            border: OutlineInputBorder(),
            labelText: DESCRIPTION_EMAIL,
            errorText: snapshot.error,
          ),
        );
      },
    );
  }

  Widget passwordField(LoginBloc bloc) {
    return StreamBuilder(
      stream: bloc.password,
      builder: (context, snapshot) {
        return StreamBuilder<Object>(
          stream: bloc.hidePassword,
          initialData: true,
          builder: (context, hideSnapshot) {
            return TextField(
              focusNode: _focusNode2,
              obscureText: hideSnapshot.data,
              cursorColor: primaryColor2,
              onChanged: bloc.changePassword,
              decoration: InputDecoration(
                suffixIcon: IconButton(
                  onPressed: () => bloc.changeHidePassword(!hideSnapshot.data),
                  icon: Icon(
                    hideSnapshot.data ? Icons.visibility : Icons.visibility_off,
                    color: primaryColor5,
                  ),
                ),
                border: OutlineInputBorder(),
                labelText: DESCRIPTION_PASSWORD,
                errorText: snapshot.error,
              ),
            );
          },
        );
      },
    );
  }

  Widget forgotButton(LoginBloc bloc, BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.end,
      children: <Widget>[
        FlatButton(
          child: Text(
            DESCRIPTION_BUTTON_FORGOT_PASSWORD,
            style: TextStyle(fontWeight: FontWeight.normal),
          ),
          onPressed: () {},
        ),
      ],
    );
  }

  void submit(
      AsyncSnapshot snapshot, BuildContext context, LoginBloc bloc) async {
    if (snapshot.hasData) {
      String result = await bloc.submit();
      if (result.contains("true")) {
        Navigator.of(context).pushReplacementNamed(DESCRIPTION_PAGE_HOME);
      } else {
        showDialog(
          context: context,
          builder: (_) {
            return ErrorDialog(
              error: result,
              function: () async {
                String result = await bloc.submit();
                if (result.contains("true")) {
                  Navigator.of(context).pop();
                  Navigator.of(context)
                      .pushReplacementNamed(DESCRIPTION_PAGE_HOME);
                }
              },
            );
          },
        );
      }
    }
  }

  Widget submitButton(LoginBloc bloc, BuildContext context) {
    return StreamBuilder<Object>(
      stream: bloc.outLoading,
      builder: (_, snapshot) {
        if (snapshot.hasData && snapshot.data) {
          return Container(
            height: 50,
            width: 50,
            alignment: Alignment.center,
            child: CircularProgressIndicator(),
          );
        } else {
          return StreamBuilder(
            stream: bloc.submitValid,
            builder: (_, snapshot) {
              return SizedBox(
                width: double.infinity,
                child: OutlineButton(
                  child: Text(
                    DESCRIPTION_ENTER,
                    style: TextStyle(
                      color: primaryColor5,
                    ),
                  ),
                  textColor: primaryColor5,
                  color: primaryColor5,
                  highlightedBorderColor: primaryColor5,
                  borderSide: BorderSide(
                    color: primaryColor5,
                    width: 1,
                  ),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.all(Radius.circular(25)),
                  ),
                  onPressed: () async {
                    submit(snapshot, context, bloc);
                  },
                ),
              );
            },
          );
        }
      },
    );
  }
}

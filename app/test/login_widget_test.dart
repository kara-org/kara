import 'package:bloc_pattern/bloc_pattern.dart';
import 'package:kara/src/blocs/login_bloc.dart';
import 'package:kara/src/ui/pages/login_page.dart';
import 'package:kara/src/utils/constants.dart';

import 'package:flutter/material.dart';

import 'package:flutter_test/flutter_test.dart';

void main() {
  group('Complete widget tests of LoginPage: ', () {
    testWidgets(
        'Verify if there are 2 TextFields (email and password), an OutlineButton and a FlatButton',
        (WidgetTester tester) async {
      await tester.pumpWidget(
        BlocProvider(
          child: MaterialApp(
            home: LoginPage(),
          ),
          blocs: [
            Bloc((i) => LoginBloc()),
          ],
        ),
      );

      final txtFields = find.byType(TextField);
      expect(txtFields, findsNWidgets(2));

      TextField txtFieldEmail = tester.widget(txtFields.at(0));
      expect(txtFieldEmail.decoration.labelText, DESCRIPTION_EMAIL);

      TextField txtFieldSenha = tester.widget(txtFields.at(1));
      expect(txtFieldSenha.decoration.labelText, DESCRIPTION_PASSWORD);

      final btnEntrar = find.byType(OutlineButton);
      expect(btnEntrar, findsOneWidget);

      final btnForgot = find.byType(FlatButton);
      expect(btnForgot, findsOneWidget);
    });

    group('Checking if the error message is working correctly: ', () {
      testWidgets("Check if the error is showing when it's supposed to",
          (WidgetTester tester) async {
        LoginBloc bloc = LoginBloc();
        bloc.changeEmail('');
        bloc.changePassword('');

        await tester.pumpWidget(
          BlocProvider(
            child: MaterialApp(
              home: LoginPage(),
            ),
            blocs: [
              Bloc((i) => bloc),
            ],
          ),
        );

        await tester.pump(Duration.zero);

        final txtFields = find.byType(TextField);

        final finderEmail = txtFields.at(0);
        TextField txtFieldEmail = tester.widget(finderEmail);
        expect(txtFieldEmail.decoration.errorText, DESCRIPTION_MISSING_FIELD);

        final finderPassword = txtFields.at(1);
        TextField textFieldPassword = tester.widget(finderPassword);
        expect(
            textFieldPassword.decoration.errorText, DESCRIPTION_MISSING_FIELD);
      });

      testWidgets(
          "Check if the error is not showing when it's supposed to not show",
          (WidgetTester tester) async {
        LoginBloc bloc = LoginBloc();
        bloc.changeEmail('email@domain.com');
        bloc.changePassword('password');

        await tester.pumpWidget(
          BlocProvider(
            child: MaterialApp(
              home: LoginPage(),
            ),
            blocs: [
              Bloc((i) => bloc),
            ],
          ),
        );

        await tester.pump(Duration.zero);

        final txtFields = find.byType(TextField);

        final finderEmail = txtFields.at(0);
        TextField txtFieldEmail = tester.widget(finderEmail);
        expect(txtFieldEmail.decoration.errorText, null);

        final finderPassword = txtFields.at(1);
        TextField txtFieldPassword = tester.widget(finderPassword);
        expect(txtFieldPassword.decoration.errorText, null);
      });
    });

    testWidgets('Verify if the hide/show button is working correctly',
        (WidgetTester tester) async {
      LoginBloc bloc = LoginBloc();
      bloc.changeHidePassword(false);

      // Build our app and trigger a frame.
      await tester.pumpWidget(
        BlocProvider(
          child: MaterialApp(
            home: LoginPage(),
          ),
          blocs: [
            Bloc((i) => bloc),
          ],
        ),
      );

      await tester.pump(Duration.zero);

      // Validate if the password isn't obscured
      final txtFields = find.byType(TextField);
      final finderPassword = txtFields.at(1);
      TextField txtFieldPassword = tester.widget(finderPassword);
      expect(txtFieldPassword.obscureText, false);
    });
  });
}

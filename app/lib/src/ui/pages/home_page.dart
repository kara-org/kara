import 'package:bloc_pattern/bloc_pattern.dart';
import 'package:flutter/material.dart';
import 'package:kara/src/blocs/login_bloc.dart';
import 'package:kara/src/utils/constants.dart';

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final bloc = BlocProvider.getBloc<LoginBloc>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Home"),
      ),
      body: Center(
        child: RaisedButton(
          child: Text('Logout'),
          onPressed: () async {
            await bloc.logout();
            Navigator.of(context).pushReplacementNamed(DESCRIPTION_PAGE_LOGIN);
          },
        ),
      ),
    );
  }
}

import 'package:bloc_pattern/bloc_pattern.dart';
import 'package:flutter/material.dart';
import 'package:kara/src/blocs/demanda_bloc.dart';
import 'package:kara/src/models/demanda.dart';
import 'package:kara/src/ui/components/demand_widget.dart';
import 'package:kara/src/utils/constants.dart';

class DemandsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final bloc = BlocProvider.getBloc<DemandaBloc>();
    return Scaffold(
      appBar: AppBar(
        title: Text(DESCRIPTION_DEMANDS),
        centerTitle: true,
      ),
      body: buildDemands(bloc),
    );
  }

  StreamBuilder<List<Demanda>> buildDemands(DemandaBloc bloc) {
    return StreamBuilder(
      stream: bloc.demandsStream,
      builder: (BuildContext context, AsyncSnapshot snapshot) {
        if (snapshot.hasError) {
          return Container(
            alignment: Alignment.center,
            child: Text(
              DESCRIPTION_SEARCH_ERROR.toUpperCase(),
              style: TextStyle(
                  color: Colors.blue,
                  fontSize: 16,
                  fontWeight: FontWeight.bold),
            ),
          );
        } else if (!snapshot.hasData) {
          bloc.loadData();
          return Center(child: CircularProgressIndicator());
        } else if (snapshot.data.isEmpty) {
          return Container(
            alignment: Alignment.center,
            child: Text(
              DESCRIPTION_DEMANDS_EMPTY,
              style: TextStyle(
                  color: Colors.blue,
                  fontSize: 16,
                  fontWeight: FontWeight.bold),
            ),
          );
        } else {
          return ListView.builder(
            itemCount: (snapshot.data.length * .5).round(),
            itemBuilder: (BuildContext context, int index) {
              int index1 = index * 2;
              int index2 = index * 2 + 1;
              if (index < snapshot.data.length) {
                return Row(
                  children: <Widget>[
                    DemandWidget(snapshot.data[index1]),
                    if (index2 < snapshot.data.length)
                      DemandWidget(snapshot.data[index2]),
                  ],
                );
              } else {
                return Container();
              }
            },
          );
        }
      },
    );
  }
}

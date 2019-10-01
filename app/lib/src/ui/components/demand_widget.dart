import 'package:flutter/material.dart';
import 'package:kara/src/models/demanda.dart';
import 'package:kara/src/utils/constants.dart';
import 'package:kara/src/utils/kara_themes.dart';

class DemandWidget extends StatelessWidget {
  final Demanda demanda;

  DemandWidget(this.demanda);

  @override
  Widget build(BuildContext context) {
    final _screenSize = MediaQuery.of(context).size;
    return Container(
      width: _screenSize.width * .5,
      child: Card(
        margin: EdgeInsets.symmetric(
          vertical: 7,
          horizontal: 5,
        ),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
        elevation: 3,
        child: Row(
          children: <Widget>[
            buildTimerContainer(),
            buildExpandedTexts(_screenSize),
          ],
        ),
      ),
    );
  }

  Container buildTimerContainer() {
    return Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.only(
          topLeft: Radius.circular(10),
          bottomLeft: Radius.circular(10),
        ),
        color: KaraThemes.secundaryColor[300],
      ),
      padding: EdgeInsets.all(10),
      width: 80,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[
          Text(
            'RESTAM',
            style: TextStyle(
              color: Colors.white,
            ),
            textAlign: TextAlign.center,
          ),
          Container(
            margin: EdgeInsets.symmetric(vertical: 10),
            child: Text(
              (demanda.quantidadeSolicitada - (demanda.quantidadeAlcancada ?? 0))
                  .toString(),
              style: TextStyle(
                fontSize: 20,
                color: Colors.white,
                fontWeight: FontWeight.bold,
              ),
              textAlign: TextAlign.center,
            ),
          ),
          Text(
            'PARA A META',
            style: TextStyle(
              color: Colors.white,
            ),
            textAlign: TextAlign.center,
          ),
        ],
      ),
    );
  }

  Expanded buildExpandedTexts(Size screenSize) {
    return Expanded(
      child: Container(
        margin: EdgeInsets.symmetric(vertical: 5, horizontal: 5),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Text(
              demanda.descricao.toUpperCase(),
              style: TextStyle(
                  color: KaraThemes.secundaryColor[300],
                  fontWeight: FontWeight.bold,
                  fontSize: 16),
            ),
            Container(
              margin: EdgeInsets.only(top: 5, bottom: 10),
              child: Text(
                'PARA ' + demanda.ong.nome,
                style: TextStyle(
                  color: Colors.grey[600],
                ),
              ),
            ),
            buildDonateButton(),
          ],
        ),
      ),
    );
  }

  Row buildDonateButton() {
    return Row(
      mainAxisAlignment: MainAxisAlignment.end,
      children: <Widget>[
        Container(
          height: 25,
          width: 70,
          child: RaisedButton(
            child: Text(
              DESCRIPTION_DONATE,
              style: TextStyle(
                color: Colors.white,
              ),
            ),
            color: KaraThemes.primaryColor[300],
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.all(Radius.circular(25)),
            ),
            onPressed: () {},
          ),
        ),
      ],
    );
  }
}

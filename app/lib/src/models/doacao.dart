import 'package:kara/src/models/usuario.dart';

import 'item_doacao.dart';

class Doacao {
  int id;
  Usuario usuario;
  String dataAgendamento;
  String dataConfimacao;
  List<ItemDoacao> itemDoacao;

  Doacao(
      {this.id,
      this.usuario,
      this.dataAgendamento,
      this.dataConfimacao,
      this.itemDoacao});

  Doacao.fromJson(Map<String, dynamic> json) {
    id = json['id'];
    usuario =
        json['usuario'] != null ? new Usuario.fromJson(json['usuario']) : null;
    dataAgendamento = json['data_agendamento'];
    dataConfimacao = json['data_confimacao'];
    if (json['item_doacao'] != null) {
      itemDoacao = new List<ItemDoacao>();
      json['item_doacao'].forEach((v) {
        itemDoacao.add(new ItemDoacao.fromJson(v));
      });
    }
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['id'] = this.id;
    if (this.usuario != null) {
      data['usuario'] = this.usuario.toJson();
    }
    data['data_agendamento'] = this.dataAgendamento;
    data['data_confimacao'] = this.dataConfimacao;
    if (this.itemDoacao != null) {
      data['item_doacao'] = this.itemDoacao.map((v) => v.toJson()).toList();
    }
    return data;
  }
}

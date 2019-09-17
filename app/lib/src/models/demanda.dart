import 'categoria.dart';
import 'ong.dart';

class Demanda {
  int id;
  Ong ong;
  Categoria categoria;
  double quantidadeSolicitada;
  double quantidadeAlcancada;
  String descricao;
  bool ativo;

  Demanda(
      {this.id,
      this.ong,
      this.categoria,
      this.quantidadeSolicitada,
      this.quantidadeAlcancada,
      this.descricao,
      this.ativo});

  Demanda.fromJson(Map<String, dynamic> json) {
    id = json['id'];
    ong = json['ong'] != null ? new Ong.fromJson(json['ong']) : null;
    categoria = json['categoria'] != null
        ? new Categoria.fromJson(json['categoria'])
        : null;
    quantidadeSolicitada = double.parse(json['quantidade_solicitada']);
    quantidadeAlcancada = double.parse(json['quantidade_alcancada']);
    descricao = json['descricao'];
    ativo = json['ativo'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['id'] = this.id;
    if (this.ong != null) {
      data['ong'] = this.ong.toJson();
    }
    if (this.categoria != null) {
      data['categoria'] = this.categoria.toJson();
    }
    data['quantidade_solicitada'] = this.quantidadeSolicitada;
    data['quantidade_alcancada'] = this.quantidadeAlcancada;
    data['descricao'] = this.descricao;
    data['ativo'] = this.ativo;
    return data;
  }
}
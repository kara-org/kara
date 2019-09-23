import 'categoria.dart';
import 'ong.dart';

class Demanda {
  int id;
  Ong ong;
  int idOng;
  Categoria categoria;
  int idCategoria;
  double quantidadeSolicitada;
  double quantidadeAlcancada;
  String descricao;
  bool ativo;

  Demanda(
      {this.id,
      this.ong,
      int idOng,
      this.categoria,
      int idCategoria,
      this.quantidadeSolicitada,
      this.quantidadeAlcancada,
      this.descricao,
      this.ativo});

  Demanda.fromJson(Map<String, dynamic> json) {
    id = json['id'];
    ong = json['ong'] != null ? new Ong.fromJson(json['ong']) : null;
    idOng = json['id_ong'];
    categoria = json['categoria'] != null
        ? new Categoria.fromJson(json['categoria'])
        : null;
    idCategoria = json['id_categoria'];
    quantidadeSolicitada = json['quantidade_solicitada'] == null
        ? null
        : double.parse(json['quantidade_solicitada'].toString());
    quantidadeAlcancada = json['quantidade_alcancada'] == null
        ? null
        : double.parse(json['quantidade_alcancada'].toString());
    descricao = json['descricao'];
    ativo = json['ativo'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['id'] = this.id;
    if (this.ong != null) {
      data['ong'] = this.ong.toJson();
    }
    data['id_ong'] = this.idOng;
    if (this.categoria != null) {
      data['categoria'] = this.categoria.toJson();
    }
    data['id_categoria'] = this.idCategoria;
    data['quantidade_solicitada'] = quantidadeSolicitada == null
        ? null
        : double.parse(quantidadeSolicitada.toString());
    data['quantidade_alcancada'] = quantidadeAlcancada == null
        ? null
        : double.tryParse(quantidadeAlcancada.toString());
    data['descricao'] = this.descricao;
    data['ativo'] = this.ativo;
    return data;
  }
}

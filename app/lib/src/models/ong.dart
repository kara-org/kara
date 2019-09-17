import 'endereco.dart';
import 'telefone.dart';

class Ong {
  int id;
  String nome;
  String cnpj;
  String historia;
  List<Telefone> telefone;
  bool ativo;
  Endereco endereco;

  Ong(
      {this.id,
      this.nome,
      this.cnpj,
      this.historia,
      this.telefone,
      this.ativo,
      this.endereco});

  Ong.fromJson(Map<String, dynamic> json) {
    id = json['id'];
    nome = json['nome'];
    cnpj = json['cnpj'];
    historia = json['historia'];
    if (json['telefone'] != null) {
      telefone = new List<Telefone>();
      json['telefone'].forEach((v) {
        telefone.add(new Telefone.fromJson(v));
      });
    }
    ativo = json['ativo'];
    endereco = json['endereco'] != null
        ? new Endereco.fromJson(json['endereco'])
        : null;
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['id'] = this.id;
    data['nome'] = this.nome;
    data['cnpj'] = this.cnpj;
    data['historia'] = this.historia;
    if (this.telefone != null) {
      data['telefone'] = this.telefone.map((v) => v.toJson()).toList();
    }
    data['ativo'] = this.ativo;
    if (this.endereco != null) {
      data['endereco'] = this.endereco.toJson();
    }
    return data;
  }
}
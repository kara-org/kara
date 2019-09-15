import 'endereco.dart';
import 'telefone.dart';

class Usuario {
  int id;
  String email;
  String nomeCompleto;
  bool ativo;
  String ultimoLogin;
  String cpf;
  Null foto;
  bool vinculoOng;
  Endereco endereco;
  List<Telefone> telefone;

  Usuario(
      {this.id,
      this.email,
      this.nomeCompleto,
      this.ativo,
      this.ultimoLogin,
      this.cpf,
      this.foto,
      this.vinculoOng,
      this.endereco,
      this.telefone});

  Usuario.fromJson(Map<String, dynamic> json) {
    id = json['id'];
    email = json['email'];
    nomeCompleto = json['nome_completo'];
    ativo = json['ativo'];
    ultimoLogin = json['ultimo_login'];
    cpf = json['cpf'];
    foto = json['foto'];
    vinculoOng = json['vinculo_ong'];
    endereco = json['endereco'] != null
        ? new Endereco.fromJson(json['endereco'])
        : null;
    if (json['telefone'] != null) {
      telefone = new List<Telefone>();
      json['telefone'].forEach((v) {
        telefone.add(new Telefone.fromJson(v));
      });
    }
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['id'] = id;
    data['email'] = email;
    data['nome_completo'] = nomeCompleto;
    data['ativo'] = ativo;
    data['ultimo_login'] = ultimoLogin;
    data['cpf'] = cpf;
    data['foto'] = foto;
    data['vinculo_ong'] = vinculoOng;
    if (endereco != null) {
      data['endereco'] = endereco.toJson();
    }
    if (telefone != null) {
      data['telefone'] = telefone.map((v) => v.toJson()).toList();
    }
    return data;
  }
}

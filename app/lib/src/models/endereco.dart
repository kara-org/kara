class Endereco {
  int id;
  String logradouro;
  String bairro;
  String cidade;
  String estado;
  int numero;
  bool principal;

  Endereco(
      {this.id,
      this.logradouro,
      this.bairro,
      this.cidade,
      this.estado,
      this.numero,
      this.principal});

  Endereco.fromJson(Map<String, dynamic> json) {
    id = json['id'];
    logradouro = json['logradouro'];
    bairro = json['bairro'];
    cidade = json['cidade'];
    estado = json['estado'];
    numero = json['numero'];
    principal = json['principal'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['id'] = this.id;
    data['logradouro'] = this.logradouro;
    data['bairro'] = this.bairro;
    data['cidade'] = this.cidade;
    data['estado'] = this.estado;
    data['numero'] = this.numero;
    data['principal'] = this.principal;
    return data;
  }
}

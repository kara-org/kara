class Status {
  int codigoStatus;
  String mensagem;

  Status({this.codigoStatus, this.mensagem});

  Status.fromJson(Map<String, dynamic> json) {
    codigoStatus = json['codigo_status'];
    mensagem = json['mensagem'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['codigo_status'] = this.codigoStatus;
    data['mensagem'] = this.mensagem;
    return data;
  }
}
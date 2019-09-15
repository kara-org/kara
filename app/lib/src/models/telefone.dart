class Telefone {
  int id;
  String numero;
  bool whatsapp;

  Telefone({this.id, this.numero, this.whatsapp});

  Telefone.fromJson(Map<String, dynamic> json) {
    id = json['id'];
    numero = json['numero'];
    whatsapp = json['whatsapp'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['id'] = this.id;
    data['numero'] = this.numero;
    data['whatsapp'] = this.whatsapp;
    return data;
  }
}
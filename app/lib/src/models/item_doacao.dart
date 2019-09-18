import 'demanda.dart';
import 'status.dart';

class ItemDoacao {
  int id;
  String quantidadePrometida;
  String quantidadeEfetivada;
  String dataAtualizacao;
  int doacao;
  Demanda demanda;
  Status status;

  ItemDoacao(
      {this.id,
      this.quantidadePrometida,
      this.quantidadeEfetivada,
      this.dataAtualizacao,
      this.doacao,
      this.demanda,
      this.status});

  ItemDoacao.fromJson(Map<String, dynamic> json) {
    id = json['id'];
    quantidadePrometida = json['quantidade_prometida'];
    quantidadeEfetivada = json['quantidade_efetivada'];
    dataAtualizacao = json['data_atualizacao'];
    doacao = json['doacao'];
    demanda =
        json['demanda'] != null ? new Demanda.fromJson(json['demanda']) : null;
    status =
        json['status'] != null ? new Status.fromJson(json['status']) : null;
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['id'] = this.id;
    data['quantidade_prometida'] = this.quantidadePrometida;
    data['quantidade_efetivada'] = this.quantidadeEfetivada;
    data['data_atualizacao'] = this.dataAtualizacao;
    data['doacao'] = this.doacao;
    if (this.demanda != null) {
      data['demanda'] = this.demanda.toJson();
    }
    if (this.status != null) {
      data['status'] = this.status.toJson();
    }
    return data;
  }
}

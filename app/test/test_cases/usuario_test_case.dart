class UsuarioTestCase {
  static const Map<String, dynamic> jsonUsuario = {
    "id": 2,
    "email": "j_kelvin1997@hotmail.com",
    "nome_completo": "Jonathan Kelvin",
    "ativo": true,
    "ultimo_login": "2019-09-05T14:56:20.303571Z",
    "cpf": "06382375560",
    "foto": null,
    "vinculo_ong": true,
    "endereco": {
      "id": 1,
      "logradouro": "Avenida Doutor José Thomas D'Ávila Nabuco",
      "bairro": "Farolândia",
      "cidade": "Aracaju",
      "estado": "SE",
      "numero": 155,
      "principal": false
    },
    "telefone": [
      {"id": 3, "numero": "999999999", "whatsapp": true}
    ],
    "ong": {
      "id": 1,
      "nome": "GAAC",
      "cnpj": "00.000.000/0001-91",
      "historia": "Historia",
      "telefone": [
        {"id": 1, "numero": "22222222222", "whatsapp": false},
        {"id": 2, "numero": "33333333333", "whatsapp": true}
      ],
      "ativo": true,
      "endereco": {
        "id": 1,
        "logradouro": "Avenida Doutor José Thomas D'Ávila Nabuco",
        "bairro": "Farolândia",
        "cidade": "Aracaju",
        "estado": "SE",
        "numero": 155,
        "principal": false
      }
    }
  };
}

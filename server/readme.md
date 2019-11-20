# Kara API

O Kara API é o serviço que gerencia usuários e ongs do sistema Kara, assim como permite que o sistema realize o processo de criação de demandas e sinalizações dos desejos de realizar doações entre os usuários e ongs presentes no sistema.

### Desenvolvido usando
Este projeto foi desenvolvido utilizando as seguintes ferramentas:

* [Django](https://www.djangoproject.com/) - O framework usado como base.
* [Django Rest Framework](https://www.django-rest-framework.org/) - A ferramenta utilizada para construção da API Rest.


## Getting Started

1. Clone o repo
```sh
git clone https://github.com/DCOMP-UFS/PRATICAS.kara.git
```

2. Entre na pasta da API
```sh
cd server/
```

3. Crie sua virtualenv (opcional)

Para a criação da virtualenv, utilize a ferramenta de sua preferência. 

- Pode ser o [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest):
```sh
mkvirtualenv kara-api
```
- Pode ser também utilizando o [virtualenv](https://virtualenv.pypa.io/en/latest/)
```sh
virtualenv kara-api
```

4. Instale as dependências

Uma vez estando no diretório server/ :
```sh
pip install -r requirements/common.txt
```

### Pré-requisitos

Essa é a listagem das rependências do projeto, porém elas são automaticamente instaladas ao realizar o passo 4 do menu Getting Started.

- Django==2.2
- django-cors-headers==3.0.2
- djangorestframework==3.9.4
- djangorestframework-jwt==1.11.0
- Pillow==6.0.0
- PyJWT==1.7.1

## Contribuições

1. Fork o projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Adicionei uma nova feature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Autores do Kara API

* **Mayara Machado** -  [MayaraMachado](https://github.com/MayaraMachado)
* **Pedro Daltro** - [pedrodaltro](https://github.com/pedrodalt)

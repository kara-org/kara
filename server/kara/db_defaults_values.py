#abra o shell com o comando:
#>> python manage.py shell
#e execute o código a seguir

from doacoes.models import Categoria, StatusItemDoacao

StatusItemDoacao.objects.bulk_create(
    [ 
        StatusItemDoacao(codigo_status=1, mensagem="Pendente"),
        StatusItemDoacao(codigo_status=2, mensagem="Cancelada"),
        StatusItemDoacao(codigo_status=3, mensagem="Confirmada")
    ] 
)

Categoria.objects.bulk_create(
    [
        Categoria(descricao="Alimentos"),
        Categoria(descricao="Roupas"),
        Categoria(descricao="Móveis"),
        Categoria(descricao="Saúde"),
        Categoria(descricao="Serviços"),
        Categoria(descricao="Dinheiro"),
        Categoria(descricao="Eletrodoméstico"),
        Categoria(descricao="Aparelhos tecnológicos"),
    ]
)
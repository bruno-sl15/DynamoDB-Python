import boto3

def inserir_filme(titulo, ano, diretor, generos):
    dynamodb = boto3.resource('dynamodb')
    tabela = dynamodb.Table('Filmes')
    tabela.put_item(
        Item={
            'titulo': titulo,
            'ano': ano,
            'diretor': diretor,
            'generos': generos
        }
    )

inserir_filme(
    'Bacurau',
    2019,
    ['Kleber Mendonça Filho', 'Juliano Dornelles'],
    ['Western', 'Suspense', 'Terror', 'Misterio', 'Aventura']
)
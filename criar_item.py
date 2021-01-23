import boto3


def inserir_filme(titulo, ano, diretor, generos):
    dynamodb = boto3.resource('dynamodb')
    tabela = dynamodb.Table('Filmes')
    tabela.put_item(
        Item={
            'Titulo': titulo,
            'Ano': ano,
            'Diretor': diretor,
            'Generos': generos
        }
    )


inserir_filme('Apocalypse Now', 1979, 'Francis Ford Coppola', ['Drama', 'Guerra'])
inserir_filme('Parasita', 2019, 'Bon Joon-ho', 'Drama')


from pprint import pprint
import boto3

def ler_filme(titulo, ano):
    dynamodb = boto3.resource('dynamodb')
    tabela = dynamodb.Table('Filmes')
    resposta = tabela.get_item(
        Key={
            'titulo': titulo,
            'ano': ano
        }
    )
    return resposta

filme = ler_filme('Parasita', 2019)
if 'Item' in filme:
    print("Filme encontrado:")
    pprint(filme['Item'])
else:
    print('Filme não consta na base de dados')
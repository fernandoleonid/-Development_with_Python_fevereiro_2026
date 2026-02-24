import requests

def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'erro' in data:
            return {'erro':'CEP não encontrado'}
        else:
            return data
    else:
        return {'erro':'CEP Invalido!'}



cep  = input('Digite um cep para pesquisa: ')
info = consultar_cep(cep)

print ('#'*20)
print (f'CEP: {info["cep"]}')
print (f'Logradouro: {info["logradouro"]}')
print (f'Bairro: {info["bairro"]}')
print (f'Cidade: {info["localidade"]}')
print (f'Estado: {info["estado"]}')

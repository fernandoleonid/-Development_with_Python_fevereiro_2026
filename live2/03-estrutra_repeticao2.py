senha_cadastrada = '123'
senha_digitada = input('Digite sua senha para entra: ')

while senha_cadastrada != senha_digitada:
    print ('Senha incorreta, tente novamente!')
    senha_digitada = input('Digite sua senha para entra: ')
    
print ('Entrando no sistema...')
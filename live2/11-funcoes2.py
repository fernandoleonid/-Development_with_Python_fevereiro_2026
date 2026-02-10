
def pegar_numeros ():
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))
    return [numero1, numero2]

opcao = None
while opcao != '0':
    print ('1 - Adição')
    print ('2 - Subtração')
    print ('3 - Multiplicação')
    print ('4 - Divisão')
    print ('0 - Sair')
    opcao = input ('Escolha uma opção: ')
    
    if opcao == '1':
        numero1, numero2 = pegar_numeros()
        resposta = numero1 + numero2
        print (resposta)
    elif opcao == '2':
        numero1, numero2 = pegar_numeros()
        resposta = numero1 - numero2
        print (resposta)
    elif opcao == '3':
        numero1, numero2 = pegar_numeros()
        resposta = numero1 * numero2
        print (resposta)
    elif opcao == '4':
        numero1, numero2 = pegar_numeros()
        resposta = numero1 / numero2
        print (resposta)
    elif opcao == '0':
        print ('Saindo do Sistema...')
    else:
        print ('Opção errada tente novamente...')

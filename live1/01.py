nome = input ('Digite seu nome: ')
nota1 = int(input ('Digite a primeira nota: '))
nota2 = int(input ('Digite a segunda nota: '))

soma = nota1 + nota2
media = soma / 2


if media >= 5:
    print (f'{nome} sua média é {media} e voce está Aprovado')
else:
    print (f'{nome} sua média é {media} e voce está Reprovado')
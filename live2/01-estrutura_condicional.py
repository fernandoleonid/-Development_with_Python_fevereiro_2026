tempo = int(input('Digite a quantidade de anos de trabalho: '))

if tempo > 8:
    print ('Sênior')
elif tempo > 5:
    print ('Pleno')
else:
    print ('Junior')
alunos = [
    {
        'nome': 'Ana', 
        'Nota':8, 
        'uf': 'sp'
    }, 
    {
        'nome': 'Pedro', 
        'Nota':3, 
        'uf': 'rj'
    }, 
    {
        'nome': 'Maria', 
        'Nota':1, 
        'uf': 'MG'
    }
]

for aluno in alunos:
    print (aluno)

print ('#'*50)
alunos.append ( {'nome': 'Fernando', 'nota': 2, 'uf': 'SP'})

for aluno in alunos:
    print (aluno)
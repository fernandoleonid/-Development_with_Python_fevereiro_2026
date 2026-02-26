import sqlite3

conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
               id INTEGER  PRIMARY KEY AUTOINCREMENT,
               titulo TEXT NOT NULL,
               feita INTEGER DEFAULT 0
            )
""")

conn.commit()

def adicionar():
    titulo_digitado = input('Digite o titulo da tarefa: ')
    cursor.execute('INSERT INTO tarefas (titulo) VALUES (?)',(titulo_digitado,))
    conn.commit()
    print (f'------  {titulo_digitado}  Cadastrada!!!  ------')

def listar():
    cursor.execute('SELECT * FROM tarefas')
    tarefas = cursor.fetchall()
    print (f'Código |   Tarefa   | Concluido')
    print ('-'*30)
    for tarefa in tarefas:
        if tarefa[2] == 0:
            estado = 'Pendente'
        else:
            estado = 'Concluido'
        print (f'{tarefa[0]:<6} | {tarefa[1]:<10} | {estado} ')

def concluir() :
    listar()
    id_digitado = input ('Escolha um Id da tarefa para concluir: ')
    cursor.execute('SELECT * FROM tarefas WHERE id = ?', (id_digitado,))
    tarefa = cursor.fetchall()
    if tarefa == []:
        print ('Tarefa não encontrada!')
        return
    
    cursor.execute('UPDATE tarefas SET feita = 1 WHERE id = ?', (id_digitado,))
    conn.commit()
    print ('Tarefa atualizada com sucesso!')


def deletar():
    listar()
    id_digitado = input ('Digite ID da tarefa para deletar: ')
    cursor.execute('SELECT * FROM tarefas WHERE id = ?', (id_digitado,))
    tarefa = cursor.fetchall()
    if tarefa == []:
        print ('Tarefa não encontrada!')
        return
    
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (id_digitado,))
    conn.commit()
    print ('Tarefa removida com sucesso!!!')

def menu():
    while True:
        print ('TODO LIST')
        print ('1 - Adicionar tarefa')
        print ('2 - Listar tarefas')
        print ('3 - Concluir tarefa')
        print ('4 - Deletar tarefa')
        print ('0 - Sair')

        opcao = input('Escolha uma opção:')
        
        if opcao == '1':
            adicionar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            concluir()
        elif opcao == '4':
            deletar()
        elif opcao == '0':
            print ('Saindo do sistema...')
            break
        else:
            print ('Opção invalida, tente novamente!')


menu()

import sqlite3

conexao = sqlite3.connect("data/data.db") 
cursor = conexao.cursor() 

def listing():
    print("\nLista de Tarefas")
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        id,task,status = task
        print(f"{id}- {task}: {status}")

def add_tasks():
    while True:
        add_task = input("Digite a tarefa: ").lower()
        add_task = add_task.title()
        add_status = input("Digite o status da tarefa: ").lower()
        add_status = add_status.title()
        cursor.execute("INSERT INTO tasks(tarefas, status) VALUES(?, ?)",(add_task, add_status))
        conexao.commit()
        proceed = read_int("Deseja adiciona mais tarefas?\n1-SIM\n2-NÃO\n")
        if proceed == 2:
            break

def update():
    while True:
        select_task= read_int("Digite o numero da tarefa: ")
        option = read_int("Deseja alteral o nome ou status?\n1-Nome\n2-Status\n ")
        if option == 1:
            up_task = input("Digite o Nome da tarefa: ").lower()
            up_task = up_task.title()
            cursor.execute("""UPDATE tasks 
                           SET tarefas = ?
                           WHERE id = ? 
                           """,(up_task, select_task))
            conexao.commit()
            print("Nome alterado com sucesso!\n")
            break 
        elif option == 2:
            up_status = input("Digite o Status da tarefa: ").lower()
            up_status = up_status.title()
            cursor.execute("""UPDATE tasks 
                           SET status = ?
                           WHERE id = ? 
                           """,(up_status, select_task))
            conexao.commit()
            print("Status altereado com sucesso!\n")
            break
        else:
            print("Digite uma opção valida!")

def delete():
    while True:
        delete = read_int("Digite o número da tarefa: ")
        confirmation = read_int("Confirmar exclusão?: \n1-Sim\n2-Não\n")
        if confirmation == 1:
            cursor.execute("DELETE FROM tasks WHERE id = ?",(delete,))
            conexao.commit()
            print("Tarefa excluida com sucesso!\n")
            break
        elif confirmation == 2:
            print("Exclusão cancelada!")
            break
        else:
            print("choice uma opção valida!")
            
def read_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Digite apenas números!")

while True:
    print("LISTA DE TAREFAS")
    print("1- Listar tarefas\n2- Adicionar Tarefa\n3- Editar Tarefa\n4- Excluir Tarefa\n5- Sair")
    choice = read_int("Selecione uma opção: ")
    if choice == 1:
        listing()
    elif choice == 2:
        add_tasks()
    elif choice == 3:
        update()
    elif choice == 4:
        delete()
    elif choice == 5:
        print("Até a proxima!")
        break
    else:
        print("selecione uma opção valida\n")
        
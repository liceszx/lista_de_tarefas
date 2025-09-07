def adicionar_tarefa(lista_de_tarefas, tarefa):
    """Adiciona nova tarefa a uma lista pré-existente"""
    lista_de_tarefas.append(tarefa)
    print("-->> Tarefa adicionada com sucesso!")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    """Exibe lista de tarefas númeradas"""
    print("-" * 50)
    print(f"{' ' * 15}Lista de Tarefas")
    print("-" * 50)
    n = 1
    for tarefa in lista_de_tarefas:
        print(f"{n} - {tarefa}")
        n += 1
    print("-" * 50)

def deletar_tarefa(lista_de_tarefas, tarefa):
    """Deleta tarefa de uma lista pré-existente a partir do número dela"""
    lista_de_tarefas.pop((tarefa - 1))
    print("-" * 10)
    print("--> Tarefa deletada com sucesso!!")
    print("\n")
    return lista_de_tarefas

def exibir_menu():
    """Exibe menu com opções para o usuárie"""
    print("Escolha uma opção:\n" 
          "1- Inserir nova tarefa\n"
          "2- Listar tarefas\n"
          "3- Deletar tarefa\n" 
          "4- Sair"
    )
    print("-" * 50)

# variáveis
lista_de_tarefas = []
continuar = True

# cabeçalho do programa
print("-" * 50)
print(f"{' ' * 5}Seja bem-vinde à sua lista de tarefas!!")
print("-" * 50)

# loop principal
while continuar:
    exibir_menu()
    escolha = input("Insira o que deseja fazer: \n")
    print(" " * 50)

    if escolha == "1":
        tarefa = input('Insira uma nova tarefa: \n')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif escolha == "2":
         listar_tarefas(lista_de_tarefas)
    elif escolha == "3":
        # valida e verifica se o valor é numérico e se está dentro do limite da lista
        tarefa = input('Insira o número da tarefa que deseja deletar: ')
        if not tarefa.isnumeric():
            print('Valor dado não é um número! Tente novamente. ')
        elif int(tarefa) > len(lista_de_tarefas) or int(tarefa) <= 0:
            print('--> Número inválido! Tente novamente. ')
        else:
            deletar_tarefa(lista_de_tarefas, int(tarefa))
    elif escolha == "4":
        print(f"{'=' * 5}> LISTA ENCERRADA <{'=' * 5}")
        continuar = False
    else:
        print('Opção inválida! Por favor, tente novamente.')
    print('\n')
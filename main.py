print('================= LISTAS DE TAREFAS =================')

junção = []

#MOSTRA O MENU
def menu():
    while True:
        mostrar = input(''' 
        1 - VER TAREFAS
        2 - CRIAR TAREFA
        3 - EXCLUIR TAREFA
        4 - ALTERAR TAREFA
        5 - SAIR
        ==> ''')

        if mostrar == '1':
            listar(junção)
        elif mostrar == '2':
            criar_tarefa(junção)
        elif mostrar == '3':
            excluir_tarefa(junção)
        elif mostrar == '4':
            print("Função alterar ainda não criada.")  
        elif mostrar == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")


def listar(junção):
    for i, tarefa in enumerate(junção, start=1):
        print(f'{i}. {tarefa['tarefa']}')
    



def criar_tarefa(junção):
     pedirtarefa = input('digite a tarefa: ')
     descrição = input('digite a descrição: ')
     prioridade = input('''
    ======= PRIORIDADE =======
                        
        1 - URGENTE
        2 - ALTA
        3 - MÉDIA
        4 - BAIXA
        
        ==> ''')
     categoria = input('''
    ===== CATEGORIA =====
        
        1 - INDIVIDUAL
        2 - LAZER
        3 - TRABALHO
        4 - FILHOS
                       
    ===> ''')
     
     tarefa = {
          'tarefa': pedirtarefa,
          'descrição': descrição,
          'prioridade': prioridade,
          'categoria': categoria 
     }

     junção.append(tarefa)
     print('======= TAREFA ADICIONA A LISTA =======')
     for chave, valor in tarefa.items():
          print(f'{chave} == {valor}')


def excluir_tarefa(junção):
    print('Tarefas atuais:')
    for i, tarefa in enumerate(junção):
        print(f"{i+1} - {tarefa['tarefa']}")
    indice = int(input('Digite o número da tarefa que quer excluir: ')) - 1
    if 0 <= indice < len(junção):
        removida = junção.pop(indice)
        print(f"Tarefa '{removida['tarefa']}' removida com sucesso!")
    else:
        print("Número inválido.")

menu()

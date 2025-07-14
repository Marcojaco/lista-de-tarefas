print('LISTA DE TAREFAS')

Alista = ['lavar prato', 'almoçar', 'tomar banho']
print(Alista)

while(True):

if add == 'sair':
    print('tchaul')
    break


elif add == 'adicionar':
    Aadd = input('o que você quer add? : ')
    Alista.append(Aadd)
    print(f'{Aadd} foi adicionado a sua lista')
    print(Alista)
    

elif add == 'remover':
    remove = input('o que você quer tirar : ')
    Alista.remove(remove)
    print(f'{remove} foi banido/removido da sua lista')
    print(Alista)
    

else:
    print('ENTÃO OQ VC QUER?')

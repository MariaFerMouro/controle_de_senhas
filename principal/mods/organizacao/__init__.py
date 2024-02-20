from principal.mods.erro import erro
from principal.mods.funcao import *
from time import sleep
def menu():
    print('\033[:33m='*40)
    print('\033[:34m1 - Fazer login'
          '\n2 - Cadastrar-se'
          '\n3 - banco de dados (administrador)\033[m')
    print('\033[:33m=' * 40)
    y = erro('Digite sua opção: ')
    if y == 1:
        print('fazer login')
    if y == 2:
        sleep(1)
        user()
        sleep(1)
        senha()
    if y == 3:
        print('banco de dados')
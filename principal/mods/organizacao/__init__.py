from principal.mods.erro import erro
from principal.mods.funcao import *
from time import sleep
def menu():
    while True:
        print('\033[:33m='*40)
        print('\033[:34m1 - Fazer login'
              '\n2 - Cadastrar-se'
              '\n3 - banco de dados (administrador)'
              '\n4 - Sair\033[m')
        print('\033[:33m=' * 40)
        y = erro('Digite sua opção: ')
        if y == 1:
            login()
        if y == 2:
            sleep(1)
            user()
            sleep(1)
            senha()
        if y == 3:
            acesso = input('Senha do administrador: ').strip()
            resultado = '12345'
            if acesso == resultado:
                contador = 0
                numuser = 0
                banco = r"C:/Users/Maria Fernanda/PycharmProjects/gerador_de_senhas/principal/banco_de_dados.txt"
                with open(banco, "r") as linhas:
                    usuarios = linhas.readlines()
                    print('\033[:33m='*40)
                    print(f'{"N°":<5}',f'{"Username":<20}', 'Senha' )
                    for cn in usuarios:
                        contador += 1
                        if contador % 2 == 0: #senhas
                            numuser += 1
                            senhas = cn
                            print(f'\033[34m{numuser:<5}', f'\033[m{contrabarran(username):<20}', contrabarran(senhas))
                        else:#username
                            username = cn

                    print('\033[:33m=' * 40)
                    sleep(3)
            else:
                print('\033[31mSenha incorreta!')
        if y == 4:
            print('Obrigado pelo acesso, volte logo!')
            break
def senha():
    from time import sleep
    '''
    Verifica se a senha está nos padrões exijidos e cadastra no banco de dados
    :return: none
    '''
    print('\033[:31m* Sua senha deve conter no mínimo: '
          '\n8 caractéres; '
          '\n2 letras maiúsculas; '
          '\n1 caractére especial (!@#$%&*);'
          '\n2 números; '
          '\nNÃO PODENDO CONTER ESPAÇOS. \033[m')
    sleep(2)
    while True:
        print (f'\033[:34mSugestão de senha forte: {gerador()}\033[m')
        x = input('Escolha a sua senha:')
        cont = num =mai =esp = 0
        if ' ' in x:
            print('O sistema não aceita espaços na senha.')
            continue
        else:
            for c in x:
                if c.isnumeric():
                    num += 1
                if c.isupper():
                    mai += 1
                if especiais(c):
                    esp += 1
                cont += 1

        if num < 2:
            print('\033[:31mSua senha precisa ter dois ou mais números\033[m')
            continue
        if cont < 8:
            print('\033[:31mSua senha precisa ter 8 ou mais caractéries\033[m')
            continue
        if mai < 2:
            print('\033[:31mSua senha precisa ter 2 ou mias letras maiúsculas\033[m')
            continue
        if esp == 0:
            print('\033[:31mSua senha precisa ter pelo menos 1 caractere especial\033[m')
            continue
        break
    with open("banco_de_dados.txt", "a") as senhas:
        senhas.write(f"\n{x}")
    print('\033[32mSua senha foi cadastrada!\033[m')
def user():
    banco =r"C:/Users/Maria Fernanda/PycharmProjects/gerador_de_senhas/principal/banco_de_dados.txt"
    while True:
        x = input('\033[mEscolha um nome de usuário: ').strip().capitalize()
        with open(banco, "r") as use:
            numuser = len(use.readlines())
            if numuser == 0:
                with open(banco, "w") as primeiro_user:
                    primeiro_user.write(x)
                break
            else:
                igual = 0
                contador = 0
                with open(banco, "r") as linhas:
                    linha = linhas.readlines()
                    for lin in linha:
                        contador += 1
                        resto = contador % 2
                        if resto != 0:
                            if contrabarran(lin) == x:
                                igual += 1
                    if igual == 0:
                        with open(banco, "a") as outros_users:
                            outros_users.write(f'\n{x}')
                        print('\033[32mNome adicionado com sucesso!')
                        break
                    if igual > 0:
                        print('\033[31mEsse nome de usuário já existe, tente outro!\033[m')
                        continue

def especiais(a):
    cont = 0
    while True:
        if '!' in a:
            cont += 1
        if '@' in a:
            cont += 1
        if '#' in a:
            cont += 1
        if '$' in a:
            cont += 1
        if '%' in a:
            cont += 1
        if '&' in a:
            cont += 1
        if '*' in a:
            cont += 1
        if '+' in a:
            cont += 1
        if '=' in a:
            cont += 1
        if '-' in a:
            cont += 1
        if '_' in a:
            cont += 1
        if ':' in a:
            cont += 1
        if ';' in a:
            cont += 1
        if '.' in a:
            cont += 1
        if ',' in a:
            cont += 1
        if '<' in a:
            cont += 1
        if '>' in a:
            cont += 1
        if '?' in a:
            cont += 1
        if '/' in a:
            cont += 1
        if '°' in a:
            cont += 1
        if cont > 0:
            return True
        if cont == 0:
            return False
def contrabarran(a):
    if '\n' in a:
        return a.replace('\n', '')
    else:
        return a


def login():
    user = input('Nome de usuário:').strip().capitalize()
    senha = input('Senha:').strip()
    banco = r"C:/Users/Maria Fernanda/PycharmProjects/gerador_de_senhas/principal/banco_de_dados.txt"
    with open(banco, 'r') as infos:
        linhas = infos.readlines()
        contador = 0
        semcadastro = 0
        for c in linhas:
            contador += 1
            if contador % 2 != 0:
                if contrabarran(c) == user:
                    if senha == contrabarran(linhas[contador]):
                        print('\033[32mBem vindo ao sistema!\033[m')
                        break
                    else:
                        print('\033[31mA senha não condiz com o usuário!\033[m')
                        break
                else:
                    semcadastro += 1
        if semcadastro == (len(linhas)) / 2:
            print('\033[31mEsse usuário não existe!\033[m')
def gerador():
    from random import sample, choice
    lista = sample(range(1,11), 10)
    senha = list()
    while True:
        for num in lista:
            if num == 1:
                lista1 = ['!','@','#','$','%','&','*','+','=','-','_',':',';','.',',','<','>','?','/','°']
                senha.append(choice(lista1))
            if num == 2:
                lista2 = ['!','@','#','$','%','&','*','+','=','-','_',':',';','.',',','<','>','?','/','°']
                senha.append(choice(lista2))
            if num == 3:
                lista3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                senha.append(choice(lista3))
            if num == 4:
                lista4 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                senha.append(choice(lista4))
            if num == 5:
                lista5 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                senha.append(choice(lista5))
            if num == 6:
                lista6 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                senha.append(choice(lista6))
            if num == 7:
                lista7 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                senha.append(choice(lista7))
            if num == 8:
                lista8 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                senha.append(choice(lista8))
            if num == 9:
                lista9 = ['1','2','3','4','5','6','7','8','9']
                senha.append(choice(lista9))
            if num == 10:
                lista10 = ['1','2','3','4','5','6','7','8','9']
                senha.append(choice(lista10))

        string = ''.join(senha)
        contador = 0
        igual = 0
        banco = r"C:/Users/Maria Fernanda/PycharmProjects/gerador_de_senhas/principal/banco_de_dados.txt"
        with open(banco, "r") as linhas:
            linha = linhas.readlines()
            for lin in linha:
                contador += 1
                if contador % 2 == 0:
                    if contrabarran(lin) == string:
                        igual += 1
        if igual == 0:
            return string
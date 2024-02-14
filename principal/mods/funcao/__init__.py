def senha():
    print('\033[:31m* Sua senha deve conter no mínimo: '
          '\n8 caractéres; '
          '\n2 letras maiúsculas; '
          '\n1 caractére especial (!@#$%&*);'
          '\n2 números; '
          '\nNÃO PODENDO CONTER ESPAÇOS. \033[m')
    while True:
        x = input('Escolha a sua senha:')
        cont = 0
        num = 0
        mai = 0
        esp = 0
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
            print('Sua senha precisa ter dois ou mais números')
            num = False
        else:
            num = True
        if cont < 8:
            print('Sua senha precisa ter 8 ou mais caractéries')
            cont = False
        else:
            cont = True
        if mai < 2:
            print('Sua senha precisa ter 2 ou mias letras maiúsculas')
            mai = False
        else:
            mai = True
        if esp == 0:
            print('Sua senha precisa ter pelo menos 1 caractere especial')
            esp = False
        else:
            esp = True
        print(cont, num, mai, esp)

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


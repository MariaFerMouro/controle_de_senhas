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


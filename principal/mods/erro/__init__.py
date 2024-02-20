def erro(a):
    while True:
        x = input(a)
        try:
            y = int(x)
        except(TypeError, ValueError):
            print(f'\033[31mO programa não aceita o valor "{x}", tente novamente!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033Você interrompeu o programa!\033[m')
        if 0 < y < 4:
            return y
        else:
            print('\033Esse comando não exisite!\033[m')
            continue
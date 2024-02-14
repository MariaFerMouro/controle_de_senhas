def erro(a):
    while True:
        x = input(a)
        try:
            y = int(x)
        except(TypeError, ValueError):
            print(f'O programa não aceita o valor "{x}", tente novamente!')
            continue
        except(KeyboardInterrupt):
            print('Você interrompeu o programa!')
        if 0 < y < 4:
            return y
        else:
            print('Esse comando não exisite!')
            continue
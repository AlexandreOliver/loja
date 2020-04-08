
def cor(name):
    cores = {'pausa': '\033[m',
             'preto': '\033[;;30m',
             'vermelho': '\033[;;31m',
             'verde': '\033[;;32m',
             'amarelo': '\033[;;33m',
             'azul': '\033[;;34m',
             'roxo': '\033[;;35m',
             'azul claro': '\033[;;36m',
             'cinza': '\033[;;37m'}
    if name in cores.keys():
        c = cores[name]

    else:
        c = "Cor não registrada"

    return c




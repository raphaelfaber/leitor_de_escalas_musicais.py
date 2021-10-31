from acessorios import*
import os
from time import sleep
while True:
    texto('Bem vindo ao gerador de escalas musicais!')
    print("""Para usar esse programa considere:
    C - Dó
    D - Ré
    E - Mí
    F - Fá
    G - Sol
    A - Lá
    B - Si""",end='\n')
    p=escalador()
    sleep(0.5)
    linha()
    escalamaior(p)
    linha()
    sleep(1)
    escalamenor(p)
    linha()
    sleep(1)
    harmonicomaior(p)
    linha()
    try:
        q = str(input('Deseja sair?')).lower()
    except:
        print(('Digite uma opção válida!'))
    else:
        if q in 'sy':
            break
        else:
            continue

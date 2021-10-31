def escalador():
    notas = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    notasr = []
    while True:
        p = input('Digite uma nota musical: ').upper()
        if p not in 'A#B#C#D#E#F#G#':
            print('Nota musical inválida')
            try:
                p = str(input('Digite uma nota válida: ')).upper()
            except:
                print('Nota digitada inválida')
            break
        else:
            break
    for nota in range(0,15):
        if notas[nota] == p:
            posicao = nota
            break
    for c in range (posicao,posicao+12):
        notasr.append(notas[c])
    notasr = notasr*2
    return notasr


def escalamaior(notasr):
      print(f'A escala maior de {notasr[0]} é:\n {notasr[0]} - {notasr[0+2]} - {notasr[0+4]} - {notasr[0+5]} - {notasr[0+7]} - {notasr[0+9]} - {notasr[0+11]} ')


def escalamenor(notasr):
    print(f'A escala menor de {notasr[0]} é:\n {notasr[0]} - {notasr[0 + 2]} - {notasr[0 + 3]} - {notasr[0 + 5]} - {notasr[0 + 7]} - {notasr[0 + 8]} - {notasr[0 + 10]}')


def harmonicomaior(notasr):
    print(f'O campo hamônico maior do {notasr[0]} é:\n {notasr[0]} - {notasr[0+2]}m - {notasr[0+4]}m - {notasr[0+5]} - {notasr[0+7]} - {notasr[0+9]}m - {notasr[0+11]}º ')


def texto(mensagem,tamanho=50):
    print( '=' * tamanho)
    print(f'{mensagem:^{tamanho}}')
    print( '=' * tamanho)


def linha(tamanho=50):
    print('-'*tamanho)
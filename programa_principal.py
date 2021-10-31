notas = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
notasr = []
try:
    while True:
        p = str(input('digite uma nota musical: ')).upper()
        if p not in 'A#B#C#D#E#F#G#':
            print('Nota musical inválida')
            continue
        else:
            break
except:
    print('Nota musical inválida')
for nota in range(0,15):
    if notas[nota] == p:
        posição = nota
        break
for c in range (posição,posição+12):
    notasr.append(notas[c])
notasr = notasr*2
print(f'A escala maior de {notasr[0]} é: {notasr[0]} {notasr[0+2]} {notasr[0+4]} {notasr[0+5]} {notasr[0+7]} {notasr[0+9]} {notasr[0+11]} ')
print(f'A escala menor de {notasr[0]} é: {notasr[0]} {notasr[0+2]} {notasr[0+3]} {notasr[0+5]} {notasr[0+7]} {notasr[0+8]} {notasr[0+10]}')
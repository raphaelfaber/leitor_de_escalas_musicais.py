notas = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
p = str(input('digite uma nota musical: '))
for nota in range(0,(len(notas)/2)+1):
    if p == nota:
        p = notas[nota]
print(nota)
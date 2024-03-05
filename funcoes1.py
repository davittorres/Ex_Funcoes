
nota1 = float(input('Digite sua nota no 1 bimestre: '))
nota2 = float(input('Digite sua nota no 2 bimestre: '))
nota3 = float(input('Digite sua nota no 3 bimestre: '))
nota4 = float(input('Digite sua nota no 4 bimestre: '))

def calcular_media():
    calcular = (nota1 + nota2 + nota3 + nota4) / 4
    return calcular

def verificar_situacao():
    media = calcular_media()
    if media < 7:
        print('Aluno reprovado!!!')
    elif media == 10:
        print('Parabens voce e nota 10')
    else:
        print('Aluno Aprovado!!')



verificar_situacao()


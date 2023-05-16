idiomas = float(input('Informe a quantia de horas em idiomas: '))
eventos = float(input('Informe a quantia de horas em eventos: '))
visitas = float(input('Informe a quantia de horas em visitas: '))
extensao = float(input('informe a quantia de horas em extensao: '))

total = (idiomas + eventos) + (visitas + extensao)


if idiomas >= 40:
    idiomas = 40
    print(f'O total de horas validas em curso de idiomas é: {idiomas:.2f}')
else:
    idiomas = idiomas
    print(f'O total de horas validas em curso de idiomas é: {idiomas:.2f}')
if eventos >= 40:
    eventos = 40
    print(f'O total de horas validas em eventos é: {eventos:.2f}')
else:
    eventos = eventos
    print(f'O total de horas validas em eventos é: {eventos:.2f}')
if visitas >= 20:
    visitas = 20
    print(f'O total de horas validas em visistas é: {visitas:.2f}')
else:
    visitas = visitas
    print(f'O total de horas validas em visistas é: {visitas:.2f}')
if extensao >= 80:
    extensao = 80
    print(f'O total de horas validas em extensao é: {extensao:.2f}')
else:
    extensao = extensao
    print(f'O total de horas validas em extensao é: {extensao:.2f}')

print(f'A soma total de horas é: {total:.2f}')

horas_validas = (idiomas + eventos) + (visitas + extensao)
print(f'O total da soma de horas validas é de: {horas_validas:.2f}')

if horas_validas >= 100:
    print('Voce atingiu o minimo de horas necessárias!')
else:
    print('Você não atingiu o minimo de horas necessárias!')

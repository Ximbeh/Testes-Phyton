# while True:
#     i = input('Please enter an integer (0 to exit):\n')
#     i = int(i)
#     if i == 0:
#         print("Exiting the Program")
#         break
#     print(f'{i} square is {i ** 2}')

nEstudantes = int(input('Quantos estudantes fizeram a prova?'))
snEstudantes = nEstudantes
estudantesInfo = {}
print(nEstudantes)

while snEstudantes > 0:
    snEstudantes=snEstudantes-1
    nome = input('Qual o nome do estudante?')
    nota = int(input('Qual a nota desse estudante?'))

    estudantesInfo[nome]=nota

somaNotas = 0
for estudante in estudantesInfo:
    somaNotas = somaNotas+estudantesInfo[estudante]

mediaNotas = somaNotas/nEstudantes  

print(f'Número de estudantes: {nEstudantes}')
for indice, estudante in enumerate(estudantesInfo, start=1):
    print(f'Estudante {indice}')
    print(f'Nome: {estudante}')
    print(f'Nota:{estudantesInfo[estudante]}')

print('-----------------')

print(f'Média da turma: {mediaNotas}')
print('Aprovados:')
for estudante in estudantesInfo:
    if estudantesInfo[estudante] >= 6:
        print(f'- {estudante}:{estudantesInfo[estudante]}')
print('Reprovados:')
for estudante in estudantesInfo:
    if estudantesInfo[estudante] < 6:
        print(f'- {estudante}:{estudantesInfo[estudante]}')



# # for estudante in nEstudantes:
# #     estudantesInfo([estudante]) = input('Qual o nome do estudante?')
# #     estudantesInfo(estudante) = input('E sua nota?')

# #     print (estudantesInfo)

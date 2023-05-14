# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0

# Itera cada pergunta na lista de perguntas
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()

    # Imprime as opções de resposta para as perguntas
    opcoes = pergunta['Opções']
    for indice, opcao in enumerate(opcoes):
        print(f'{indice})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    # Cria variáveis para verificar se a escolha foi correta
    escolha_int = None
    acertou = False
    qtd_opcoes = len(opcoes)

    # Verifica se a escolha é um número inteiro valido
    if escolha.isdigit():
        escolha_int = int(escolha)

    # Verifica se a resposta do usúario está dentro das opções
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    # Verifica se acertou, e incrementa no contador de acertos
    if acertou:
        qtd_acertos += 1
        print('Acertou')
        print()
    else:
        print('Errou  ')
        print()

# Mostra a quantidade de acertos de acordo com a quantidade de perguntas
print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas.')

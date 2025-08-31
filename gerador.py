# tentativa de criar um gerador de senha
# criado por Denisander Vivan 08/05/2022
import random
import numero, cabecalho


try:
    def valida(msg):
        while True:
            final = input(msg).strip().upper()[0]
            if final not in 'SN':
                print('\033[31mOpção inválida! Digite SIM ou NÃO!\033[m')
                continue
            else:
                return final


    parcial = []
    senha = []
    cont = 0
    caracteres = ('!', '@', '#', '$', '%', '&', '*', '(', ')', '?')
    números = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    alfamaiu = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'X', 'Y', 'Z', 'W')
    alfaminu = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'x', 'y', 'z', 'w')

    cabecalho.cabecalho('Gerador de senha!')

    while True:
        tamanho = numero.digiteint('\033[33mQual o tamanho da sua senha? ')
        if tamanho < 5:
            print('A senha não pode ter menos que cinco números!')
            continue
        else:
            break
    carac = valida('Você deseja caracteres especiais na sua senha? Sim ou não? ').strip().upper()[0]
    num = valida('Você deseja números na sua senha? Sim ou não? ').strip().upper()[0]
    almaiu = valida('Você deseja letras maiúsculas na sua senha? Sim ou não? ').strip().upper()[0]
    almin = valida('Você deseja letras minúsculas na sua senha? Sim ou não? \033[m').strip().upper()[0]

    if carac == 'N' and num == 'N' and almaiu == 'N' and almin == 'N':
        print('Nehuma opção escolhida! Fim do programa!')

    if carac == 'S':
        parcial.append(caracteres)
        cont += 1
    if num == 'S':
        parcial.append(números)
        cont += 1
    if almaiu == 'S':
        parcial.append(alfamaiu)
        cont += 1
    if almin == 'S':
        parcial.append(alfaminu)
        cont += 1

    if cont >= 1:
        for i in range(tamanho):
            var = random.randint(0, len(parcial) - 1)
            if len(parcial[var]) == 10:
                dez = random.randint(0, 9)
                senha.append(parcial[var][dez])
            if len(parcial[var]) == 26:
                vinte = random.randint(0, 25)
                senha.append(parcial[var][vinte])

    final = ''
    final = final.join(senha)
    print(f'\033[35mSua senha é: {final}\033[m')
except Exception as erro:
    print(f'Tivemos o erro: {erro}')

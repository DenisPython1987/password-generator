def digitefloat(n='Digite um número real: '):
    """
    Função que aceita somente números reais (float), aceita números com vírgula.
    :param n: informar o número.
    :return: Retorna um valor real.
    """
    while True:
        try:
            num = str(input(n)).strip().replace(',', '.')
            final = float(num)
            return final
        except ValueError:
            print('Digite sua altura em números separados por vírgula!')
            continue
        except Exception as erro:
            print(f'Infelizmente tivemos o erro: {erro.__class__}')


def peixe(peso=0):
    """
    Função que calcula se será aplicada uma multa em cima da quantidade de peixe pescado.
    :param peso: peso de peixes em kg.
    :return: retorna um valor real.
    """
    try:
        if peso > 40:
            parcial = peso - 40
            final = parcial * 4
            return final
        else:
            return 0
    except Exception as erro:
        print(f'Acho que deu o erro: {erro.__class__}')


def moeda(num=0):
    """
    Função para formatar valores reais em moeda.
    :param num: número real a ser formatado.
    :return: retorna uma string formatada em moeda.
    """
    inicial = f'{num:.2f}'
    parcial = str(inicial).replace('.', ',')
    return f'R${parcial}'


def digiteint(num='Digite um número: '):
    """
    Função que só aceita valores inteiros como entrada.
    :param num: número a ser verificado.
    :return: retorna um número inteiro.
    """
    while True:
        try:
            inicial = str(input(num)).strip()
            return int(inicial)
        except ValueError:
            print('Digite apenas números inteiros')
            continue


def raiz(num=1):
    """
    Função que retorna um valor aproximado de uma raiz quadrada, baseada numa fórmula de Newton.
    :param num: O número cuja raiz vai ser calculada.
    :return: Retorna quase uma raiz quadrada.
    """
    b = 2
    p = (b + (num / b)) / 2
    return p


def resto(n1=1, n2=1):
    """
    Função que mostra na tela o resto duma divisão.
    :param n1: dividendo.
    :param n2: divisor.
    :return: não retorna nada.
    """
    while n1 >= n2:
        num = n1 - n2
        print(f'{n1} - {n2} = {num}')
        n1 = num


def palindromo():
    """
    Função do professor Nilo que calcula se uma string é um palíndromo.
    :return: não retorna nada.
    """
    s = input('Digite um número sem espaços: ')
    i = 0
    f = len(s) - 1
    while f > i and s[i] == s[f]:
        f -= 1
        i += 1
    if s[i] == s[f]:
        print(f'{s} é palíndromo')
    else:
        print(f'{s} não é palíndromo')


def par(x):
    return x % 2 == 0


def par_ou_impar(x):
    if par(x):
        return 'par'
    else:
        return 'ímpar'


def maior(a, b):
    if a > b:
        return f'{a} é maior'
    else:
        return f'{b} é maior'


def multiplo(a, b):
    return a % b == 0


def quadrado(x):
    return x * 4


def areatriangulo(base, altura):
    area = (base * altura) / 2
    return area


def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat


def fibonacci(n):
    n1 = 0
    n2 = 1
    print(f'{n1} {n2} ', end='')
    for i in range(0, n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(f'{n3} ', end='')

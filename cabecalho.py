def linha(n=40):
    """
    Função que imprime uma linha na tela
    :param n: Informar a quantidade de caracteres
    :return: não retorna nada
    """
    print('\033[1;34m-\033[m' * n)


def cabecalho(msg):
    """
    Funão para imprimir um cabeçalho na tela com linhas personalizadas
    :param msg: Mensagem a ser impressa
    :return: não retorna nada
    """
    linha(len(msg) + 4)
    print(f'\033[1;34m  {msg}\033[m')
    linha(len(msg) + 4)

def calcular_expressao(expressao):
    """
    Calcula uma expressão aritmética fornecida como string.
    :param expressao: A expressão aritmética a ser calculada (ex: '2 + 3 * 4')
    :return: O resultado da expressão ou uma mensagem de erro.
    """
    try:
        resultado = eval(expressao)
        return f"O resultado é: {resultado}"
    except Exception as e:
        return f"Erro ao calcular a expressão: {e}"


entrada = input("Digite uma expressão aritmética para calcular (ex: 2 + 3 * 4): ")


print(calcular_expressao(entrada))
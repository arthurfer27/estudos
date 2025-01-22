"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40

def bake_time_remaining(num):  
    """Função calcula o tempo restante para cozimento da lasanha.

    :param num: int - quantidade de tempo para que e lasanha fique pronta.
    :return: int - tempo restante para que a lasanha fique pronta.
    """    
    return EXPECTED_BAKE_TIME - num    


bake_time_remaining(30)

def preparation_time_in_minutes(num):
    """Função calcula o tempo de cozimento de cada camada da lasanha.

    :param num: int - quantidade de camadas a serem montadas na lasanha.
    :return: int - tempo restante para que a lasanha fique pronta.

    Cada camada leva 2 minutos adicionais para ficarem prontas
    """  
    number_of_layers = num
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Função calcula o tempo restante para o cozimento da lasanha de acordo com a quantidade de camadas a serem montadas.

    :param number_of_layers: int - quantidade de camadas da lasanha.
    :param elapsed_bake_time: int - quantidade de tempo para que e lasanha fique pronta.
    :return: int - tempo restante para que a lasanha fique pronta.
    """  
    number_of_layers = number_of_layers * 2
    return number_of_layers + elapsed_bake_time
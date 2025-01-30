"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""
def get_rounds(number):
    rounds = [number, number+1, number+2]    
    return rounds

def concatenate_rounds(rounds_1, rounds_2):
    lists = rounds_1 + rounds_2
    return lists

def list_contains_round(rounds, number):
    if number in rounds:
        return True
    return False


def card_average(hand):
    average = sum(hand) / len(hand)
    return average

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    firts_and_last_average = (hand[0] + hand[-1]) / 2
    middle_term = len(hand) // 2
    if firts_and_last_average == card_average(hand) or hand[middle_term] == card_average(hand):
        return True
    return False


def average_even_is_average_odd(hand):
    lista_par = [hand[i] for i in range (0, len(hand), 2)]
    lista_impar = [hand[i] for i in range (1, len(hand), 2)]

    avg_par = sum(lista_par) / len(lista_par)
    avg_impar = sum(lista_impar) / len(lista_impar)

    if avg_par == avg_impar:
        return True
    return False


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
        return hand
    return hand
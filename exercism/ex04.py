#O objetivo deste exercício é resolver os diversos problemas propostos em uma viagem, envolvendo o câmbio de moedas, em formato de códigos
def exchange_money(budget, exchange_rate):
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    effective_rate = budget / (exchange_rate * (1 + spread/100))
    max_value = (effective_rate // denomination) * denomination
    return max_value
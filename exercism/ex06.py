def value_of_card(card):
    face_cards = {"J", "Q", "K"}
    if card == "A":
        return 1
    if card in face_cards:
        return 10
    if card.isdigit() and 2<= int(card) <= 10:
        return int(card)
    return None


def higher_card(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one > value_two:
        return card_one
    if value_two > value_one:
        return card_two
    return card_one, card_two


def value_of_ace(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if "A" in (card_one, card_two):
        return 1
    if (value_one + value_two + 11 > 21):
        return 1
    return 11

def is_blackjack(card_one, card_two):
    face_cards = {"J", "Q", "K", "10"}
    if card_one == "A" and card_two == "A":
        return False
    if (card_one == "A" and card_two in face_cards) or (card_one in face_cards and card_two == "A"):
        return True
    return False


def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    return False


def can_double_down(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    double_values = {9, 10, 11}
    if value_one + value_two in double_values:
        return True
    return False
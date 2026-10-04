def filter_by_currency(transactions, currency="USD"):
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction

def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction["description"]

def card_number_generator(start, stop):
    for number in range(start, stop + 1):
        card_str = f"{number:016d}"
        yield f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"


        
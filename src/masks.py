def get_mask_card_number(card_number: str) -> str:
    card_str = str(card_number)
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: str) -> str:
    account_str = str(account_number)
    return f"**{account_str[-4:]}"

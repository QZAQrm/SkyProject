from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    # 1. Разбиваем входящую строку на список слов
    parts = info.split()

    # 2. Достаем сам номер (это всегда последний элемент списка)
    number = parts[-1]

    # 3. Достаем название карты или счета (всё, кроме последнего элемента)
    # и сразу склеиваем обратно в строку через пробел
    name = " ".join(parts[:-1])

    # 4. Пишем условие проверки:
    if name == "Счет":
        # Здесь нужно вызвать get_mask_account() для number
        return f"{name} {get_mask_account(number)}"
        # И вернуть склеенную строку вида: "Счет **4305"
    else:
        # Здесь нужно вызвать get_mask_card_number() для number
        return f"{name} {get_mask_card_number(number)}"
        # И вернуть склеенную строку вида: "Visa Platinum 7000 79** **** 6361"


def get_date(date_str: str) -> str:
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")

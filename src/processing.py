def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Возвращает новый список словарей, содержащий только те словари,
    у которых ключ 'state' соответствует указанному значению.
    """
    # 1. Создаем пустой список для отфильтрованных данных (например, filtered_data = [])
    filtered_data = []

    # 2. Пишем цикл for, который пройдет по каждому элементу (словарю) в списке data
    for element in data:
        if element.get("state") == state:
            filtered_data.append(element)
    return filtered_data

    # 3. Внутри цикла проверяем: если значение по ключу 'state' в текущем словаре равно переменной state,
    #    то добавляем этот словарь в наш новый список с помощью .append()

    # 4. Возвращаем заполненный список через return


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """
    Возвращает новый список словарей, отсортированный по дате.
    """
    return sorted(data, key=lambda x: x.get('date', ''), reverse=reverse)

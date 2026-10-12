from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                if filename:
                    # Если имя файла передано, открываем его в режиме дозаписи ("a" - append)
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message + "\n")  # \n нужен для переноса на новую строку
                else:
                    # Если файла нет (filename остался None), просто выводим в терминал
                    print(log_message)

            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    # Если имя файла передано, открываем его в режиме дозаписи ("a" - append)
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message + "\n")  # \n нужен для переноса на новую строку
                else:
                    # Если файла нет (filename остался None), просто выводим в терминал
                    print(log_message)
                raise
                return result

        return wrapper

    return decorator

import pytest

from src.decorators import log


# Создаем функцию-манекен без указания файла (вывод в консоль)
@log()
def my_func(x, y):
    return x + y


def test_log_console_success(capsys):
    # 1. Вызываем нашу функцию, например my_func(1, 2)
    my_func(4, 3)

    # 2. Считываем всё, что напечаталось в консоль за время работы функции
    captured = capsys.readouterr()

    # 3. Сравниваем захваченный текст (captured.out) с ожидаемым ("my_func ok\n")
    assert captured.out == "my_func ok\n"


@log()
def my_func_div(x, y):
    return x / y


def test_log_console_error(capsys):
    with pytest.raises(ZeroDivisionError):
        my_func_div(10, 0)
    log_message = capsys.readouterr()
    assert log_message.out == "my_func_div error: ZeroDivisionError. Inputs: (10, 0), {}\n"


def test_log_file_success(tmp_path):
    # 1. Создаем путь к временному файлу внутри временной папки
    log_file = tmp_path / "test_log.txt"

    # 2. Создаем функцию-манекен прямо здесь и передаем ей путь (превратив его в обычную строку через str)
    @log(filename=str(log_file))
    def my_func_file(x, y):
        return x + y

    # 3. Вызови функцию my_func_file с любыми числами
    my_func_file(13, 3)

    # 4. Открываем файл и читаем его содержимое в переменную content
    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 5. Напиши assert, который сравнит переменную content с эталонной строкой успеха
    assert content == "my_func_file ok\n"


def test_log_file_error(tmp_path):
    # 1. Создаем временный файл
    log_file = tmp_path / "test_log.txt"

    # 2. Создаем функцию-манекен с ошибкой внутри теста
    @log(filename=str(log_file))
    def my_func_file_div(x, y):
        return x / y

    # 3. Открой блок with pytest.raises(ZeroDivisionError):
    # и вызови внутри него функцию my_func_file_div(10, 0)
    with pytest.raises(ZeroDivisionError):
        my_func_file_div(10, 0)

    # 4. Открой файл через with open(...) как в прошлом тесте,
    # прочитай текст в переменную content
    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 5. Напиши assert, сравнив content со строкой ошибки
    assert content == "my_func_file_div error: ZeroDivisionError. Inputs: (10, 0), {}\n"

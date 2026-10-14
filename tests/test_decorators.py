import pytest

from src.decorators import log


@log()
def my_func(x, y):
    return x + y


@log()
def my_func_div(x, y):
    return x / y


def test_log_console_success(capsys):
    result = my_func(4, 3)
    assert result == 7
    captured = capsys.readouterr()
    assert captured.out == "my_func ok\n"


def test_log_console_error(capsys):
    with pytest.raises(ZeroDivisionError):
        my_func_div(10, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_func_div error: ZeroDivisionError. Inputs: (10, 0), {}\n"


def test_log_file_success(tmp_path):
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def multiply(x, y):
        return x * y

    result = multiply(3, 5)
    assert result == 15
    assert log_file.read_text(encoding="utf-8") == "multiply ok\n"


def test_log_file_error(tmp_path):
    log_file = tmp_path / "mylog_error.txt"

    @log(filename=str(log_file))
    def fail_div(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        fail_div(5, 0)

    assert log_file.read_text(encoding="utf-8") == "fail_div error: ZeroDivisionError. Inputs: (5, 0), {}\n"

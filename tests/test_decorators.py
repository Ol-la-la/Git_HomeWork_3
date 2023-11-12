import os
from datetime import datetime
import pytest

from scr.decorators import my_function, log


def test_my_function():
    assert my_function(1, 2) == 3


@pytest.mark.parametrize(
    "arg_1, arg_2, expected_result",
    [
        (2, 5, " my_foo ok"),
        (1, "r", " my_foo error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, 'r') {}"),
    ],
)
def test_log(arg_1, arg_2, expected_result):
    filename = "test.txt"
    if os.path.exists(filename):
        os.remove(filename)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @log(filename)
    def my_foo(x: int, y: int) -> int:
        return x + y

    my_foo(arg_1, arg_2)
    with open(filename) as file:
        log_mes = file.read().strip()

    expected_log = now + expected_result

    assert log_mes == expected_log


@pytest.mark.parametrize("arg_1, arg_2, expected_result",
                         [(2, 5, " my_foo ok"),
                          (1, "r",
                           " my_foo error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, 'r') {}")])
def test_console_log(capsys, arg_1, arg_2, expected_result):
    @log()
    def my_foo(x: int, y: int) -> int:
        return x + y

    my_foo(arg_1, arg_2)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expected_log = now + expected_result
    log_mes = capsys.readouterr()
    assert log_mes.out.strip() == expected_log

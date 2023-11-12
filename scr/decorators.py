from datetime import datetime
from functools import wraps
from typing import Callable, Optional, Any


def log(filename: Optional[str] = None) -> Callable:
    def wrapped(function: Callable) -> Callable:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Текущая дата и время
            try:
                result = function(*args, **kwargs)
                status = f'{function.__name__} ok'
            except Exception as e:  # Обработка возникающих ошибок
                result = None
                status = f"{function.__name__} error: {e}. Inputs: {args} {kwargs}"

            # Если указано имя файла, то записываем лог в файл, если нет - то выводим в консоль
            if filename:
                with open(filename, 'a', encoding="utf-8") as f:
                    f.write(f"{now} {status}\n")
            else:
                print(f"{now} {status}\n")
            return result

        return inner

    return wrapped


@log("mylog.txt")
def my_function(x, y) -> object:
    return x + y


my_function(1, 2)

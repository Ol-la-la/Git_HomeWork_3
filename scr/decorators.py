from datetime import datetime
from functools import wraps


def log(filename="mylog.txt"):
    def wrapped(function):
        @wraps(function)
        def inner(*args, **kwargs):
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")   # Выводит текущую дату и время
            try:
                result = function(*args, **kwargs)
                status = f'{function.__name__} ok'
            except Exception as e:                                # Обработка возникающих ошибок
                result = None
                status = f"{function.__name__} error: {e}. Inputs: {args} {kwargs}"

            if filename:
                with open(filename, 'a', encoding="utf-8") as f:
                    f.write(f"{now} {status}\n")
            else:
                print(f"{now} {status}\n")
            return result
        return inner
    return wrapped


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)

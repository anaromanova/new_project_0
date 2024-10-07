from typing import Callable
from datetime import datetime


def log(filename: str = '') -> Callable:
    """Функция, которая автоматически логирует начало и конец
     выполнения функции, а также ее результаты или возникшие ошибки."""
    def decorator(func: Callable) -> Callable:
        """Функция-декоратор"""
        def wrapper(*args, **kwargs) -> None:
            """Функция для логирования, записей ошибок."""
            print(f"Начало работы: {datetime.now().replace(minute=0, second=0, microsecond=0)}")
            try:
                func(*args, **kwargs)
                message = "ok"
            except Exception as e:
                message = e
            finally:
                if '.' in filename:
                    with open(filename, "a") as file1:
                        # Writing data to a file
                        file1.write(f"{func.__name__}, {message} \n")
                else:
                    print(f"{func.__name__}, {message}")
            print(f"Конец работы: {datetime.now().replace(minute=0, second=0, microsecond=0)}")
        return wrapper
    return decorator

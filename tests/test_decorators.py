from typing import Union
from datetime import datetime

from src.decorators import log


def test_log(capsys) -> None:
    """Функция тестирует log from src.decorators"""
    @log(filename="")
    def func_for_decorators(x: Union[str, int], y: Union[str, int]) -> int:
        """Функция для проверки decorators"""
        return x + y

    func_for_decorators(1, 2)
    captured = capsys.readouterr()
    assert captured.out == f"Начало работы: {datetime.now().replace(minute=0, second=0, microsecond=0)}\nfunc_for_decorators, ok\nКонец работы: {datetime.now().replace(minute=0, second=0, microsecond=0)}\n"

    func_for_decorators("1", 2)
    captured = capsys.readouterr()
    assert captured.out == f"Начало работы: {datetime.now().replace(minute=0, second=0, microsecond=0)}\nfunc_for_decorators, can only concatenate str (not \"int\") to str\nКонец работы: {datetime.now().replace(minute=0, second=0, microsecond=0)}\n"

    @log(filename="file.txt")
    def func_for_decorators(x: Union[str, int], y: Union[str, int]) -> int:
        """Функция для проверки decorators"""
        return x + y

    result = func_for_decorators(1, 2)
    assert result is None

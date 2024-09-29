import pytest


@pytest.fixture
def numbers() -> int:
    return 7000792289606361


@pytest.fixture
def empty_lsts() -> list:
    return []


@pytest.fixture
def lsts() -> list:
    return [7000792289606361]

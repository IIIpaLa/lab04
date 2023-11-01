import pytest
from lib import count_common_elements

# Тесты для функции count_common_elements
def test_count_common_elements_empty_lists():
    # Тестируем с пустыми списками
    result = count_common_elements([], [])
    assert result == 0

def test_count_common_elements_no_common_elements():
    # Тестируем, когда списки не имеют общих элементов
    result = count_common_elements([1, 2, 3], [4, 5, 6])
    assert result == 0

def test_count_common_elements_some_common_elements():
    # Тестируем случай, когда есть общие элементы
    result = count_common_elements([1, 2, 3, 4], [3, 4, 5])
    assert result == 2

def test_count_common_elements_all_common_elements():
    # Тестируем случай, когда все списки имеют одинаковые элементы
    result = count_common_elements([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4])
    assert result == 4

def test_count_common_elements_duplicate_elements():
    # Тестируем случай, когда есть дубликаты в списках
    result = count_common_elements([1, 2, 2, 3], [2, 3, 3, 4])
    assert result == 2

# Запускаем тесты с помощью pytest
if __name__ == "pymain__":
    pytest.main()

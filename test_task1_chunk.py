import pytest
from task1_chunk import chunk


@pytest.mark.parametrize(
    "items, size, expected",
    [
        ([1, 2, 3, 4], 2, [[1, 2], [3, 4]]),          # ровно
        ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),   # с остатком
        ([1, 2, 3], 10, [[1, 2, 3]]),                  # size > длины
        ([], 3, []),                                   # пустой
        ([1, 2, 3], 1, [[1], [2], [3]]),               # size == 1
    ],
)
def test_chunk(items: list[int], size: int, expected: list[list[int]]) -> None:
    assert chunk(items, size) == expected


def test_chunk_invalid_size() -> None:
    with pytest.raises(ValueError):
        chunk([1, 2, 3], 0)

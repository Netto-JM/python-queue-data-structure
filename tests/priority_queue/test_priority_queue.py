import pytest

from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    # Arrange
    priority_queue = PriorityQueue()

    # Act
    # Test enqueue and len
    priority_queue.enqueue({"qtd_linhas": 1})
    priority_queue.enqueue({"qtd_linhas": 6})
    priority_queue.enqueue({"qtd_linhas": 3})
    assert len(priority_queue) == 3

    priority_queue.enqueue({"qtd_linhas": 5})
    priority_queue.enqueue({"qtd_linhas": 7})
    priority_queue.enqueue({"qtd_linhas": 2})
    assert len(priority_queue) == 6

    # Test search with valid indexes
    assert priority_queue.search(0) == {"qtd_linhas": 1}
    assert priority_queue.search(5) == {"qtd_linhas": 7}

    # Test search with invalid indexes
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(len(priority_queue))
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(-1)

    # Test high_priority list dequeue
    assert priority_queue.dequeue() == {"qtd_linhas": 1}
    assert priority_queue.dequeue() == {"qtd_linhas": 3}
    assert priority_queue.dequeue() == {"qtd_linhas": 2}
    assert len(priority_queue) == 3

    # Test regular_priority list dequeue
    assert priority_queue.dequeue() == {"qtd_linhas": 6}
    assert priority_queue.dequeue() == {"qtd_linhas": 5}
    assert priority_queue.dequeue() == {"qtd_linhas": 7}
    assert len(priority_queue) == 0

from ting_file_management.abstract_queue import AbstractQueue
from typing import Any


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.items = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.items)

    def enqueue(self, value: Any):
        """Aqui irá sua implementação"""
        self.items.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if len(self.items) == 0:
            raise IndexError("A fila está vazia")

        return self.items.pop(0)

    def search(self, index: int):
        """Aqui irá sua implementação"""
        if index < 0 or index >= len(self.items):
            raise IndexError("Índice Inválido ou Inexistente")

        return self.items[index]

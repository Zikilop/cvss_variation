"""
Скрипт — упорядоченный список операций, применяемых к исходной модели.
Результат применения скрипта -- один граф (модель).
"""

from dataclasses import dataclass, field

from .operation import Operation


@dataclass(slots=True)
class Script:
    """
    Один скрипт клонирования.

    Attributes:
        operations: список операций, последовательно применяемых к модели
    """
    operations: list[Operation] = field(default_factory=list)

    def add(self, operation: Operation) -> None:
        """Добавляем операцию в наш список"""
        self.operations.append(operation)

    @property
    def size(self) -> int:
        """Нужно, чтобы записывать в CVSS"""
        return len(self.operations)

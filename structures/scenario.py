"""
Сценарий — упорядоченный список скриптов.
Каждый скрипт порождает один файл-клон из исходной модели.
"""

from dataclasses import dataclass, field

from .script import Script


@dataclass(slots=True)
class Scenario:
    """
    Полный сценарий клонирования.

    Attributes:
        scripts: список скриптов
    """
    scripts: list[Script] = field(default_factory=list)

    def add(self, script: Script) -> None:
        """Добавляем скрипт в наш список"""
        self.scripts.append(script)

    @property
    def size(self) -> int:
        """Нужно, чтобы записывать в CVSS"""
        return len(self.scripts)

    @property
    def total_operations(self) -> int:
        """Нужно, чтобы записывать в CVSS"""
        return sum(s.size for s in self.scripts)
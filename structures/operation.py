"""
Одна операция клонирования: умножение параметра на множитель с фильтром по сосудам.
"""

from dataclasses import dataclass

#frozen=True, чтобы неизменяемые значения были (меньше вероятность косяка)
#slots=True, т к у нас фиксированное количество атрибутов, а это оптимизирует память
@dataclass(frozen=True, slots=True)
class Operation:
    """
    Единичная операция в скрипте клонирования.

    Attributes:
        parameter:  имя параметра (пока доступны SInit, SMin, SMax, PMin, PMax, Leng, Diff)
        multiplier: вещественный множитель
        type:       фильтр по Type (если None — не отслеживается)
        id:         фильтр по ID   (если None — не отслеживается)
        tag:        фильтр по Tag  (если None — не отслеживается)
    """
    parameter: str
    multiplier: float
    type: int | None = None
    id: int | None = None
    tag: int | None = None

    def format_filter_field(self, value: int | None) -> str:
        """Форматирует значение фильтра для текстового вывода в файл сценария для CVSS."""
        return "-" if value is None else str(value)
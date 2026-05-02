"""
Запись сценария в текстовый файл формата CVSS.

Формат (из мануала, п.14):
  - Строки с '#' -- комментарии
  - Количество скриптов
  - Для каждого скрипта: количество операций, затем строки операций
  - Строка операции: Parameter Mul Type ID Tag
    (Parameter -- регистрозависимый, Type/ID/Tag -- число или '-')
  - Поля разделены пробелами
"""

from pathlib import Path

from tqdm import tqdm

from structures.operation import Operation
from structures.scenario import Scenario


def format_operation(op: Operation) -> str:
    """Форматирует одну операцию в строку текстового формата CVSS."""
    # TODO: Возможно, надо сделать форматирование красивее, но пока так
    parts = [
        op.parameter,
        f"{op.multiplier:.10g}",
        op.format_filter_field(op.type),
        op.format_filter_field(op.id),
        op.format_filter_field(op.tag),
    ]
    return "  ".join(parts)


def write_scenario(
    scenario: Scenario,
    path: str | Path,
    show_progress: bool = True,
) -> None:
    """
    Записывает сценарий в текстовый файл формата CVSS.

    Args:
        scenario:      объект Scenario для записи
        path:          путь к выходному файлу
        show_progress: показывать ли прогресс-бар
    """
    path = Path(path)

    scripts = scenario.scripts
    iterator = tqdm(scripts, desc="Writing scripts", disable=not show_progress)

    lines: list[str] = []

    # Заголовок: количество скриптов
    lines.append("# Number of scripts")
    lines.append(str(scenario.size))

    for script in iterator:
        # TODO: надо сделать номер скрипта
        lines.append("# script №")
        # Количество операций в скрипте
        lines.append("# Number of operations in script")
        lines.append(str(script.size))

        # Строки операций
        lines.append("# Operations: Parameter  Mul  Type  ID  Tag")
        for op in script.operations:
            lines.append(format_operation(op))

    # Записываем одним вызовом — эффективнее для больших файлов
    path.write_text("\n".join(lines) + "\n", encoding="ansi")
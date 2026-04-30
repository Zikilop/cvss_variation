"""
Чтение YAML-конфигурации и создание генератора.

Этот модуль НЕ создаёт Scenario напрямую — он читает YAML,
определяет режим и делегирует генерацию соответствующему генератору.
"""

from pathlib import Path
from typing import Any

import yaml

#from config.constraints import VALID_MODES


def load_config(path: str | Path) -> dict[str, Any]:
    """
    Читает YAML-файл и возвращает словарь конфигурации.

    Выполняет базовую проверку наличия обязательных полей.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    if not isinstance(config, dict):
        raise ValueError(f"YAML должен содержать словарь на верхнем уровне")

    mode = config.get("mode")
    if mode is None:
        raise ValueError("Поле 'mode' обязательно в YAML-конфигурации")

#    if mode not in VALID_MODES:
#        raise ValueError(
#            f"Неизвестный режим '{mode}'. Допустимые: {sorted(VALID_MODES)}"
#        )

    if "parameters" not in config:
        raise ValueError("Поле 'parameters' обязательно в YAML-конфигурации")

    return config
"""
Абстрактный базовый класс генераторов сценариев.

Чтобы добавить новый режим генерации нужно:
  1. Создать файл в generators/
  2. Наследоваться от BaseGenerator
  3. Реализовать метод generate(), который возвращает сценарий
  4. Зарегистровать в GENERATOR_REGISTRY
"""

from abc import ABC, abstractmethod
from typing import Any


from structures.scenario import Scenario


class BaseGenerator(ABC):
    """
    Базовый класс для всех генераторов.

    Args:
        config: словарь, полученный из YAML-файла
    """

    def __init__(self, config: dict[str, Any]) -> None:
        self.config = config

    @abstractmethod
    def generate(self) -> Scenario:
        """Генерирует сценарий по конфигурации. Возвращает объект Scenario."""
        ...


# Реестр генераторов: mode_name -> class
# Заполняется после определения всех генераторов (в __init__.py или здесь через lazy import)
GENERATOR_REGISTRY: dict[str, type[BaseGenerator]] = {}


def register_generator(mode: str):
    """Декоратор для регистрации генератора в реестре."""
    def decorator(cls: type[BaseGenerator]):
        GENERATOR_REGISTRY[mode] = cls
        return cls
    return decorator


def get_generator(mode: str, config: dict[str, Any]) -> BaseGenerator:
    """Фабрика: возвращает генератор по имени режима."""
    if mode not in GENERATOR_REGISTRY:
        available = ", ".join(sorted(GENERATOR_REGISTRY.keys()))
        raise ValueError(f"Неизвестный режим '{mode}'. Доступные: {available}")
    return GENERATOR_REGISTRY[mode](config)
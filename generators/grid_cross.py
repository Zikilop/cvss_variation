"""
Генератор: декартово произведение (grid_cross).

Каждая комбинация множителей из всех параметров → один скрипт.
Скрипт содержит по одной операции на каждый параметр.

Пример: 2 параметра с [0.9, 1.0, 1.1] и [0.95, 1.05]
         → 3 × 2 = 6 скриптов, каждый по 2 операции.
"""

import itertools
from typing import Any

from structures.operation import Operation
from structures.script import Script
from structures.scenario import Scenario
from .base import BaseGenerator, register_generator


@register_generator("grid_cross")
class GridCrossGenerator(BaseGenerator):

    def generate(self) -> Scenario:
        param_blocks = self.config["parameters"]

        # Для каждого блока параметров строим список операций
        axes: list[list[Operation]] = []

        for block in param_blocks:
            ops = _build_operations_from_block(block)
            axes.append(ops)

        # Декартово произведение всех осей
        scenario = Scenario()
        for combination in itertools.product(*axes):
            script = Script()
            for op in combination:
                script.add(op)
            scenario.add(script)

        return scenario


def _build_operations_from_block(block: dict[str, Any]) -> list[Operation]:
    """
    Из одного YAML-блока параметра строит список Operation
    (по одной на каждый multiplier).
    """
    name = block["name"]
    multipliers = block["multipliers"]
    filters = block.get("filters", {})

    type = filters.get("type")
    id = filters.get("id")
    tag = filters.get("tag")

    return [
        Operation(
            parameter=name,
            multiplier=m,
            type=type,
            id=id,
            tag=tag,
        )
        for m in multipliers
    ]

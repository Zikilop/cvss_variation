"""
CLI точка входа.

Использование:
    python main.py -i config.yaml -o scenario.txt
"""

import time
import click

from file_io import load_config, write_scenario
from generators.base import get_generator

# Импорт для срабатывания декораторов @register_generator
import generators.grid_cross

@click.command()
@click.option('--input', '-i', required=True, help='YAML конфигурация')
@click.option('--output', '-o', default='scenario.txt', help='Выходной .txt файл')
@click.option('--verbose', is_flag=True, default=True, help="Verbose output")
def main(input, output, verbose):
    """Простая CLI программа"""
    config = load_config(input)
    mode = config["mode"]

    if verbose:
        print(f"Режим:          {mode}")
        print(f"Входной файл:   {input}")
        print(f"Выходной файл:  {output}")
        print()
    
    generator = get_generator(mode, config)

    t0 = time.perf_counter()
    scenario = generator.generate()
    t_gen = time.perf_counter() - t0
    
    if verbose:
        print(
            f"Сгенерировано:  {scenario.size} скриптов, "
            f"{scenario.total_operations} операций ({t_gen:.2f}s)"
        )

    t0 = time.perf_counter()
    write_scenario(scenario, output, show_progress=True)
    t_write = time.perf_counter() - t0
    
    if verbose:
        print(f"\nЗаписано за {t_write:.2f}s -> {output}")


if __name__ == '__main__':
    main()
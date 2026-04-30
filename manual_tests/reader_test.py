import click
import sys
from pathlib import Path
# Костыльно. Может, потом стоит убрать или порефакторить проект, но пока так
# Это для того, чтобы могли обращаться к ../file_io/yaml_reader.py
sys.path.append(str(Path(__file__).resolve().parents[1]))

from file_io.yaml_reader import load_config

@click.command()
@click.option('--path', '-p', default='../examples/test.yaml', help='Путь к YAML файлу')
def main(path):
    print(load_config(path))

if __name__ == '__main__':
    main()
import click
from mansai.inner import inner_hello


@click.command(help="SAI 구성원과 관련된 작업을 하는 도구입니다.")
@click.option(
    "--name",
    required=True,
)
def main(name):
    print(f'hello {name}')

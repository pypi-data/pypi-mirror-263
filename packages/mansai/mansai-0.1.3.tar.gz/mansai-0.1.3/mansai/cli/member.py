import click
from mansai.hello import say_hello_to
from mansai.inner.deep_hello import say_deep_hello_to
from korea.greeting import say_hello_to as kr_say_hello_to
from china.greeting import say_hello_to as cn_say_hello_to


@click.command(help='SAI 구성원과 관련된 작업을 하는 도구입니다.')
@click.option(
    '--name',
    required=True,
)
def main(name):
    say_hello_to(name)
    say_deep_hello_to(name)
    kr_say_hello_to(name)
    cn_say_hello_to(name)


if __name__ == '__main__':
    main(None)

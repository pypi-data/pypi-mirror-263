import click
from helloengland.greeting import say_hello_to
from helloengland.subpackage.humble_greeting import say_humble_hello_to
from hellokorea.greeting import say_hello_to as kr_say_hello_to
from hellochina.greeting import say_hello_to as cn_say_hello_to


@click.command(help='친구에게 인사하세요.')
@click.option(
    '--name',
    required=True,
)
def main(name):
    say_hello_to(name)
    say_humble_hello_to(name)
    kr_say_hello_to(name)
    cn_say_hello_to(name)


if __name__ == '__main__':
    main()

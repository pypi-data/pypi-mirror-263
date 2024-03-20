import click

from cron_parser.cron_expression import CronExpression

@click.command()
@click.argument('expression')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
def cli(expression):
    parser = CronExpression(expression).parse()
    output = parser.format_as_table()
    click.echo(output)


if __name__ == '__main__':
    cli()

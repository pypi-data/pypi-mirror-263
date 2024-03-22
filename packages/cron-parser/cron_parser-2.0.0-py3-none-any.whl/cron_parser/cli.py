import click

from cron_parser.parse_cron_expression import ParseCronExpression

@click.command()
@click.argument('expression', default= "")
def cli(expression):
    try:
        output = ParseCronExpression(expression).evaluate()
        click.echo("cron-parser to parse the cron expression\n")
        click.echo(output)
    except Exception as e:
        print("Exception occured : ",e)

if __name__ == '__main__':
    cli()

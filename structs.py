import click
def error(message):
    click.secho(message, bg='red')


def help():
    print()
    click.secho("WELCOME TO HELP 👏", fg='yellow')
    print()
    click.secho("If your getting a 'Database' error, visit SQLite's Website:")
    click.secho("https://www.sqlite.org/docs.html", fg="blue")
    print()
    click.secho("For a full start guide visit our Github:")
    click.secho("https://github.com/definiteconfusion/SQL-Command-Line-Utility/blob/main/StartGuide.md", fg='blue')
    print()
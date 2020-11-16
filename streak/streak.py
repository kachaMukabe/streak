import calendar
import datetime
import click
from colorama import init
from termcolor import colored

from streak.db import get_all, get_year, initialize_db, update_month


init()

# db.insert({str(datetime.datetime.now().year): {str(datetime.datetime.now().month): [True, False, True]}})


@click.group(invoke_without_command=True)
@click.option('-c', '--check', is_flag=True)
def cli(check):
    qal = calendar.Calendar(firstweekday=6)
    calendar.setfirstweekday(calendar.SUNDAY)
    initialize_db()
    y, m, today =  datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day
    year = get_year(y)
    click.echo(calendar.weekheader(2))
    for day in qal.monthdayscalendar(y, m):
        def format_day(d, year):
            d = str(d)
            done = False
            try:
                done = year[str(m)][d]
            except KeyError:
                if not d == "0":
                    year[str(m)][d] = False
            if str(today) == d and check:
                year[str(m)][d] = True
                done = True
            if d == "0":
                d = '  '
            elif len(d) == 1:
                d = colored(f' {d}', 'red', attrs=['blink', 'bold']) if done else f' {d}'
            return colored(d, 'red') if done else d
        click.echo(" ".join([format_day(x, year) for x in day]))
    update_month(y,m, year[str(m)])

if __name__ == "__main__":
    cli()
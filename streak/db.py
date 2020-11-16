from tinydb import TinyDB, Query
from tinydb.operations import set
import datetime
import os

path = os.path.expanduser('~/streak')
if not os.path.exists(path):
    os.mkdir(path)
    
db = TinyDB(f'{path}/db.json')

Entry = Query()

def initialize_db():
    year = datetime.datetime.now().year
    c_year, exists = query_year(year)
    if not exists:
        insert_year(year)

def get_all():
    return db.all()

def query_year(year):
    response = db.search(Entry.year == year)

    return response, len(response) > 0


def insert_year(year):
    db.insert({
        'year': year,
        '1': {},
        '2': {},
        '3': {},
        '4': {},
        '5': {},
        '6': {},
        '7': {},
        '8': {},
        '9': {},
        '10': {},
        '11': {},
        '12': {}
    })

def get_year(year):
    response = db.search(Entry.year == year)
    year = response[0] if len(response) > 0 else {}
    return year


def update_month(year, month, data):
    db.update(set(f'{month}', data), Entry.year == year)


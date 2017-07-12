#!/usr/bin/python3
import sys
from tinydb import TinyDB, Query
from datetime import datetime

def klara_list(sortfield = ''):
    table = db.table('task')
    tasks = table.all()
    klara_print_tasks(tasks)

def klara_print_tasks(tasks):
    tpl = '{:>4} {:<30} {:<10} {:>6} {:>10} {:>10}'
    width = 4 + 1 + 30 + 1 + 10 + 1 + 6 + 1 + 10 + 1 + 10
    print(tpl.format('ID', 'Description', 'Topic', 'Points', 'Created', 'Finished'))
    print(width * '-')
    points_total = 0
    for task in tasks:
        created = '{:%Y-%m-%d}'.format(datetime.fromtimestamp(task['created']))
        print(tpl.format(task.eid, task['description'], task['topic'], task['points'], created, task.get('finished', '')))
        points_total += int(task['points'])
    print(width * '-')
    print('Total points: ' + str(points_total))

def klara_create():
    table = db.table('task')
    keys = ['description', 'topic', 'points']
    task = {}
    print('Creating task.')
    for key in keys:
        task[key] = input(key + ': ')
    task['created'] = datetime.now().timestamp()
    table.insert(task)

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        sys.stderr.write('Missing command arg.\n')
        sys.exit(1)
    command = sys.argv[1]
    args = sys.argv[2:]
    db = TinyDB('db.json')
    if (command == 'list'):
        klara_list(*args)
    elif (command == 'create'):
        klara_create(*args)
    else:
        print('Unknown command "' + command + '"')

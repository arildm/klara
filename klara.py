#!/usr/bin/python3
import sys
from tinydb import TinyDB, Query

def klara_list(sortfield = ''):
    table = db.table('task')
    tasks = table.all()
    klara_print_tasks(tasks)

def klara_print_tasks(tasks):
    tpl = '{:>4} {:<40} {:<10} {:>10} {:>10} {:>10}'
    width = 4 + 1 + 40 + 1 + 10 + 1 + 10 + 1 + 10 + 1 + 10
    print(tpl.format('ID', 'Description', 'Topic', 'Points', 'Created', 'Finished'))
    print(width * '-')
    points_total = 0
    for task in tasks:
        print(tpl.format(task.eid, task['description'], task['topic'], task['points'], task.get('created', ''), task.get('finished', '')))
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
    task['created'] = 0
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

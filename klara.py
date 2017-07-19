#!/usr/bin/python3
import sys
from tinydb import TinyDB, Query
from datetime import datetime

class Task(dict):

    TIME_FORMAT = '{:%Y-%m-%d}'

    def __init__(self, d={}):
        dict.__init__(self, d)
        # Re-set special values.
        if 'created' in d:
            self.created = d['created']
        if 'finished' in d:
            self.finished = d['finished']
        try:
            self.eid = d.eid
        except AttributeError: {}

    def __setattr__(self, attr, value):
        if attr in ['created', 'finished']:
            if isinstance(value, datetime):
                value = value.timestamp()
        if attr in ['points']:
            try:
                value = int(value)
            except ValueError:
                value = 0
        self[attr] = value

    def __getattr__(self, attr):
        if attr in self:
            if attr in ['created', 'finished']:
                time = datetime.fromtimestamp(self[attr])
                return self.TIME_FORMAT.format(time)
            return self[attr]
        return ''


class Klara():

    def __init__(self, dbfile='klara.json'):
        self.db = TinyDB(dbfile)
        self.table = self.db.table('task')

    def list(self, sortfield='eid'):
        tasks = self.table.all()
        tasks = [Task(task) for task in tasks]
        if sortfield != None:
            tasks.sort(key=lambda t: getattr(t, sortfield))
        Klara.print_tasks(tasks)

    def print_tasks(tasks):
        print_table([
            ('eid', 'ID', 4, '>'),
            ('description', 'Description', 30, '<'),
            ('topic', 'Topic', 10, '<'),
            ('points', 'Points', 6, '>'),
            ('created', 'Created', 10, '>'),
            ('finished', 'Finished', 10, '>')
        ], tasks)
        points_total = sum(int(task.points) for task in tasks)
        print('Total points: {}'.format(points_total))

    def create(self):
        print('Creating task.')
        task = Klara.edit_input()
        task.created = datetime.now()
        self.table.insert(task)

    def edit(self, id, key=None, value=None):
        id = int(id)
        task = self.get(id)
        if value == None:
            print('Editing task {}.'.format(id))
            if key == None:
                task = Klara.edit_input(task)
            else:
                task = Klara.edit_input(task, keys=[key])
        else:
            print('Setting {} to {}.'.format(key, value))
            setattr(task, key, value)
        self.table.update(task, eids=[id])

    def get(self, id):
        el = self.table.get(eid=id)
        if (el == None):
            raise Error('No task with id {}'.format(id))
        return Task(el)

    def edit_input(task=Task(), keys=['description', 'topic', 'points']):
        for key in keys:
            # Suggest existing value.
            suggestion = ' ["' + str(getattr(task, key)) + '"]' if key in task else ''
            raw = input(key + suggestion + ': ')
            # Leave existing value if input is empty.
            if (raw or not suggestion):
                setattr(task, key, raw)
        return task

    def finish(self, id):
        id = int(id)
        task = self.get(id)
        if task.finished:
            sys.stderr.write('Task {} already finished at {}!\n'.format(id, task.finished))
            return
        task.finished = datetime.now()
        self.table.update(task, eids=[id])
        print('Task {} finished at {}.'.format(id, task.finished))

    def search(self, term):
        def match(description):
            return term.lower() in description.lower()
        result = self.table.search(Query().description.test(match))
        tasks = [Task(task) for task in result]
        Klara.print_tasks(tasks)

    def topic(self, topic):
        result = self.table.search(Query().topic == topic)
        tasks = [Task(task) for task in result]
        Klara.print_tasks(tasks)


def print_table(fields, data):
    keys = [f[0] for f in fields]
    headers = [f[1] for f in fields]
    width = sum(field[2] + 1 for field in fields) - 1
    tpl = ''.join('{:' + f[3] + str(f[2]) + '} ' for f in fields)[:-1]
    print(tpl.format(*headers))
    print(width * '-')
    for row in data:
        print(tpl.format(*[str(getattr(row, k))[:w] for (k, l, w, a) in fields]))
    print(width * '-')

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        sys.stderr.write('Missing command arg!\n')
        sys.exit(1)
    command = sys.argv[1]
    args = sys.argv[2:]
    klara = Klara()
    getattr(klara, command)(*args)

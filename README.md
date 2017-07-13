# Klara

Minimalistic Python CLI task manager.

## Usage

### Create

    $ python3 klara.py create
    description: Create README
    topic: doc
    points: 1

### List

    $ python3 klara.py list
      ID Description                    Topic      Points    Created   Finished
    ---------------------------------------------------------------------------
       1 Create README                  doc             1 2017-07-12           
    ---------------------------------------------------------------------------
    Total points: 1

### Edit

edit \<id> [\<field> [\<value>]]

    $ python3 klara.py edit 1
    Editing task 1.
    description ["Create README"]: 
    topic ["doc"]: meta
    points ["1"]: 2

    $ python3 klara.py edit 1 topic
    Editing task 1.
    topic ["meta"]: doc

    $ python3 klara.py edit 1 points 2
    Setting points to 2.


### Finish

finish \<id>

    $ python3 klara.py finish 1
    Task 2 finished at 2017-07-12.


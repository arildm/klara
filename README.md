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

    $ python3 klara.py edit 1
    Editing task 1.
    description ["Create README"]: 
    topic ["doc"]: meta
    points ["1"]: 2

### Finish

    $ python3 klara.py finish 1
    Task 2 finished at 2017-07-12.


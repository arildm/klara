# Klara

Minimalistic Python CLI task manager.

## Usage

### Create

    $ python3 klara.py create
    description: Create README
    topic: doc
    points: 2

### List

list [\<sortfield>]

    $ python3 klara.py list 
      ID Description                    Topic      Points    Created   Finished
    ---------------------------------------------------------------------------
       1 Create README                  doc             2 2017-07-13           
       2 Git setup                      admin           1 2017-07-13           
    ---------------------------------------------------------------------------
    Total points: 3

    $ python3 klara.py list points
      ID Description                    Topic      Points    Created   Finished
    ---------------------------------------------------------------------------
       2 Git setup                      admin           1 2017-07-13           
       1 Create README                  doc             2 2017-07-13           
    ---------------------------------------------------------------------------
    Total points: 3

### Edit

edit \<id> [\<field> [\<value>]]

    $ python3 klara.py edit 1
    Editing task 1.
    description ["Create README"]: 
    topic ["doc"]: meta
    points ["2"]: 3

    $ python3 klara.py edit 1 points
    Editing task 1.
    points ["2"]: 3

    $ python3 klara.py edit 1 points 3
    Setting points to 3.

### Finish

finish \<id>

    $ python3 klara.py finish 1
    Task 2 finished at 2017-07-12.


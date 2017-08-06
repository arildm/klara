# Klara

Minimalistic Python CLI task manager.

## Requirements

* [TinyDB](http://tinydb.readthedocs.io/en/latest/)

## Installation

Create a simple invocation script in a directory in your `$PATH`:

    python3 /path/to/klara/klara.py $@

Save the script as `klara` and set it to executable:

    chmod +x ~/bin/klara

## Usage

### Create

    $ klara create
    description: Create README
    topic: doc
    points: 2

### List

list [\<sortfield>]

    $ klara list
      ID Description                    Topic      Points    Created   Finished
    ---------------------------------------------------------------------------
       1 Create README                  doc             2 2017-07-13           
       2 Git setup                      admin           1 2017-07-13           
    ---------------------------------------------------------------------------
    Total points: 3

    $ klara list points
      ID Description                    Topic      Points    Created   Finished
    ---------------------------------------------------------------------------
       2 Git setup                      admin           1 2017-07-13           
       1 Create README                  doc             2 2017-07-13           
    ---------------------------------------------------------------------------
    Total points: 3

### Edit

edit \<id> [\<field> [\<value>]]

    $ klara edit 1
    Editing task 1.
    description ["Create README"]: 
    topic ["doc"]: meta
    points ["2"]: 3

    $ klara edit 1 points
    Editing task 1.
    points ["2"]: 3

    $ klara edit 1 points 3
    Setting points to 3.

### Finish

finish \<id>

    $ klara finish 1
    Task 2 finished at 2017-07-12.

### Search

search \<term>

    $ klara search read
      ID Description                    Topic      Points    Created   Finished
    ---------------------------------------------------------------------------
       1 Create README                  doc             2 2017-07-13           
    ---------------------------------------------------------------------------
    Total points: 2

### Topic

topic \<topic>

    $ klara topic doc
      ID Description                    Topic      Points    Created   Finished
    ---------------------------------------------------------------------------
       1 Create README                  doc             2 2017-07-13           
    ---------------------------------------------------------------------------
    Total points: 2

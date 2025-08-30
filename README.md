# p.notes
## . description
simple encrypted notes console app . made for fun in one day\
*try to guess the pass for uploaded db*
## . features
+ create encrypted notes
+ view notes for today / yesterday / tomorrow
+ displayed notes are automatically sorted in time order
## . dependencies
+ python
+ gnupg installed
+ venv with python-gnupg library: pip install python-gnupg
## . shit
- no function to set gnupg's folder using ui for now (defaults to ~/.gnupg/)
## . coming up
+ weekly notes
+ encrypting with gpg key as alternative to passphrase ?

# usage
### . init storage
```python main.py init```\
*you'll be asked if you want to make a copy of the current db, if one exists, and to make a passphrase you'll use then to login*
### . create a note
```python main.py add [--time TIME {HH:MM}] [--name NAME] [--content CONTENT]```\
*you are not forced to specify note's info in the command. if you don't, you'll be asked for that later*
### . view notes
```python main.py view [--tomorrow] [--yesterday]```\
*shows today's notes by default*

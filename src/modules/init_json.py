import shutil
from constants.consts import JSONFILENAME, GPGEXT

def init_json(no_copy: bool = False, back_up: bool = False):
    try:
        with open(JSONFILENAME+GPGEXT, 'r') as f:
            if back_up: 
                shutil.copy(JSONFILENAME+GPGEXT, JSONFILENAME+GPGEXT+'.copy')
            elif not no_copy:
                print(f"WARNING : {JSONFILENAME+GPGEXT} exists . it will be rewritten")
                print("INFO : use --no-copy / --back-up to make it faster next time")
                create_copy = input(". create copy? : y/N: ")
                if create_copy.lower() == 'y':
                    shutil.copy(JSONFILENAME+GPGEXT, JSONFILENAME+GPGEXT+'.copy')

    except FileNotFoundError:
        pass

    create_file()

import json
import utils.gpg as gpg
def create_file():
    with open(JSONFILENAME, 'w') as f:
        json.dump({}, f)

    passphrase = input("INPUT : passphrase: ")
    gpg.encrypt(filepath=JSONFILENAME, passphrase=passphrase)





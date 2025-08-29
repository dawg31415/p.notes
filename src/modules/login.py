import utils.json_funcs as json_funcs
from utils.errors import PassphraseError
from constants.consts import JSONFILENAME, GPGEXT

def login():
    try:
        open('../db/'+JSONFILENAME+GPGEXT).close()
    except:
        print("ERR : login.db : no database found. use 'init' first")
        print()
        exit(0)
    try: 
        passphrase = input("LOGIN : INPUT : passphrase: ")
        json_funcs.load(passphrase) 
    except PassphraseError:
        print("ERR : decryption : passphrase is incorrect")
        print("TIP : decryption : press ctrl+c to exit")
        login()
    except KeyboardInterrupt:
        print("\nINFO : exiting\n")
        exit(0)

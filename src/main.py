from modules.args import parse_args
from modules.login import login
from modules.init_json import init_json
from modules.display import display
from modules.add import add

def main():
    action, *args = parse_args()
    if action   != 'init': login()
    if action   == 'init':
        init_json(*args)
    elif action == 'view':
        display(*args)
    elif action == 'add':
        add(*args)
    print() # i just like it this way

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nEXIT : execution stopped\n")

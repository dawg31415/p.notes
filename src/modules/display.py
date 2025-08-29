from datetime import datetime, timedelta
from note.note import Note
from utils.sort_notes import sort_notes
import utils.json_funcs as json_funcs

def display(tomorrow: bool=False, yesterday: bool=False) -> None:
    e = datetime.now()
    if tomorrow: e += timedelta(days=1)
    if yesterday: e -= timedelta(days=1)

    e_beauty = e.strftime("%Y.%m.%d")
    print(f"\nnotes for {e_beauty}")
    notes: [Note] = json_funcs.get(e)
    for note in sort_notes(notes):
        note.display()
    if len(notes) == 0:
        print('    no notes')

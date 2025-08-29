import json
from datetime import datetime, time
from note.note import Note
from constants.consts import JSONFILENAME, GPGEXT
from utils.errors import PassphraseError
import utils.gpg as gpg
import utils.etime as etime

global data, cached_pass
data = None

def load(passphrase: str) -> None:
    global data, cached_pass
    decrypted_ok, decrypted_text = gpg.decrypt(JSONFILENAME+GPGEXT, passphrase)
    if not decrypted_ok:
        raise PassphraseError()

    cached_pass = passphrase
    data = json.loads(decrypted_text)

    # parse notes-dicts to notes-Notes
    for day_notes in data.values():
        for note_time, note_dict in day_notes.items():
            day_notes[note_time] = Note.from_json(note_dict)

def get(date: datetime) -> [Note]:
    day_str = etime.date_to_str(date)
    global data
    if day_str not in data.keys(): return [] 
    notes_data = data[day_str]
    notes = list(notes_data.values())
    return notes

def _set(note_time: time, name: str, content: str) -> None:
    _datetime = datetime.now()
    day_str = etime.date_to_str(_datetime)

    global data
    if day_str not in data.keys(): data[day_str] = {}
    data[day_str][note_time] = Note(
            time = note_time,
            name = name,
            content = content
            )
    write()

def write():
    global data, cached_pass
    _data = {}
    # parse notes-Notes to notes-dicts to store it
    for day_date, day_notes in data.items():
        _data[day_date] = {}
        for note_time, note in day_notes.items():
            # messy bc day_data is str and note_time is time but i aint dealin' w it
            if type(note_time) is not str: note_time = etime.time_to_str(note_time)
            _data[day_date][note_time] = note.to_dict()

    with open(JSONFILENAME, 'w') as f:
        json.dump(_data, f)

    gpg.encrypt(filepath=JSONFILENAME, passphrase=cached_pass)






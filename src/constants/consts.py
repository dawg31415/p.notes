JSONFILENAME = '../db/notes.json'
GPGEXT = '.gpg'

from typing import Union
NOTE_NAME_TYPE = Union[str, int, float, bool] 
NOTE_CONTENT_TYPE = Union[str, int, float, bool] 
NOTE_TIME_TYPE = str

DATE_FORMAT = "%Y.%m.%d"
TIME_FORMAT = "%H.%M"
# day_str = _datetime.strftime("%Y.%m.%d")
# note_time = datetime.strptime(note_time, "%H.%M.%S")

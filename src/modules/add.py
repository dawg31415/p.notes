from constants.consts import NOTE_NAME_TYPE, NOTE_CONTENT_TYPE, NOTE_TIME_TYPE
from utils.json_funcs import _set
from datetime import datetime
import utils.etime as etime

def add(time:str=None, name:str=None, content:str=None) -> None:
    if not name: name = ask_for("name", "hashable", NOTE_NAME_TYPE)
    if not content: content = ask_for("content", "hashable", NOTE_CONTENT_TYPE)
    if not time: time = ask_for("time", "{HH.MM}", NOTE_TIME_TYPE)

    validate, issue = validate_args(time, name, content)
    if not validate:
        print(f"ERR : {issue} : wrong format")
        add() # TODO give in params which are good

    time = etime.str_to_time(time)
    _set(note_time=time, name=name, content=content)

def ask_for(obj_name: str, desc: str, force_type: type = None):
    text = obj_name if not desc else obj_name + ':' + str(desc)
    obj = input(f"INPUT : {text}: ")
    while (not obj) and (force_type and type(obj) is force_type):
        print("ERR : input.type is wrong")
        obj = input(f"INPUT : {text}: ")
    return obj

def validate_args(time: str, name: str, content: str) -> tuple:
    try:
        note_time = etime.str_to_time(time)
    except ValueError:
        return (False, "time")
    return (True, "")

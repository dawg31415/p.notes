from note.note import Note
from datetime import time

def sort_notes(notes):
    clone = notes.copy()
    for i in range(len(notes)):
        for j, note in enumerate(clone):
            if notes[i].time > note.time:
                notes[notes.index(note)] = notes[i] 
                notes[i] = note
        clone.remove(notes[i])
    return notes

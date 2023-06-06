from _datetime import datetime
from Model.Note import Note


class NoteService:
    @staticmethod
    def create_new_note(header: str, body: str) -> Note:
        note = Note()
        note.set_changing_time(datetime.now().strftime('%d-%m-%y %H:%M:%S'))
        note.set_header(header)
        note.set_body(body)
        return note

    @staticmethod
    def clone_note_from_external_library(note_id: int, date_time, header: str, body: str) -> Note:
        note = Note()
        note.set_note_id(note_id)
        note.set_changing_time(date_time)
        note.set_header(header)
        note.set_body(body)
        return note

    @staticmethod
    def change_note(note: Note, header: str, body: str):
        note.set_header(header)
        note.set_body(body)
        note.set_changing_time(datetime.now().strftime('%d-%m-%y %H:%M:%S'))

    @staticmethod
    def delete_note(note: Note):
        note.__del__()


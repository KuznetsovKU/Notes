from Model.NoteList import NoteList
from Model.Note import Note


class NoteListService:
    nlt = NoteList()

    @staticmethod
    def get_note_list(note_list: NoteList = nlt):
        return note_list.get_note_list()

    @staticmethod
    def add_note_to_list(new_note: Note, note_list: NoteList = nlt):
        note_list.add_note_to_list(new_note)

    @staticmethod
    def delete_note_from_list(note_to_delete_id: int, note_list: NoteList = nlt):
        note_list.delete_note_from_list(note_to_delete_id)

    @staticmethod
    def clear_note_list(note_list: NoteList = nlt):
        note_list.clear_note_list()
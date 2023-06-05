from .Note import Note


class NoteList:
    def __init__(self):
        self.__note_list = []

    def add_note_to_list(self, new_note: Note):
        self.__note_list.append(new_note)

    def delete_note_from_list(self, note_to_delete_id: int):
        for note in self.__note_list:
            if note.get_note_id() == note_to_delete_id:
                self.__note_list.remove(note)
                break

    def clear_note_list(self):
        self.__note_list.clear()

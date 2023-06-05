from Note import Note


class NoteList:
    __slots__ = 'note_list'
    
    def __init__(self):
        self.note_list = []

    def add_note_to_list(self, new_note: Note):
        self.note_list.append(new_note)

    def delete_note(self, note_to_delete: int):
        for note in self.note_list:
            if note.get_note_id() == note_to_delete:
                self.note_list.remove(note)
                break

    def clear_note_list(self):
        self.note_list.clear()

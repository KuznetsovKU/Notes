from _datetime import datetime


class Note:
    @staticmethod
    def set_new_note_id(note_id: int) -> int:
        Note.note_id += 1
        return note_id

    __slots__ = ('note_id', 'creation_time', 'header', 'body')

    def __init__(self):
        self.note_id = Note.set_new_note_id(Note.note_id)
        self.creation_time = datetime.now()
        self.header = "untitled"
        self.body = "..."

    def get_note_id(self):
        return self.note_id

    def get_creation_time(self):
        return self.creation_time

    def get_header(self):
        return self.header

    def get_body(self):
        return self.body

    def set_header(self, header: str):
        self.header = header

    def set_body(self, body: str):
        self.body = body

    def get_note_info(self):
        return f"Note id: {self.get_note_id()}'\t'Creation time: {self.get_creation_time()}" \
               f"'\n'------------------------------'\n'" \
               f"{self.get_header()}" \
               f"'\n'------------------------------'\n'" \
               f"{self.get_body()}'\n'"

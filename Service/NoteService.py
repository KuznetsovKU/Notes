from Model.Note import Note


class NoteService:
    @staticmethod
    def create_new_note(header: str, body: str) -> Note:
        note = Note()
        note.set_header(header)
        note.set_body(body)
        return note

    @staticmethod
    def change_note(note: Note, header: str, body: str):
        note.set_header(header)
        note.set_body(body)

    @staticmethod
    def delete_note(note: Note):
        note.__del__()


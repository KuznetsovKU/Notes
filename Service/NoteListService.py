from Model.NoteList import NoteList
from Model.Note import Note


class NoteListService:
    nl = NoteList()

    @staticmethod
    def get_note_list(note_list: NoteList = nl) -> list[Note]:
        return note_list.get_note_list()

    @staticmethod
    def add_note_to_list(new_note: Note, note_list: NoteList = nl) -> bool:
        note_list.add_note_to_list(new_note)
        return new_note in note_list.get_note_list()

    @staticmethod
    def delete_note_from_list(note: Note, note_list: NoteList = nl) -> bool:
        note_list.delete_note_from_list(note)
        return note not in note_list

    @staticmethod
    def clear_note_list(note_list: NoteList = nl) -> bool:
        note_list.clear_note_list()
        return len(note_list.get_note_list()) == 0

    @staticmethod
    def find_note(search_type: int, search_arg: str, note_list: NoteList = nl) -> list[Note]:
        output_note_list = []
        match search_type:
            case 1:  # По ID
                for note in note_list.get_note_list():
                    if str(note.get_note_id()) == search_arg:
                        output_note_list.append(note)
            case 2:  # По дате создания / изменения
                for note in note_list.get_note_list():
                    if search_arg.lower() in note.get_creation_or_changing_time().lower():
                        output_note_list.append(note)
            case 3:  # По заголовку
                for note in note_list.get_note_list():
                    if search_arg.lower() in note.get_header().lower():
                        output_note_list.append(note)
            case 4:  # По тексту
                for note in note_list.get_note_list():
                    if search_arg.lower() in note.get_body().lower():
                        output_note_list.append(note)
        return output_note_list

    @staticmethod
    def fill_note_list_from_note_file(notes_from_file: list[dict], note_list: NoteList = nl) -> int:
        for element in notes_from_file:
            note = Note()
            note.set_note_id(element.get('_Note__note_id'))
            note.set_changing_time(element.get('_Note__creation_or_changing_time'))
            note.set_header(element.get('_Note__header'))
            note.set_body(element.get('_Note__body'))
            note_list.add_note_to_list(note)
        return len(note_list.get_note_list())

from .Note import Note


class NoteList:
    def __init__(self):
        self.__note_list = []

    def get_note_list(self) -> list[Note]:
        return self.__note_list

    def add_note_to_list(self, new_note: Note):
        self.__note_list.append(new_note)

    def delete_note_from_list(self, note: Note):
        for element in self.__note_list:
            if element == note:
                self.__note_list.remove(element)
                break

    def clear_note_list(self):
        self.__note_list.clear()

    # def find_max_note_id(self) -> int:
    #     max_note_id = 0
    #     for element in self.__note_list:
    #         if element.get_note_id() > max_note_id:
    #             max_note_id = element.get_note_id()
    #     return max_note_id

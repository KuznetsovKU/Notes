from _datetime import datetime


class Note:
    @staticmethod
    def __set_new_note_id(note_id: int) -> int:
        Note.__note_id += 1
        return note_id

    __note_id = 1
    __creation_time = datetime.now()
    __header = "untitled"
    __body = "..."

    def __init__(self):
        self.__note_id = Note.__set_new_note_id(Note.__note_id)

    def __del__(self):
        del self

    def get_note_id(self):
        return self.__note_id

    def get_creation_time(self):
        return self.__creation_time

    def get_header(self):
        return self.__header

    def get_body(self):
        return self.__body

    def set_header(self, header: str):
        self.__header = header

    def set_body(self, body: str):
        self.__body = body

    def get_note_info(self):
        return f"Note id: {self.get_note_id()}'\t'Creation time: {self.get_creation_time()}" \
               f"'\n'------------------------------'\n'" \
               f"{self.get_header()}" \
               f"'\n'------------------------------'\n'" \
               f"{self.get_body()}'\n'"

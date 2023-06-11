from _datetime import datetime



class Note:
    @staticmethod
    def __set_new_note_id(note_id: int) -> int:
        Note.__note_id += 1
        return note_id

    __note_id = 1
    __creation_or_changing_time = datetime.now().strftime('%d-%m-%y %H:%M:%S')
    __header = "untitled"
    __body = "..."

    def __init__(self):
        self.__note_id = Note.__set_new_note_id(Note.__note_id)

    def __del__(self):
        del self

    def get_note_id(self):
        return self.__note_id

    def get_creation_or_changing_time(self):
        return self.__creation_or_changing_time

    def get_header(self):
        return self.__header

    def get_body(self):
        return self.__body

    def set_note_id(self, note_id: int):
        self.__note_id = note_id

    def set_changing_time(self, date_time):
        self.__creation_or_changing_time = date_time

    def set_header(self, header: str):
        self.__header = header

    def set_body(self, body: str):
        self.__body = body

    def get_note_info(self):
        return f"Note id: {str(self.get_note_id()).rjust(3)}'\t'Creation time: {self.get_creation_or_changing_time()}" \
               f"'\n'------------------------------------------------'\n'" \
               f"{self.get_header()}" \
               f"'\n'------------------------------------------------'\n'" \
               f"{self.get_body()}'\n"

    def get_small_note_info(self):
        return f"Note id: {str(self.get_note_id()).rjust(3)}'\t'Creation time: {self.get_creation_or_changing_time()}" \
               f"'\n'------------------------------------------------'\n'" \
               f"{self.get_header()}" \
               f"'\n'------------------------------------------------'\n'" \
               f"{self.get_body()[:44]}...'\n"

    @classmethod
    def set_class_note_id(cls, new_note_id: int):
        cls.__note_id = new_note_id

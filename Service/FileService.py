import json
from operator import eq

from Model import Note


class FileService:
    @staticmethod
    def check_note_file():
        nf = open('note_file.json', 'a', encoding='utf-8')
        nf.close()

    @staticmethod
    def count_notes() -> int:
        with open('note_file.json', 'r', encoding='utf-8') as nf:
            return len(nf.readlines())

    @staticmethod
    def clear_note_file():
        with open('note_file.json', 'w', encoding='utf-8') as nf:
            nf.write("")
        with open('note_file.json', 'r', encoding='utf-8') as nf:
            return len(nf.readlines()) == 0

    # @staticmethod
    # def find_needed_line(note: Note):
    #     requested_note = FileService.parse_note_to_json(note)
    #     print(requested_note)



    @staticmethod
    def delete_note_from_file(parsed_note: str):
        prev_length = FileService.count_notes()
        # requestes_note = FileService.parse_note_to_json(note)
        temp_list = []
        with open('note_file.json', 'r', encoding='utf-8') as nf:
            for i in nf.read().splitlines():
                if not eq(str(i), str(parsed_note)):
                    temp_list.append(i)
        FileService.clear_note_file()
        FileService.fill_note_file(temp_list)
        with open('note_file.json', 'r', encoding='utf-8') as nf:
            return FileService.count_notes() == prev_length - 1 and parsed_note not in nf.readlines()

    @staticmethod
    def change_note_in_file(note_to_change: str, new_note: Note):
        prev_length = FileService.count_notes()
        FileService.delete_note_from_file(note_to_change)
        return FileService.add_note_to_file(new_note) and FileService.count_notes() == prev_length

    @staticmethod
    def add_note_to_file(note: Note) -> bool:
        with open('note_file.json', 'a', encoding='utf-8') as nf:
            nf.write(FileService.parse_note_to_json(note) + '\n')
        with open('note_file.json', 'r', encoding='utf-8') as nf:
            return FileService.parse_note_to_json(note) in nf.read().splitlines()[-1]

    @staticmethod
    def fill_note_file(note_list: list[str]):
        with open('note_file.json', 'a', encoding='utf-8') as nf:
            for note in note_list:
                nf.write(note + '\n')

    @staticmethod
    def parse_note_to_json(note: Note) -> str:
        note_info = note.__dict__
        return json.dumps(note_info, ensure_ascii=False)

    @staticmethod
    def parse_all_notes_from_json():
        output_list = []
        with open('note_file.json', 'r', encoding='utf-8') as nf:
            for line in nf.read().splitlines():
                note = json.loads(line)
                output_list.append(note)
        return output_list

    @staticmethod
    def export_note(note: Note):
        header = note.get_header()
        note_info = note.__dict__
        with open(f'{header}.json', 'w', encoding='utf-8') as export:
            export.write(json.dumps(note_info, ensure_ascii=False, indent=5))

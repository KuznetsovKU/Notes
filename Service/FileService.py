import json

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

    @staticmethod
    def add_note_to_file(note: Note) -> bool:
        with open('note_file.json', 'a', encoding='utf-8') as nf:
            nf.write(FileService.parse_note_to_json(note) + '\n')
        with open('note_file.json', 'r', encoding='utf-8') as nf:
            return FileService.parse_note_to_json(note) in nf.read().splitlines()[-1]

    @staticmethod
    def parse_note_to_json(note: Note) -> str:
        note_info = note.__dict__
        return json.dumps(note_info, ensure_ascii=False)

    # @staticmethod
    # def fill_note_file(note_list: list[Note]):
    #     with open('note_file.json', 'a', encoding='utf-8') as nf:
    #         for note in note_list:
    #             nf.write(JSONParser.parse_note_to_json(note) + '\n')

    @staticmethod
    def parse_note_from_json():
        output_list = []
        with open('note_file.json', 'r', encoding='utf-8') as nf:
            for line in nf.read().splitlines():
                note = json.loads(line)
                output_list.append(note)
        return output_list


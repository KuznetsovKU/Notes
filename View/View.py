from Model.Note import Note


class View:
    @staticmethod
    def __greetings():
        print('Добро пожаловать в приложение "Заметки"!')
        print()

    @staticmethod
    def farewell():
        print('Вы закончили работу с приложением "Заметки". До свидания!')
        print()

    @staticmethod
    def synchronize_informing(result: bool):
        if result:
            print('Синхронизация записной книжки выполнена успешно.')
            View.__greetings()
        else:
            print('Выполняется синхронизация записной книжки. Пожалуйста, подождите.')

    @staticmethod
    def show_menu(menu):
        print("Выберите необходимую операцию: ")
        for key in menu:
            print(f"{key} : {menu[key]}", end='\t | \t')
        print()
        View.__suggest_choice()

    @staticmethod
    def __suggest_choice():
        print("Введите номер выбранной операции: ", end='')

    @staticmethod
    def ask_search_type():
        print(f"\nКак будем искать? (Для поиска по дате укажите дату в формате ДД-ММ-ГГ)")

    @staticmethod
    def ask_search_parameter(search_type: int):
        print(f'Введите соответствующие данные для поиска "{search_type}": ', end='')

    @staticmethod
    def invalid_command():
        print("Введите корректный номер выбранной операции: ", end='')

    @staticmethod
    def show_all_notes(note_list: list[Note]):
        print()
        if not note_list:
            print("Заметки не найдены")
        else:
            print("Найдены следующие заметки:")
            for note in note_list:
                print(f'{note.get_small_note_info()}')
                print()
        print()

    @staticmethod
    def show_note(note: Note):
        print(note.get_note_info())
        print()

    @staticmethod
    def confirm_note_file_clearing(list_clearing_confirmation: bool, file_clearing_confirmation: bool):
        print()
        if list_clearing_confirmation and file_clearing_confirmation:
            print("Список заметок успешно очищен.")
        else:
            print("Произошла ошибка! Попробуйте повторить операцию.")
        print()

    @staticmethod
    def confirm_note_adding(to_list_adding_confirmation: bool, to_file_adding_confirmation: bool, header):
        print()
        if to_list_adding_confirmation and to_file_adding_confirmation:
            print(f'Заметка "{header}" успешно добавлена.')
        else:
            print("Произошла ошибка! Попробуйте повторить операцию.")
        print()

    @staticmethod
    def ask_to_confirm(operation: str):
        print(f"\nПожалуйста, подтвердите операцию {operation}:")
        print()

    @staticmethod
    def ask_note_header():
        print(f"\nВведите заголовок заметки: ", end='')

    @staticmethod
    def ask_note_body():
        print(f"Введите содержимое заметки: ", end='')


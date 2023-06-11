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
    def step_back_information():
        print('Возврат на предыдуший уровень меню.')

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
    def check_note_list(note_list: list[Note]):
        print()
        if not note_list:
            print("Заметки не найдены")
        else:
            return True

    @staticmethod
    def show_all_notes(note_list: list[Note]):
        # print()
        # if not note_list:
        #     print("Заметки не найдены")
        # else:
        if View.check_note_list(note_list):
            print("Найдены следующие заметки:")
            note_list = sorted(note_list, key=lambda x: x.get_creation_or_changing_time(), reverse=True)
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
            View.__operation_failure()

    @staticmethod
    def confirm_note_adding(to_list_adding_confirmation: bool, to_file_adding_confirmation: bool, header):
        print()
        if to_list_adding_confirmation and to_file_adding_confirmation:
            print(f'Заметка "{header}" успешно добавлена.')
        else:
            View.__operation_failure()

    @staticmethod
    def confirm_note_deleting(from_list_deleting_confirmation: bool, from_file_deleting_confirmation: bool, header):
        print()
        if from_list_deleting_confirmation and from_file_deleting_confirmation:
            print(f'Заметка "{header}" успешно удалена.')
        else:
            View.__operation_failure()

    @staticmethod
    def confirm_note_changing(in_list_changing_confirmation: bool, in_file_changing_confirmation: bool, header):
        print()
        if in_list_changing_confirmation and in_file_changing_confirmation:
            print(f'Заметка "{header}" успешно изменена.')
        else:
            View.__operation_failure()

    @staticmethod
    def ask_to_confirm(operation: str):
        print(f'\nПожалуйста, подтвердите операцию "{operation}":')
        print()

    @staticmethod
    def ask_note_header():
        print(f"\nВведите заголовок заметки: ", end='')

    @staticmethod
    def ask_note_body():
        print(f"Введите содержимое заметки: ", end='')

    @staticmethod
    def __operation_failure():
        print("Произошла ошибка! Попробуйте повторить операцию.")
        print()

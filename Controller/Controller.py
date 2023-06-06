from Service import NoteService, NoteListService, FileService, Validator
from View.View import View
from .Menus import Menus


class Controller:

    @staticmethod
    def program():
        menus = Menus()
        Controller.__synchronize_file_and_note_list()
        program_is_running = True
        while program_is_running:
            View.show_menu(menus.get_main_menu())
            main_menu_command = Controller.__get_user_answer(menus.get_main_menu())
            match main_menu_command:
                case 1:  # Показать все заметки
                    View.show_all_notes(NoteListService.get_note_list())
                case 2:  # Найти заметку
                    View.ask_search_type()
                    View.show_menu(menus.get_search_menu())
                    search_menu_command = Controller.__get_user_answer(menus.get_search_menu())
                    View.ask_search_parameter(menus.get_search_menu()[search_menu_command])
                    search_parameter = input()
                    search_result = NoteListService.find_note(search_menu_command, search_parameter)
                    View.show_all_notes(search_result)
                    if search_result:
                        if len(search_result) > 1:
                            choice_menu = dict(enumerate(list(map(lambda x: x.get_header(), search_result)), start=1))
                            View.show_menu(choice_menu)
                            choice_menu_command = Controller.__get_user_answer(choice_menu)
                            View.show_note(search_result[choice_menu_command - 1])
                        else:
                            View.show_note(search_result[0])
                        View.show_menu(menus.get_note_menu())
                        note_menu_command = Controller.__get_user_answer(menus.get_note_menu())
                        match note_menu_command:
                            case 1:  # Изменить заметку
                                pass
                            case 2:  # Удалить заметку
                                View.ask_to_confirm(menus.get_main_menu())
                                View.show_menu(menus.get_confirm_menu())
                                confirm_menu_command = Controller.__get_user_answer(menus.get_confirm_menu())
                                match confirm_menu_command:
                                    case 1:  # Подтвердить
                                        check1 = NoteListService.delete_note_from_list(1)
                                        check2 = FileService.clear_note_file()
                                        View.confirm_note_file_clearing(check1, check2)
                                    case 2:  # Отменить
                                        continue
                            case 3:  # Выйти в главное меню
                                pass

                    ## не дописано

                case 3:  # Добавить заметку
                    header, body = Controller.__get_new_data()
                    note = NoteService.create_new_note(header, body)
                    check1 = NoteListService.add_note_to_list(note)
                    check2 = FileService.add_note_to_file(note)
                    View.confirm_note_adding(check1, check2, header)
                case 4:  # Очистить список заметок
                    View.ask_to_confirm(menus.get_main_menu()[6])
                    View.show_menu(menus.get_confirm_menu())
                    confirm_menu_command = Controller.__get_user_answer(menus.get_confirm_menu())
                    match confirm_menu_command:
                        case 1:  # Подтвердить
                            check1 = NoteListService.clear_note_list()
                            check2 = FileService.clear_note_file()
                            View.confirm_note_file_clearing(check1, check2)
                        case 2:  # Отменить
                            continue
                case 5:  # Выйти из программы
                    View.farewell()
                    program_is_running = False

    @staticmethod
    def __get_user_answer(menu: dict[int, str]) -> int:
        user_answer = input()
        while not Validator.is_valid_user_answer(menu, user_answer):
            View.invalid_command()
            user_answer = input()
        return int(user_answer)

    @staticmethod
    def __get_new_data():
        View.ask_note_header()
        header = input()
        View.ask_note_body()
        body = input()
        return header, body

    @staticmethod
    def __synchronize_file_and_note_list():
        FileService.check_note_file()
        synchronize_is_complete = False
        while not synchronize_is_complete:
            input_data = FileService.parse_note_from_json()
            note_list_length = NoteListService.fill_note_list_from_note_file(input_data)
            synchronize_is_complete = bool(FileService.count_notes() == note_list_length)
            View.synchronize_informing(synchronize_is_complete)

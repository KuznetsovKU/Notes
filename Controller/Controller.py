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
                    if View.check_note_list(NoteListService.get_note_list()):
                        View.ask_search_type()
                        View.show_menu(menus.get_search_menu())
                        search_menu_command = Controller.__get_user_answer(menus.get_search_menu())
                        View.ask_search_parameter(menus.get_search_menu()[search_menu_command])
                        search_parameter = input()
                        search_result = NoteListService.find_note(search_menu_command, search_parameter)
                        if search_result:
                            # current_note = 0
                            if len(search_result) > 1:
                                View.show_all_notes(search_result)
                                choice_menu_list = list(map(lambda x: x.get_header(), search_result))
                                # choice_menu_list.append('Выйти в главное меню')
                                choice_menu = dict(enumerate(choice_menu_list, start=1))
                                choice_menu.update({0: 'Выйти в главное меню'})
                                View.show_menu(choice_menu)
                                choice_menu_command = Controller.__get_user_answer(choice_menu)
                                if choice_menu_command == 0:
                                    View.step_back_information()
                                    continue
                                else:
                                    current_note = search_result[choice_menu_command - 1]
                                    # View.show_note(search_result[choice_menu_command - 1])
                            else:
                                current_note = search_result[0]
                                # View.show_note(search_result[0])
                            View.show_note(current_note)
                            View.show_menu(menus.get_note_menu())
                            note_menu_command = Controller.__get_user_answer(menus.get_note_menu())
                            match note_menu_command:
                                case 1:  # Изменить заметку
                                    View.ask_to_confirm(menus.get_note_menu()[1])
                                    View.show_menu(menus.get_confirm_menu())
                                    confirm_menu_command = Controller.__get_user_answer(menus.get_confirm_menu())
                                    match confirm_menu_command:
                                        case 1:  # Подтвердить
                                            prev_note_id = current_note.get_note_id()
                                            prev_note_header = current_note.get_header()
                                            header, body = Controller.__get_new_data()
                                            temp_note = FileService.parse_note_to_json(current_note)
                                            NoteService.change_note(current_note, header, body)
                                            new_note_list = NoteListService.find_note(1, str(prev_note_id))
                                            check1 = len(new_note_list) == 1 and new_note_list[0].get_header() == header
                                            check2 = FileService.change_note_in_file(temp_note, new_note_list[0])
                                            View.confirm_note_changing(check1, check2, prev_note_header)
                                        case 0:  # Отменить
                                            View.step_back_information()
                                    pass
                                case 2:  # Удалить заметку
                                    View.ask_to_confirm(menus.get_note_menu()[2])
                                    View.show_menu(menus.get_confirm_menu())
                                    confirm_menu_command = Controller.__get_user_answer(menus.get_confirm_menu())
                                    match confirm_menu_command:
                                        case 1:  # Подтвердить
                                            check1 = NoteListService.delete_note_from_list(current_note)
                                            check2 = FileService.delete_note_from_file(FileService.parse_note_to_json(current_note))  # проверить
                                            View.confirm_note_deleting(check1, check2, current_note.get_header())
                                        case 0:  # Отменить
                                            View.step_back_information()
                                case 3:  # Экспортировать заметку
                                    FileService.export_note(current_note)
                                case 0:  # Выйти в главное меню
                                    View.step_back_information()
                case 3:  # Добавить заметку
                    header, body = Controller.__get_new_data()
                    note = NoteService.create_new_note(header, body)
                    check1 = NoteListService.add_note_to_list(note)
                    check2 = FileService.add_note_to_file(note)
                    View.confirm_note_adding(check1, check2, header)
                case 4:  # Очистить список заметок
                    View.ask_to_confirm(menus.get_main_menu()[4])
                    View.show_menu(menus.get_confirm_menu())
                    confirm_menu_command = Controller.__get_user_answer(menus.get_confirm_menu())
                    match confirm_menu_command:
                        case 1:  # Подтвердить
                            check1 = NoteListService.clear_note_list()
                            check2 = FileService.clear_note_file()
                            View.confirm_note_file_clearing(check1, check2)
                        case 0:  # Отменить
                            continue
                case 0:  # Выйти из программы
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
            input_data = FileService.parse_all_notes_from_json()
            note_list_length = NoteListService.fill_note_list_from_note_file(input_data)
            synchronize_is_complete = bool(FileService.count_notes() == note_list_length)
            View.synchronize_informing(synchronize_is_complete)

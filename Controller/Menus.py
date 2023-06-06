class Menus:
    def __init__(self):
        self.__main_menu = {1: "Показать все заметки",
                            2: "Найти заметку",
                            3: "Добавить заметку",
                            4: "Очистить список заметок",
                            0: "Выйти из программы"}
        self.__note_menu = {1: "Изменить заметку",
                            2: "Удалить заметку",
                            0: "Выйти в главное меню"}
        self.__search_menu = {1: "По ID",
                              2: "По дате создания / изменения",
                              3: "По заголовку",
                              4: "По тексту",
                              0: "Выйти в главное меню"}
        self.__confirm_menu = {1: "Подтвердить",
                               0: "Отменить"}

    def get_main_menu(self):
        return self.__main_menu

    def get_note_menu(self):
        return self.__note_menu

    def get_search_menu(self):
        return self.__search_menu

    def get_confirm_menu(self):
        return self.__confirm_menu

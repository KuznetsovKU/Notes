class Validator:
    @staticmethod
    def is_valid_user_answer(menu: dict[int, str], user_answer: str) -> bool:
        if not user_answer.isdigit():
            return False
        if int(user_answer) not in menu:
            return False
        return True



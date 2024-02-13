# Перемнные чтобы были доступны из любых модулей
# Создаем "базу данных" пользователей
user_dict: dict[int, dict[str, str | int | bool | list | dict]] = {}
tickets_dict: dict[tuple, tuple] = {}
path_dict: dict[tuple, tuple] = {}
cutting_dict: dict[tuple, tuple] = {}
idPlaton = 1157076572
lang:str = "ru"

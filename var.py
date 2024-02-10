# Перемнные чтобы были доступны из любых модулей
# Создаем "базу данных" пользователей
user_dict: dict[int, dict[str, str | int | bool | list | dict]] = {}
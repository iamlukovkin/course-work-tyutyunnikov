import prettytable as pt

from src.data import database


def input_value(message: str, is_int: bool = True) -> int | float | None:
    try:
        if is_int:
            return int(input(message))
        else:
            return float(input(message))
    except ValueError:
        print('Неверное значение')
        if input('Хотите попробовать ещё раз? (y/n) ') == 'y':
            return input_value(message)
        else:
            return None


def get_month_salary(worker: dict) -> float:
    is_can_work_more: bool = worker["is_can_work_more"]
    money_in_month: float = worker["salary"] * 0.6
    if is_can_work_more:
        money_in_month += worker["salary"] * 0.5
    return money_in_month


def get_count_months_for_worker() -> None:
    """
    проверяет сколько месяцев нужно сотруднику для достижения определенной суммы
    :return: bool - может ли перемещаться
    """
    worker_key: int = input_key(False)
    if worker_key is None:
        return
    worker: dict = database[worker_key]
    money_in_month: float = get_month_salary(worker)
    print(f'Зарплата сотрудника в месяц: {money_in_month}')
    required_money: float = input_value('Введите количество денег, которое хотите заработать: ', False)
    print(f'Для достижения суммы в {required_money} потребуется {round(required_money / money_in_month)} месяцев')


def display_worker_info(worker_key: int) -> str:
    """
    :param worker_key: ключ
    :return: str - информация о сотруднике
    """
    worker = database[worker_key]
    return f'{worker_key}: [\n' \
           f'\tИмя: {worker["name"]}\n' \
           f'\tДолжность: {worker["position"]}\n' \
           f'\tКвалификация: {worker["qualification"]}\n' \
           f'\tЗарплата: {worker["salary"]}\n' \
           f'\tМожет подрабатывать: {worker["is_can_work_more"]}\n]'


def display_all(data: dict | None = None) -> str:
    """
    выводит информацию о заготовках
    :param data: база данных
    :return: str - информация о заготовках
    """
    if data is None:
        data = database
    table: pt.PrettyTable = pt.PrettyTable()
    table.field_names = ['Ключ', 'Имя', 'Должность', 'Квалификация', 'Зарплата', 'Может подрабатывать']
    for worker_key in data.keys():
        worker = data[worker_key]
        table.add_row([worker_key, worker["name"], worker["position"], worker["qualification"],
                       worker["salary"], worker["is_can_work_more"]])
    return table.get_string()


def display_ordered_items() -> str:
    """
    Отображает список ресурсов в порядке убывания.
    :return: None
    """
    sort_database = dict(sorted(database.items(), key=lambda item: item[1]['salary'], reverse=True))
    return display_all(sort_database)


def input_key(new_key_required: bool) -> int | None:
    """
    Запрашивает у пользователя ключ записи.
    :return: str: Ключ записи
    """
    if len(database.keys()) == 0 and not new_key_required:
        print('База данных пуста')
        return None
    try:
        print(f"Существующие ключи: {', '.join(map(str, list(database.keys())))}")
        key: int = int(input('Введите ключ записи: '))
        if new_key_required ^ (key in database.keys()):
            return key
        else:
            raise ValueError
    except ValueError:
        print('Неверный ключ')
        if input('Хотите попробовать ещё раз? (y/n) ') == 'y':
            return input_key(new_key_required)
        else:
            return None


def delete_row() -> None:
    key: int = input_key(False)
    if key is not None:
        del database[key]
        print(f'Ресурс {key} удален')


def add_new_rows():
    """
    Добавляет N записей в базу данных.
    """
    n = input_value('Введите количество записей, которые хотите добавить: ')
    for _ in range(n):
        add_new_row()


def input_row_data():
    try:
        new_row = {
            "name": str(input('Введите имя: ')),
            "position": str(input('Введите должность: ')),
            "qualification": str(input('Введите квалификацию: ')),
            "salary": input_value('Введите зарплату: '),
            "is_can_work_more": input('Может подрабатывать? (y/n) ').lower() == 'y'
        }
        return new_row
    except Exception as e:
        print("Не удалось обработать входные данные:", e)
        return input_row_data()


def add_new_row() -> None:
    """
    Добавляет одну запись в базу данных.
    """
    if len(database.keys()) == 0:
        new_key = 0
    else:
        new_key: int = list(database.keys())[-1] + 1
    new_row: dict = input_row_data()
    database[new_key] = new_row
    print(f'Сотрудник #{new_key} добавлен')
    display_all()


def search_row() -> None:
    """
    Поиск записи по ключу.
    :return: None
    """
    key: int = input_key(False)
    if key is not None:
        print(display_worker_info(key))
    return None

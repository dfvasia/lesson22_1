# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


_csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(_csv):
    return [x.split(';') for x in _csv.split('\n')]


def _sort(data):
    return sorted(data, key=lambda y: int(y[1]))


def _filter(data):
    return [t for t in data if int(t[1]) > 10]


def get_users_list():
    # Чтение данных из строки
    data_ = _read(_csv)

    # Сортировка по возрасту по возрастанию
    data = _sort(data_)

    # Фильтрация
    return _filter(data)

    result_data = []
    # for person in _new_data:
    #     if person['age'] < 10:
    #         continue
    #     else:
    #         result_data.append(person)
    # return result_data


if __name__ == '__main__':
    print(get_users_list())

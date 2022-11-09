'''
2.Доработать функцию flat_generator, Должен получиться генератор, который
принимает список списков и возвращает их плоское представление. Функция
test в коде ниже также должна отработать без ошибок.

4.Написать генератор аналогичный генератору из задания 2, но обрабатывающий
списки с любым уровнем вложенности.
'''

import types
import  os
from pathlogger import logger

path = 'flatlog.log'

@logger(path)
def flat_generator(list_of_list):
    for item in list_of_list:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    if os.path.exists(path):
        os.remove(path)
    test_2()
    test_4()

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_ = []
        self.current_iterator = iter(self.list_of_list)
        return self

    def __next__(self):
        try:
            item = next(self.current_iterator)
        except StopIteration:
            if self.list_:
                self.current_iterator = self.list_.pop()
                return next(self)
            else:
                raise
        if type(item) is not list:
            return item
        else:
            self.list_.append(self.current_iterator)
            self.current_iterator = iter(item)
            return next(self)
        return self

def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    print(123)


if __name__ == '__main__':
    test_3()
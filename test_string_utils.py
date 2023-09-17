import pytest
from string_utils import StringUtils
#string_utils = StringUtils()

@pytest.mark.parametrize('string, String', [('hello', 'Hello'), ('Hello', 'Hello'), ('привет как дела', 'Привет как дела'), ('ПРИВЕТ КАК ДЕЛА', 'ПРИВЕТ КАК ДЕЛА'), ('1234', '1234'), ('!@&^*','!@&^*'), ('', ''), (' ', ' ')])
def test_cap(string, String):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == String

@pytest.mark.parametrize('string, new_string', [('Hello ', 'Hello '), (' Hello', 'Hello'), ('     hello', 'hello'), (' hello how are you', 'hello how are you'), ('  12 43 5', '12 43 5')])
def test_trim(string, new_string):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == new_string


@pytest.mark.parametrize('string, delimeter, massive', [('a,b,c,d', ',', ["a", "b", "c", "d"]), ("1:2:3", ":", ["1", "2", "3"]), ('a:b:c', ':', ["a", "b", "c"]), ('-2.0/3.3/0.22', '/', ['-2.0', '3.3', '0.22']), ('','/',[])])
def test_list(string, delimeter, massive):
    test_util = StringUtils()
    res = test_util.to_list(string, delimeter)
    assert res == massive

@pytest.mark.parametrize('string, symbol, new_string', [('skypro', 'pro', True), ('SKYpro', 's', False), ('sky pro', ' ', True), ('1515', '55', False), ('skypro', 'so', False)])
def test_contains(string, symbol, new_string):
    string_util = StringUtils()
    res = string_util.contains(string, symbol)
    assert res == new_string

@pytest.mark.parametrize('string, symbol, new_string', [('skypro', 'sky', 'pro'), ('SKYpro', 'skypro', 'SKYpro'), ('Hello how are you', ' how ', 'Helloare you'), ('15-6*4', '6*4', '15-'), ('HELLO', 'hello', 'HELLO')])
def test_delete(string, symbol, new_string):
    delete = StringUtils()
    res = delete.delete_symbol(string, symbol)
    assert res == new_string


@pytest.mark.parametrize('string, symbol, bool', [('skypro', 's', True), ('SKYpro', 'SK', True), ('Skypro', 's', False), (' skypro', ' ', True), (' SKYPRO', 'S', False), ('', '', True)])
def test_start_with(string, symbol, bool):
    start_with = StringUtils()
    res = start_with.starts_with(string, symbol)
    assert res == bool


@pytest.mark.parametrize('string, symbol, bool', [('skypro', 'o', True), ('SKYpro', 'pro', True), ('Skypro', 'O', False), ('skypro ', ' ', True), ('SKYPRO ', 'O', False), ('', '', True)])
def test_end_with(string, symbol, bool):
    end_with = StringUtils()
    res = end_with.end_with(string, symbol)
    assert res == bool


@pytest.mark.parametrize('string, bool', [('skypro', False), ('', True), (' ', True)])
def test_empty(string, bool):
    empty = StringUtils()
    res = empty.is_empty(string)
    assert res == bool


@pytest.mark.parametrize('list, joiner, result', [([1, 2, 3, -4, 0], ', ', '1, 2, 3, -4, 0'), (['a', 'b', 'c'], ' - ', 'a - b - c'), ([], '', '')])
def to_string(list, joiner, result):
    to_string = StringUtils()
    res = to_string.list_to_string(list, joiner)
    assert res == result
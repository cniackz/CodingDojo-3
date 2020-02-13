from functions import parse_path, generate_structure


def test_parse_path_home():
    path_dir = '/home'
    assert parse_path(path_dir) == ['home']


def test_parse_path_empty_string():
    assert parse_path('') == []


def test_parse_path_double_position():
    path_dir = '/home/MyFolder'
    assert parse_path(path_dir) == ['home', 'MyFolder']


def test_parse_path_with_no_first_slash():
    path_dir = 'home/MyFolder'
    assert parse_path(path_dir) == ['home', 'MyFolder']


def test_parse_path_with_end_slash():
    path_dir = '/home/MyFolder/'
    assert parse_path(path_dir) == ['home', 'MyFolder']


def test_parse_path_with_end_double_slash():
    path_dir = '/home//MyFolder/'
    assert parse_path(path_dir) == ['home', 'MyFolder']


def test_parse_path_with_end_double_slash_at_end():
    path_dir = '/home/MyFolder//'
    assert parse_path(path_dir) == ['home', 'MyFolder']


def test_generate_simple_structure():
    initial_structure = {}
    paths = ['home', 'My Folder', 'File(Dojo).txt']

    result = generate_structure(initial_structure, paths)

    assert result == {'home': {'My Folder': ['File(Dojo).txt']}}



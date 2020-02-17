from functions import parse_path, generate_structure, get_structure


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


def test_add_file_to_existing_structure():
    initial_structure = {'home': {'My Folder': ['File(Dojo).txt']}}
    paths = ['home', 'My Folder', 'File2(Dojo).txt']
    result = generate_structure(initial_structure, paths)
    assert result == {'home': {'My Folder': ['File(Dojo).txt','File2(Dojo).txt']}}

def test_get_structure():
    param = ['/home/foo-bar/file1.txt', '/home/bar/file1.txt']
    expected = {
        'home': {
            'foo-bar': ['file1.txt'],
            'bar': ['file1.txt'],
        },
    }
    result = get_structure(param)
    assert result == expected


def test_one_more_test():
    initial_structure = {'home': {'My Folder': ['File(Dojo).txt', 'File2(Dojo).txt'],'Second Folder':[]}}
    paths = ['home', 'Third Folder', 'another', 'another']
    expected = {
        'home': {
            'My Folder': ['File(Dojo).txt', 'File2(Dojo).txt'],
            'Second Folder': [],
            'Third Folder': {'another': ['another']}
        }
    }
    result = generate_structure(initial_structure,paths)
    assert result == expected
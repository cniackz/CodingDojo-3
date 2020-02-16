def parse_path(path):
    """
    Parse a full path dir into a list
    Input:
        path: /home/MyFolder
    Output:
        ['home', 'MyFolder']
    Input:
        path: %2Fhome%2FMy%20Folder%2FFile%29Dojo%28%2Etxt
    Output:
        ['home', 'My Folder', 'File(Dojo).txt']
    """

    result = []
    split_path = path.split('/')
    for element in split_path:
        if element != '':
            result.append(element)
    return result


def generate_structure(initial_structure, paths):
    """
    Generate/Update a structure based on paths list
    Rules:
        The last element must be inside of a list
        except when the paths length is 1.
        If the length is 1 the return
        is gonna be:
        One Level: {'home': []}
        Two levels: {'home': ['xpto']}
        Three levels: {'home': {'xpto': ['last one']}}
    More Examples:

    Input:
        initial_structure: {}
        paths: ['home', 'My Folder', 'File(Dojo).txt']
    Output:
        {'home': {'My Folder': ['File(Dojo).txt']]}}

    Input:
        initial_structure: {'home': {'My Folder': ['File(Dojo).txt']]}}
        paths: ['home', 'My Folder', 'File2(Dojo).txt']
    Output:
        {'home': {'My Folder': ['File(Dojo).txt', 'File2(Dojo).txt']]]}}

    Input:
        initial_structure: {'home': {'My Folder': ['File(Dojo).txt', 'File2(Dojo).txt']}}
        paths: ['home', 'Second Folder', 'foo-bar']
    Output:
        {'home': {
                  'My Folder': ['File(Dojo).txt', 'File2(Dojo).txt'],
                  'Second Folder': []
                 }
        }
    Input:
        initial_structure: {'home': {'My Folder': ['File(Dojo).txt', 'File2(Dojo).txt']}}
        paths: ['home', 'Third Folder', 'another', 'another']
    Output:
        {'home': {
                  'My Folder': ['File(Dojo).txt', 'File2(Dojo).txt'],
                  'Second Folder': [],
                  'Third Folder': {'another': ['another']}
                 }
        }
    """
    pointer_to_next_level = initial_structure
    folders = paths[:-1]
    for folder in folders:
        if folder in pointer_to_next_level:
            # point to next existing struct
            pointer_to_next_level = pointer_to_next_level[folder]
        else:
            # create new structs
            if folders[-1] == folder:
                # list is for last folder
                # create new list
                pointer_to_next_level[folder] = []
                # point to next new list
                pointer_to_next_level = pointer_to_next_level[folder]
            else:
                # dict is for all except last folder
                # create new dict
                pointer_to_next_level[folder] = {}
                # point to next new dict
                pointer_to_next_level = pointer_to_next_level[folder]
    
    # Append the file to the list
    pointer_to_next_level.append(paths[-1])
            
    return initial_structure


def add_level(dictonary, element):
    dictonary[element] = {}
    return dictonary[element]


def get_structure(dir_list):
    """

    :param dir_list: ['/home/foo-bar/file1.txt', '/home/bar/file1.txt', ...]
    :return: {
            'home': {
                'foo-bar': ['foo-bar'],
                'bar': ['file1.txt'],
                .
                d.
                .
            },
            .
            .
            .
        }
    """
    initial_structure = {}
    for dir in dir_list:
        full_path = parse_path(dir)
        initial_structure = generate_structure(initial_structure, full_path)
    return initial_structure

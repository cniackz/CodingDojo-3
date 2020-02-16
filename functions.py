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
    for x in range(0,len(paths)):
        if x == len(paths)-1:
            # do list
            if paths[x] in pointer_to_next_level:
                # do nothing bc file is in it
                pass
            else:
                # append to new list
                pointer_to_next_level.append(paths[x])
        else:
            # do dict (folders)
            if paths[x] in pointer_to_next_level:
                # point to next existing struct
                pointer_to_next_level = pointer_to_next_level[paths[x]]
            else:
                # create new struct
                if x == len(paths)-2:
                    # point to next new list
                    pointer_to_next_level[paths[x]] = []
                    pointer_to_next_level = pointer_to_next_level[paths[x]]
                else:
                    # point to next new folder
                    pointer_to_next_level[paths[x]] = {}
                    pointer_to_next_level = pointer_to_next_level[paths[x]]
            
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

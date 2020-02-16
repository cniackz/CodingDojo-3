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

def create_structure(ptr,folder,option):
    """
    It creates the structure for the next level 
    and change the pointer to new level
    """
    if option == 'dic':
        ptr[folder] = {}
    if option == 'lis':
        ptr[folder] = []
    ptr = ptr[folder]
    return ptr


def get_next_structure(ptr,folder,option):
    """
    It gets the next existing level when no new structure is needed.
    """
    if folder in ptr:
        # point to next existing struct
        ptr = ptr[folder]
    else:
        ptr = create_structure(ptr,folder,option)
    return ptr


def create_folders(ptr,paths,option):
    """
    It creates a folder in the next level for all except the last second element
    """
    folders = paths[:-2] # all except the last second element
    for folder in folders:
        ptr = get_next_structure(ptr,folder,option)
    return ptr


def create_list(ptr,paths,option):
    """
    It creates a list in the last second element
    """
    folder = paths[-2] # for last second element
    ptr = get_next_structure(ptr,folder,option)
    return ptr

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
    # all you need is one pointer to allocate new nested structure
    ptr = initial_structure
    
    # 1. Create folders if needed
    ptr = create_folders(ptr,paths,'dic')

    # 2. In last folder create list if needed
    ptr = create_list(ptr,paths,'lis')
                
    # 3. Append the file to the list if any
    ptr.append(paths[-1])
            
    # 4. return final structure
    return initial_structure


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

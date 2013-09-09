__author__ = 'dmitrijdackov'

def removeAll(list, val):
    """
    Removes all entries from the list
    """
    return [value for value in list if value != val]

def removeEmpty(list):
    return removeAll(list, '')

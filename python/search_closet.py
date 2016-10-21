def search_closet(items, colour):
    """ (list of str, str) -> list of str
    
    items is a list containing descriptions of the contents of a closet where
    every description has the form 'colour item', where each colour is one word
    and each item is one or more word.  For example:

        ['grey summer jacket', 'orange spring jacket', 'red shoes', 'green hat']

    colour is a colour that is being searched for in items. 
    
    Return a list containing only the items that match the colour.
    
    >>> search_closet(['red summer jacket', 'orange spring jacket', 'red shoes', 'green hat'], 'red')
    ['red summer jacket', 'red shoes']
    >>> search_closet(['red shirt', 'green pants'], 'blue')
    []
    >>> search_closet([], 'mauve')
    []
    """
    i = 0
    coloured_items = [] 
    while i < len(items):
        splitted  = items [i].split()
        if colour in splitted [0]:
            coloured_items.append(items [i]) 
        i += 1
    return coloured_items
            
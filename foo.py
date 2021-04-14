from rest_framework import serializers
from rest_framework.fields import Field

#
# class Fff:
#     a = serializers.IntegerField()
#     b = serializers.CharField()
#

# if __name__ == '__main__':
    # f = Fff()
    #
    # for name in dir(f):
    #     print(type(getattr(f, name)))
    #     if not isinstance(getattr(f, name), Field):
    #         continue
    #     print(name)

if __name__ == '__main__':
    print('Main Start')

    '''
    =====LIST==== список
    
    
        append()	Adds an element at the end of the list
        clear()	Removes all the elements from the list
        copy()	Returns a copy of the list
        count()	Returns the number of elements with the specified value
        extend()	Add the elements of a list (or any iterable), to the end of the current list
        index()	Returns the index of the first element with the specified value
        insert()	Adds an element at the specified position
        pop()	Removes the element at the specified position
        remove()	Removes the first item with the specified value
        reverse()	Reverses the order of the list
        sort()	Sorts the list
    '''
    l = []
    l.append('qwe')
    l.append([112233, [332211], 'qwe'])
    l.append({})
    print(l)
    l.reverse()
    print(l)
    # l.sort() # TypeError: '<' not supported between instances of 'list' and 'dict'
    print(l)

    '''
    =====DICT===== Словари
    
        clear()	Removes all the elements from the dictionary
        copy()	Returns a copy of the dictionary
        fromkeys()	Returns a dictionary with the specified keys and value
        get()	Returns the value of the specified key
        items()	Returns a list containing a tuple for each key value pair
        keys()	Returns a list containing the dictionary's keys
        pop()	Removes the element with the specified key
        popitem()	Removes the last inserted key-value pair
        setdefault()	Returns the value of the specified key. 
            If the key does not exist: insert the key, with the specified value
        update()	Updates the dictionary with the specified key-value pairs
        values()	Returns a list of all the values in the dictionary
    '''
    d = {}

    '''
    ======TUPLE======
    
        count()	Returns the number of times a specified value occurs in a tuple
        index()	Searches the tuple for a specified value and returns the position of where it was found
    '''
    t1 = (1, 2)
    t2 = ([1, 2], [2], {2}, [2])

    print(t2.index({2}))
    print(t2.count({2}))

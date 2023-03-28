def add_to_letter_counts(d, s):
    '''(dict of {str: int}, str) -> NoneType
 
    d is a dictionary where the keys are single-letter strings and the values
    are counts.
 
    For each letter in s, add to that letter's count in d.
 
    Precondition: all the letters in s are keys in d.
 
    >>> letter_counts = {'i': 0, 'r': 5, 'e': 1}
    >>> add_to_letter_counts(letter_counts, 'eerie')
    >>> letter_counts
    {'i': 1, 'r': 6, 'e': 4}
    '''
 
    for c in s:
        if c in letter_counts.keys() ==True:
            letter_counts[c] +=1
letter_counts = {'i': 0, 'r': 5, 'e': 1}
add_to_letter_counts(letter_counts, 'eerie')
letter_counts

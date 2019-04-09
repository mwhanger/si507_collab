import random

def num_vowels(string):
    count = 0
    for c in string:
        if c in 'aeiou':
            count += 1
            if count => 2:
                return True
            else:
                False

        

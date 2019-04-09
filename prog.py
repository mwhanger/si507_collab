import random
import json

def num_vowels(string):
    #count starts at 0
    count = 0
    #looks at each character to see if it's in vowel string
    for c in string:
        #if it is, add 1 to counter
        if c in 'aeiou':
            count += 1
            if count => 2:
                return True
            else:
                False

        

"""
Mexican Wave 

In this simple Kata your task is to create a function that turns a string into a Mexican Wave. 
You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 

 1.  The input string will always be lower case but maybe empty.

 2.  If the character in the string is whitespace then pass over it as if it was an empty seat
"""

def wave(s):

    return [s[:i]+s[i].upper()+s[i+1:] for i in range(len(s)) if s[i].isalpha()]

if __name__ == '__main__':

    print(wave("two words"))
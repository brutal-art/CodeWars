"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, 
the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

ASCII: ord(a) == 97 -> chr(122) == 'z'
"""

def is_pangram(st):
    arr = [x for x in range(97,123)]
    ascii = sorted([ord(c) for c in st.lower() if c.isalpha()])
    return True if arr == list(set(ascii)) else False


if __name__ == '__main__':
    string = "The quick brown fox jumps over the lazy dog."
    print(is_pangram(string))
def is_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    s_lower = s.lower()
    for char in alphabet: 
        if char not in s_lower: 
            return False
    
    return True
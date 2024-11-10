#lex_auth_01269446319507046499

def remove_duplicates(value):
    #start writing your code here
    result = ""
    seen = set()
    
    for char in value:
        if char not in seen:
            seen.add(char)
            result += char
            
    return result
print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
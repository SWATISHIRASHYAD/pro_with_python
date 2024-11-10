#lex_auth_01269442114344550475

def is_palindrome(word):
    word=word.lower()
    start=0
    end=len(word)-1
    if len(word) <= 1:
        return True
    if word[start]==word[end]:
           return is_palindrome(word[start+1:end])
    else:
        return False
               
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
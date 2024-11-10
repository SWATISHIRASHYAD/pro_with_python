#lex_auth_0127382206342184961397

def check_anagram(data1,data2):
    data1=data1.lower()
    data2=data2.lower()
    if len(data1)!=len(data2):
        return False
    for word in set(data1):
        if data1.count(word) != data2.count(word):
            return False
    for i in range(0,len(data1)):
        if data1[i]==data2[i]:
            return False
    return True

print(check_anagram("eat","tea"))
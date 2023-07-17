def is_palindrome(word):
    word=word.lower()
    if(len(word)==1):
        return True
    elif(len(word)==2):
        if(word[0]==word[1]):
            return True
        else:
            return False
    elif(len(word)>2 and word[0]==word[-1]):
        word=word[1:-1]
        result=is_palindrome(word)
        if(result):
            return True
        else:
            return False
    else:
        return False

result=is_palindrome("mm")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")

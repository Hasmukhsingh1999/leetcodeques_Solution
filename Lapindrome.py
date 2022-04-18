def lapindrome(s):
    l = len(s)
    if l%2==0:
        str1 = s[:l//2]
        str2 = s[l//2:]
    else:
        str1 = s[:l//2]
        str2 = s[l//2+1:]
    if sorted(str1)==sorted(str2):
        return True
    else:
        return False
s = input()
print(lapindrome(s))




# if l%2==0:
#     x = s[:l//2]==s[l//2:]
# else:
#     y = s[:l//2]==s[l//2+1]

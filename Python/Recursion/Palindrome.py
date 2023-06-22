def palindrome(s,si,ei):
    if si>=ei:
        return True
    if s[si]==s[ei]:
        return True
    else:
        return False
    palindrome(s,si+1,ei-1)

s = "level"
print(palindrome(s,0,len(s)-1))
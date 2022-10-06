def strtoint(s):
    if len(s)==1:
        return ord(s[0]) - ord('0')
    y = strtoint(s[1:])
    x = ord(s[0]) - ord('0')
    x = x* (10**(len(s) - 1)) + y
    return x

s = "12345"
print(strtoint(s))
print(type(strtoint(s)))
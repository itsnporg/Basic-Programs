def remove(s,a):
    if len(s)==0:
        return s
    smallOutput = remove(s[1:],a)
    if s[0]==a:
        return smallOutput
    else:
        return s[0] + smallOutput

s = "xaxxb"
print(remove(s, 'x'))
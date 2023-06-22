def duplicate(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0]==s[1]:
        return duplicate(s[1:])
    return s[0] + duplicate(s[1:])

print(duplicate("xyxxtttzzwwa"))
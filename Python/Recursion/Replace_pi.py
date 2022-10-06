def replacePi(s):
    if len(s)==0 or len(s)==1:
        return s
    
    if s[0]=="p" and s[1]=="i":
        smalloutput = replacePi(s[2:])
        return "3.14" + smalloutput
    
    else:
        smalloutput = replacePi(s[1:])
        return s[0] + smalloutput

print(replacePi("abcpipipipppddfpi"))
import re
# matching a string in python using regex 

pattern = '^b.b$' # staring with b and ending with b

string = input("Enter pattern or a string to match: > ")

result = re.match(pattern, string)

if result: 
    print("pattern is matched ")
else:
    print("pattern is not matched")
    
    
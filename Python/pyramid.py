
n= int(input('Enter the number of lines: '))  # Taking input from the user
assert n>=1 and n<=15, 'Input should be between 1 and 15'  #Checking the valid input 
def row_generator(i):                         #Function to print the elements of each line
  num=i
  for k in reversed(range(i+1)):
    if k!=0:
     print(k,end=' ')
     i-=1
  for k in range(2,num+1):
    print(k,end=' ')
  return('')                                  #Returning a string of Zero length to avoid returing of None
spaces=n-1
for i in range(1,n+1):                        #Displaying the Triangle 
  s=0
  while (s <spaces):
    print('  ',end='')
    s+=1
  print(row_generator(i))                     #Calling function, row_generator to print each row
  spaces-=1
print('Inverted Triangle')                    
spaces=0
for i in range(n,0,-1):                       #Displaying Inverted Triangle
  s=0
  while (s <spaces):
    print('  ',end='')
    s+=1  
  print(row_generator(i))
  spaces+=1

def palin_num(n):
  temp = n
  rev = 0
  while temp > 0:
      digit = temp % 10
      rev = (rev * 10) + digit
      temp = temp // 10
  if n == rev:
    print('Palindrome')
  else:
    print("Not Palindrome")

n = int(input("Enter a number you want to check for palindrome "))
palin_num(n)

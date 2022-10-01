# Love Calculator

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
combined_name = name1 + name2
lowered_name = combined_name.lower()

# Counting TRUE
T = lowered_name.count("t")
R = lowered_name.count("r")
U = lowered_name.count("u")
E = lowered_name.count("e")

TRUE = T+R+U+E

# Counting LOVE
L = lowered_name.count("l")
O = lowered_name.count("o")
V = lowered_name.count("v")
E = lowered_name.count("e")

LOVE = L+O+V+E

# Concatenating as string
true_love = str(TRUE)+str(LOVE)

# Converting to integer
int_true_love= int(true_love)

if int_true_love < 10 or int_true_love > 90:
    print(f"Your score is {int_true_love}, you go together like coke and mentos.")

elif int_true_love >= 40 and int_true_love <= 50:
    print(f"Your score is {int_true_love}, you are alright together.")

else:
    print(f"Your score is {int_true_love}.")

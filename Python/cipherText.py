"""
!!!CRYPTOGRAPHY Techniques in python!!!  
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# The Caesar Cipher technique is one of the earliest and simplest methods of encryption technique.                                        #
# It’s simply a type of substitution cipher, i.e., each letter                                                                            #
# of a given text is replaced by a letter with a fixed number of positions down the alphabet.                                             #
# __________                                                                                                                              #
# Algorithm                                                                                                                               #
# ----------                                                                                                                              #
#                                                                                                                                         #
# 1.Traverse the given text one character at a time .                                                                                     #
# 2.For each character, transform the given character as per the rule, depending on whether we’re encrypting or decrypting the text.      #
# 3.Return the new string generated.                                                                                                      #
#                                                                                                                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def cesarEncrypt(plain: str, key: int) -> str:
    plain = plain.upper()
    cipher = ""

    for i in range(len(plain)):
        cipher += chr((ord(plain[i]) - 65 + key) % 26 + 65)
        i += 1
    return cipher


def cesarDecrypt(cipher: str, key: int) -> str:
    cipher = cipher.upper()
    plain = ""
    for i in range(len(cipher)):
        plain += chr((ord(cipher[i]) - 65 - key + 26) % 26 + 65)
        i += 1
    return plain


def main():
    print("\n\n \t\t !!! cesar cipher !!! \t\t \n\n")
    print(
        " Enter your choice !! \n1. For Cesar Encryption \n2. For Cesar Decryption \n "
    )
    choice = int(input("choice = "))

    if choice == 1:
        plain = input("Enter a plain text :: ")
        key = int(input("Enter a Encryption Key ::"))
        cipher = cesarEncrypt(plain, key)
        print(f"the decryped message of {plain} with key {key} is {cipher} \n")
    elif choice == 2:
        cipher = input("Enter message that need to be decrypted : ")
        key = int(input("Enter a Encryption Key ::"))
        plain = cesarDecrypt(cipher, key)
        print(f"the decryped message of {cipher} with key {key} is {plain} \n")
    else:
        print("cesar cipher Encryption/Decryption failure !!! ")


if __name__ == "__main__":
    main()

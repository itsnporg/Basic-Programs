# Install language detection
# pip install langdetect

from langdetect import detect
text = input("Enter any text in any language: ")
print(detect(text))

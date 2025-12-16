s = input("Enter a word: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


s = input("Enter a word: ")
rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")

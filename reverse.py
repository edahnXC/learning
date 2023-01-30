a=input("enter the string: ")
print(a[::-1])          #for reversing
if a==a[::-1]:           #for checking if the string is a palindrome
   print("the given string is a palindrome")
else:
   print("the given strings is not a palindrome")
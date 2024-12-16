# #write python program  to reverse the string
# name="HelloWelcome"
# print(name[::-1])

# n=str(input("enter the number"))
# n1=(n[::-1])
# if n==n1:
#     print("number is palindrome")
# else:
#     print("not palindrome")

# #find number of vowels in given string
# n="Hellowelcome"
# vowel="aeiouAEIOU"
# sum=0
# for i in n:
#     if i in vowel:
#         sum=sum+1
# print(f"Number of vowels in a given string is {sum} ")

#split given string to list of words using slit function
# str= "Hi, How are you?"
# print(str.split())

# #find number of words in a given string
# str="Hi How are you?"
# s=" "
# sum=1
# for i in str:
#     if i in s:
#         sum=sum+1
# print(sum)

str="Hi How are you?"
s=str.split()
print(len(s))
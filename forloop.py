for number in range(1,6):
    print("*"*number)


fact=1
number=int(input("enter the number"))
for i in range(1,number+1):
    fact=fact*i
print(fact)

#number between 1 to 50 divisible by 3 and 5
for num in range(1,50):
    if num%3==0 and num%5==0:
        print(num) 

#number between 1 to 50 divisible by 3 or 5
for num in range(1,50):
    if num%3==0 or num%5==0:
       print(num)

#sum of all odd number between 10 and 20
for num in range(11,20):
    if num%2!=0:       
         print(num)

#number is palindrome or not without converting into string


    

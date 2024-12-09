def evenodd(num):
    rem=num%2
    if rem==0:
        print("even")
    else:
        print("odd")   
evenodd(-1)

x=2563
def num_count(x):
    count=0
    while x>0:
        x=x//10
        count+=1
    return count 
digits=num_count(x)
print(digits)       

a=3
b=2
c=10
d=5
e=15
result=(a*b+c/b-d)
print(result)
result1=(c-b**d/b+e*a)
print(result1)
a=10
b="10"
print(a==b)
print(str(a)==b)
a=4.55
b=int(a)+4
print(b)
n=225
a=[1, 2, 3]
b=[1, 2, 3]
print(a is b)

number = int(input("Enter number"))
if number%3==0:
    print("divisible by 3")

if number % 5 == 0:
    print("divisible by 5")

if number % 3 == 0 and number % 5 ==  0 :
    print("Divisible by both 3 and 5")
  
if number%3!=0 and number%5!=0 :
    print("Not divisible by 3 or 5")

 
# #write function to check if a number is prime
# x=int(input("enter the number"))
# def prime(num):
#     for j in range(2,num):
#         if num%j==0:
#             return False
#     return True
# print(prime(x))  

# #function fibonacci numbers
# num=int(input("enter the number")) 
# def fib(x):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(1,x-1):
#         c=a+b
#         print(c)
#         a=b
#         b=c
# fib(num)

# #write function to calculate sum of digits of numbers
# num1=int(input("enter number"))
# def digits(x):
#     sum=0
#     while(x>0):
#         y=x%10
#         sum=sum+y
#         x=x//10
#     return sum
# print(digits(num1))    
    
num=[10,15,20,25,30,45,50]
def oddeven(num):
    len=0
    for i in num:
        if i%2==0:
           len=len+1
    print("number of even number is", len)
    if i%2!=0:
           len=len+1
    print("number of even number is", len)
print(oddeven(num))

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

# #write program to find average of three subject marks using function. function should take three subject marks as parameters and return average of those
# #fixed argument
# def average(x,y,z):
#     return (x+y+z)/3
# print(average(20,20,20))

# #user given value
# x=int(input("enter subject1 marks"))
# y=int(input("enter subject2 marks"))
# z=int(input("enter subject3 marks"))
# def average(x,y,z):
#     return (x+y+z)/3
# print(average(x,y,z))

# #by assigning values
# x=int(input("enter subject1 marks"))
# y=int(input("enter subject2 marks"))
# z=int(input("enter subject3 marks"))
# def average(x,y,z):
#     avg=(x+y+z)/3
#     return avg
# avgg=average(x,y,z)
# print(avgg)

# maths_marks=int(input("enter maths marks:"))
# physics_marks=int(input("enter physics marks:"))
# chemistry_marks=int(input("enter chemistry marks:"))
# average_marks=(maths_marks+physics_marks+chemistry_marks)/3
# if average_marks<35:
#     print("failed")
# else:
#     print("passed")

# #factorial number
# def fact(x):
#     fact=1
#     for i in range(1,x+1):
#         fact=fact*i
#     return fact   
# print(fact(int(input("enter the number:"))))

# x=2563
# def num_count(x):
#     count=0
#     while x>0:
#         x=x//10
#         count+=1
#     return count 
# digits=num_count(x)
# print(digits)   

# #find largest number in a given list using for loop
# list=[10,15,7,8,99,25]
# largest=list[0]
# for i in list:
#     if i>largest:
#         largest=i
# print(largest)

#print numbers in reverse order from 1 to 10
for num in range(10,0,-1):
    print(num)

#display multiplication table of 10
for i in range(1,11):
    print(f"10*{i}={10*i}")

rows=int(input("enter number of rows"))
cols=int(input("enter number of columns"))
if i in range(1,rows+1):
    for j in range(1,cols+1):
        print("*",end=" ")
    print()    

evennum=0
num=[10,15,20,25,30,45,50]
for i in num:
    if i%2==0:
       evennum=evennum+1
print(evennum)

list=[10,15,20,25,30,45,50]
sum=0
for i in list:
    if i%2!=0:
        sum=sum+i
print(sum)


evennum=0
num=[10,15,20,25,30,45,50]
for i in num:
    if i%2==0:
       evennum=evennum+1
print(evennum)

list=[10,15,20,25,30,45,50]
sum=0
for i in list:
    if i%2!=0:
        sum=sum+i
print(sum)


#to find largest num in given list
list1=[10,15,7,8,99,23]
largest=list1[0]
for i in list1:
   if i>largest:
      largest=i
print(largest)

a=8
b=3
print(a*b)
print(a/b)
print(a//b)
print(a%b)
a=10
b=10.5
c="python"
print(type(a),type(b),type(c)) #typefunction
x=5
x=x+3
print(x) #changingvariablevalue
str1="hello"
str2="world"
print(str1+"      "+str2) #stringconcatenation
a=True
b=False
print(a,b)
print(type(a),type(b)) #booleantype

#conditional statement
x=10
if x>5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")    

# conditional with arithmetic
a=15
b=10
if a+b>20:
    print("sum is greater than 20")
else:
    print("sum is less than or equal to 20")

#nested condition
num=7
if num>5:
    if num<10:
        print("number is between 5 and 10")  

#pass or fail display grade if pass display grade
marks=int(input("Enter your marks"))
if(marks>=35):
    print("you have passed in exam")
    if(marks>=80 and marks<=100):
        print("Grade A")
    if(marks>=60 and marks<=79):
        print("Grade B")
    if(marks>=35 and marks<=59):
        print("Grade C")        
else:
    print("failed")

#calculate percentage
maths_marks=int(input("enter maths marks"))
physics_marks=int(input("enter physics marks"))
chemistry_marks=int(input("enter chemistry marks"))
percentage=int(((maths_marks+physics_marks+chemistry_marks)/300)*100)
print("percentage:",percentage)
if percentage>=35:
    print("pass")
else:
    print("fail")
if percentage>=35:
    print("you get a mobile")
    if percentage>=50:
        print("you get a laptop")
        if percentage>=76:
            print("you get a bike")
            if percentage>=90:
                print("you get a car")
else:
    print("no gift")

n=int(input("enter a number"))
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i=i+1

tuple1=(10,20,30,40,50)
for i  in tuple1:
    if i==40:
        print("yes")
    else:
        print("no")  

tuple1=(10,20,30,40,50)
for i  in tuple1:
    if i==40:
        print("yes")
    else:
        print("no")  

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
if percentage>=35:
    print("pass")
else:
    print("fail")


       
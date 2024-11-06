maths_marks=int(input("enter maths marks"))
physics_marks=int(input("enter physics marks"))
chemistry_marks=int(input("enter chemistry marks"))
percentage=int(((maths_marks+physics_marks+chemistry_marks)/300)*100)
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
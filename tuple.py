fruits=('mango','orange','banana',10,20)
for i in fruits:
    print(i)

#print yes if value 40 present in tuple else print no
tuple1=(10,20,30,40,50)
for i  in tuple1:
    if i==40:
        print("yes")
    else:
        print("no")   

#another way :- correct method
tuple1=(10,20,30,40,50)
if 40 in tuple1:
        print("yes")
else:
        print("no")  

tuple1=(10,20,30,40,50)
a=list(tuple1)
a.append(60) 
a.append(70)
a.append(80)  
print(a)     
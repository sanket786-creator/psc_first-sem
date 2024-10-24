def watchMovie():
    money=int(input("enter the money")) #int is necessary otherwise error due to python consider it as string
    if money < 300:
        print("waiting for friend")
    else:
        print("watching movie")    
watchMovie()
1
dict = {}
while True:
    print("--------------------birthday app-----------------")
    print("1.add birthday to the list")
    print("2.show birthday")
    print("3.exit")
    choice = int(input("enter the choice"))
    if choice == 1:
        if len(dict.keys())==0:
            print("nothing to show")
        else:
            name=input("enter name to look for birthday")
            birthday=dict.get(name,"no data found")
            print(birthday)
    elif choice == 2:
         name = input("enter friend's name")
         date = input("enter birthdate")
         dict[name]=date
         print("birthday added")
    elif choice == 3:
         break
    else: 
         print("choose a valid option")
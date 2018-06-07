clothes = ["T-Shirt", "Sweater"]
shopping = 1

while shopping == 1:
    require = 1
    while require == 1:
        choice = input("Welcome to our shop, what do you want (C, R, U, D)? ").lower()
        require = 0
        if choice != "c" and choice != "r" and choice != "u" and choice != "d":
            print()
            print("Please enter C or R or U or D!!!")
            print()
            require = 1
    
    if choice == "c":
        new_item = input("Enter new items: ")
        clothes.append(new_item)
        print()
        print("Our items:", end = " ")
        print(*clothes, sep = ", ", end = "")
        print()
        print()
        
    elif choice == "r":
        print("Our items:", end = " ")
        print(*clothes, sep = ", ", end = "")
        print()
        print()
        
    elif choice == "u":
        require1 = 1
        
        while require1 == 1:
            try:
                position = int(input("Update position? "))
                update_item = input("New item? ")
                require1 = 0
            except ValueError:
                print()
                print("Int please!!!")
                print()
                require1 = 1
                continue
            if position > len(clothes) or position < 1:
                print()
                print("Please choose the position in range 1 -> " + str(len(clothes)) +"!!!")
                print()
                require1 = 1
    
        clothes[position - 1] = update_item
        print("Our items:", end = " ")
        print(*clothes, sep = ", ", end = "")
        print()
        print()
        
    else:
        require2 = 1
        
        while require2 == 1:
            try:
                delete_position = int(input("Delete position? "))
                require2 = 0
            except ValueError:
                print()
                print("Int please!!!")
                require2 = 1
                continue
            if delete_position > len(clothes) or delete_position < 1:
                print()
                print("Please choose the position in range 1 -> " + str(len(clothes)) +"!!!")
                print()
                require2 = 1
                
        clothes.pop(delete_position - 1)
        print()
        print("Our items:", end = " ")
        print(*clothes, sep = ", ", end = "")
        print()
        print()
        
    again = input("Do you want to take another action?(y/n) ").lower()
    while again != "n" and again != "y":
        again = input("Please answer yes or no!(y/n) ").lower()
        print()
                
    if again == "n":
        shopping = 0
        print()
        print("Bye!!!")
        print()

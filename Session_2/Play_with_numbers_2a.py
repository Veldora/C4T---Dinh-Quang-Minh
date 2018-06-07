check_homework = 1

while check_homework == 1:
    require1 = 1

    while require1 == 1:
        homework = input("Which part of my homework do you want to check?(a, b, c, d) ").lower()
        require1 = 0
        if homework != "a" and homework != "b" and homework != "c" and homework != "d":
            print()
            print("Please answer a or b or c or d!!!")
            require1 = 1
    
    if homework == "a":
        require2 = 1

        while require2 == 1:
            a = input("Which part of 'a' do you want to check?(1, 2) ")
            require2 = 0
            if a != "1" and a != "2":
                print()
                print("Please answer 1 or 2!!!")
                require2 = 1

        if a == "1":
            print()
            for i in range(20):
                print(i, end = " ")
        else:
            require3 = 1

            while require3 == 1:
                try:
                    a2 = int(input("Enter a number: "))
                    require3 = 0
                except ValueError:
                    print()
                    print("Int please!!!")
                    require3 = 1
                    continue
                if a2 < 1:
                    print()
                    print(">0 please!!!")
                    require3 = 1

            print()
            for i in range(a2):
                print(i, end = " ")
    elif homework == "b":
        require2b = 1

        while require2b == 1:
            b = input("Which part of 'b' do you want to check?(1, 2) ")
            require2b = 0
            if b != "1" and b != "2":
                print()
                print("Please answer 1 or 2!!!")
                require2b = 1

        if b == "1":
            print()
            b_value1 = 1
            for i in range(20):
                if b_value1 % 2 == 1:
                    print("1", end = " ")
                else:
                    print("0", end = " ")
                b_value1 += 1
        else:
            require3b = 1

            while require3b == 1:
                try:
                    b2 = int(input("Enter the total number of 1's and 0's: "))
                    require3b = 0
                except ValueError:
                    print()
                    print("Int please!!!")
                    require3b = 1
                    continue
                if b2 < 1:
                    print()
                    print(">0 please!!!")
                    require3b = 1

            print()
            b_value2 = 1
            for i in range(b2):
                if b_value2 % 2 == 1:
                    print("1", end = " ")
                else:
                    print("0", end = " ")
                b_value2 += 1

    elif homework == "c":
        require4 = 1

        while require4 == 1:
            c = input("Which part of 'c' do you want to check?(1, 2) ")
            require4 = 0
            if c != "1" and c != "2":
                print()
                print("Please answer 1 or 2!!!")
                require4 = 1

        if c == "1":
            print()
            for y in range(9):
                for x in range(9):
                    multi = (x + 1) * (y + 1)
                    if multi < 10:
                        print(multi, end = "   ")
                    elif multi > 99:
                        print(multi, end = " ")
                    else:
                        print(multi, end = "  ")
                print()
                
        else:
            require3c = 1

            while require3c == 1:
                try:
                    c2 = int(input("Enter a number: "))
                    require3c = 0
                except ValueError:
                    print()
                    print("Int please!!!")
                    require3c = 1
                    continue
                if c2 < 1:
                    print()
                    print(">0 please!!!")
                    require3c = 1

                
            print()
            for y in range(c2):
                for x in range(c2):
                    multi = (x + 1) * (y + 1)
                    if multi < 10:
                        print(multi, end = "   ")
                    elif multi > 99:
                        print(multi, end = " ")
                    else:
                        print(multi, end = "  ")
                print()

    else:
        require2d = 1

        while require2d == 1:
            d = input("Which part of 'd' do you want to check?(1, 2) ")
            require2d = 0
            if d != "1" and d != "2":
                print()
                print("Please answer 1 or 2!!!")
                require2d = 1

        if d == "1":
            print()
            for y in range(9):
                if y % 2 == 0:
                    d_value1 = 1
                else:
                    d_value1 = 0
                for x in range(9):
                    if d_value1 % 2 == 1:
                        print("1", end = " ")
                    else:
                        print("0", end = " ")
                    d_value1 += 1
                print()
                
        else:
            require3d = 1

            while require3d == 1:
                try:
                    d2 = int(input("Enter a number: "))
                    require3d = 0
                except ValueError:
                    print()
                    print("Int please!!!")
                    require3d = 1
                    continue
                if d2 < 1:
                    print()
                    print(">0 please!!!")
                    require3d = 1

            print()
            for y in range(d2):
                if y % 2 == 0:
                    d_value1 = 1
                else:
                    d_value1 = 0
                for x in range(d2):
                    if d_value1 % 2 == 1:
                        print("1", end = " ")
                    else:
                        print("0", end = " ")
                    d_value1 += 1
                print()

    print()
    again = input("Do you want to check again?(y/n) ").lower()
    while again != "n" and again != "y":
        again = input("Please answer yes or no!(y/n) ").lower()
        print()
                
    if again == "n":
        check_homework = 0
        print()
        print("Bye!!!")
        print()



play = 1

while play == 1:
    string = input("String: ").lower()
    letters = {}

    for i in string:
        letter = i in letters
        if i == " ":
            continue
        elif letter == False:
            letters[i] = 1
        else:
            letters[i] += 1

    print()
    for i in letters:
        print(i, letters[i])

    again = input("Do you want to do this shit again?(y/n) ").lower()
    while again != "n" and again != "y":
        again = input("Please answer yes or no!(y/n) ").lower()
        print()
                
    if again == "n":
        play = 0
        print()
        print("Bye!!!")
        print()


from random import *
word_list=["hexagon","champion","meticulous","hello","snake","bomb","crystal"]

play = 1

while play == 1:
    word = randrange(0,7)
    length = len(word_list[word])
    display_list=[]
    
    for i in word_list[word]:
        position = randrange(0,length)
        display_list.insert(position, i)
    for j in range(length):
        print(display_list[j-1], end=" ")
        
    print()
    answer = input("Your answer: ")
    if answer == word_list[word]:
        print("Hura")
    else:
        print(":(")
        
    again = input("Do you want to play again?(y/n) ").lower()
    while again != "n" and again != "y":
        again = input("Please answer yes or no!(y/n) ").lower()
        print()
                
    if again == "n":
        play = 0
        print()
        print("Bye!!!")
        print()

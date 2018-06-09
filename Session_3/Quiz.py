do_the_quiz = 1

while do_the_quiz == 1:
    quiz = [
        {
            "ask": "1+1= ?",
            "choice": ["A. 1", "B. 11", "C. 3", "D. 2"],
            "right_choice": "D",
            "reason": "Wtf? Please go back to the elementary school!"
        },
        {
            "ask": "Who is Albert Einstein?",
            "choice": ["A. A president", "B. A physician", "C. A musician", "D. A king"],
            "right_choice": "B",
            "reason": "Of course he is a physician! Just go and search somewhere in Wikipedia!"
        },
        {
            "ask": "Who discovered America?",
            "choice": ["A. Colombus", "B. Magenlan", "C. Dumbledore", "D. Elizabeth III"],
            "right_choice": "A",
            "reason": "Colombus discovered America. Just go and search somewhere in Wikipedia!"
        }
    ]

    student_answer = []

    for i in range(len(quiz)):
        print(i + 1, end=") ")
        print(quiz[i]["ask"])
        print()
        print(*quiz[i]["choice"], sep="\n")
        print()
        require = 1
        while require == 1:
            answer = input("Your answer? ").upper()
            require = 0
            if answer != "A" and answer != "B" and answer != "C" and answer != "D":
                print("Please answer A or B or C or D!!!")
                require = 1
        student_answer.append(answer)
        print()

    print()

    right_value = 0

    for i in range(len(quiz)):
        print(i + 1, end=". ")
        if student_answer[i] == quiz[i]["right_choice"]:
            print("Bingo! {0} is the correct answer.".format(quiz[i]["right_choice"]))
            right_value += 1
        else:
            print("Nah, the right answer is {0}, not {1}.".format(quiz[i]["right_choice"], student_answer[i]))
            print("Note: {0}".format(quiz[i]["reason"]))
    print()
    print("Your mark is {0:.2f}%".format(right_value * (100 / len(quiz))))
    print()
    again = input("Do you want to do the quiz again?(y/n) ").lower()
    while again != "n" and again != "y":
        again = input("Please answer yes or no!(y/n) ").lower()
        print()

    if again == "n":
        do_the_quiz = 0
        print()
        print("Bye!!!")
        print()

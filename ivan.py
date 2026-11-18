
def display_main_menu():
    print("\n=================================")
    print(" WELCOME SA PROGRAM KO ROPA")
    print("=================================")
    print("[1] PRELIM")
    print("[2] MIDTERM")
    print("[3] FINAL")
    print("[4] EXIT")
    print("=================================")


def display_lesson_menu(quiz, lessons):
    print("\n=================================")
    print("       " + title)
    print("=================================")

    for number, lesson in lessons.items():
        print("[" + str(number) + "] " + lesson[0])

    print("[E] TAKE QUIZ")
    print("[0] BACK TO MAIN MENU")
    print("=================================")


def show_lesson(lesson):
    print("\n=================================")
    print("    MIDTERM     " + lesson[0])
    print("=================================")
    print("\n--- TOPIC INFORMATION ---")

    for info in lesson[1]:
        print(info)

    print("\n=================================")
    print("--- MINI QUIZ ---")
    print(lesson[2])

    for option in lesson[3]:
        print(option)

    answer = input("\nEnter your answer (A/B/C/D): ").upper()

    if answer == lesson[4]:
        print("Correct! Good job!")
    else:
        print("Wrong answer.")
        print("Correct answer is:", lesson[4])

    input("\nPress Enter to return to the lesson menu...")


def take_quiz(title, lessons):
    print("\n=================================")
    print("          " + title + " QUIZ")
    print("=================================")

    print("\nAnswer all the questions below.")

    for number, lesson in lessons.items():
        print("\nQuestion", number, ":", lesson[2])

        for option in lesson[3]:
            print(option)

    print("\n=================================")
    print("           ANSWER SHEET")
    print("=================================")

    answers = []

    for number in lessons:
        while True:
            answer = input("Answer for Question " + str(number) + ": ").upper()

            if answer in ["A", "B", "C", "D"]:
                answers.append(answer)
                break
            else:
                print("Invalid answer. Please enter A, B, C, or D.")

    score = 0

    print("\n=================================")
    print(" RESULTS")
    print("=================================")

    for number, lesson in lessons.items():
        correct = lesson[4]
        user_answer = answers[number - 1]

        if user_answer == correct:
            print("Question", number, "- Correct")
            score += 1
        else:
            print("Question", number, "- Wrong")
            print("Your answer:", user_answer)
            print("Correct answer:", correct)

    print("\nYour Score:", score, "/", len(lessons))

    if score == len(lessons):
        print("Excellent! Perfect score!")
    elif score >= len(lessons) / 2:
        print("Good job! Keep practicing!")
    else:
        print("bawi nalang next year ya!")

    input("\nPress Enter to return to the lesson menu aray ko po!...")


# PRELIM LESSONS

prelim_lessons = {
    1: (
        "What is Python Programming",
        [
            "Python is a high-level programming language.",
            "It is easy to read and understand.",
            "Python is used to create different programs."
        ],
        "What type of programming language is Python?",
        [
            "A. Machine Language",
            "B. High-level Language",
            "C. Assembly Language",
            "D. Binary Language"
        ],
        "B"
    ),

    2: (
        "Python Syntax",
        [
            "Syntax refers to the rules of writing code.",
            "Python is case-sensitive.",
            "Comments in Python use the # symbol."
        ],
        "Which symbol is used to write comments in Python?",
        [
            "A. //",
            "B. <!-- -->",
            "C. #",
            "D. **"
        ],
        "C"
    ),

    3: (
        "Printing Text",
        [
            "The print() function displays information.",
            "Text should be written inside quotation marks.",
            'Example: print("Hello, World!")'
        ],
        "How do you correctly print text in Python?",
        [
            "A. print(Hello)",
            "B. print Hello",
            'C. print("Hello")',
            "D. output(Hello)"
        ],
        "C"
    ),

    4: (
        "Printing Numbers",
        [
            "Numbers can be displayed using print().",
            "Numbers do not need quotation marks.",
            "Example: print(100)"
        ],
        "Which is the correct way to print a number?",
        [
            "A. print(100)",
            'B. print("one hundred")',
            "C. print = 100",
            "D. input(100)"
        ],
        "A"
    ),

    5: (
        "Variable Naming Rules",
        [
            "Variables are used to store information.",
            "A variable name can start with a letter or unde
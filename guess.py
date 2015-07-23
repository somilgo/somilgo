import random

while True:

    score = 0

    while True:

        bound1 = (input("""I'm thinking of an integer between...

>>  """))

        bound2 = (input("""
And...

>>  """))

        try:
            bound1 = int(bound1)
            bound2 = int(bound2)
        except ValueError:
            print("\n")
            print("Please input a valid integer")
            print("\n")
            continue
        if int(bound1) <= int(bound2):

            numb = int((random.randint(int(bound1), int(bound2))))
            break
        elif int(bound1) >= int(bound2):

            numb = int((random.randint(int(bound2), int(bound1))))
            break

    while True:

        guess = input("""
What is your guess?

>>  """)

        try:
            guess = int(guess)
        except ValueError:
            print("\n")
            print("Please input a valid integer")
            print("\n")
            continue
        score += 1
        if guess == numb:

            print("\n"
                  "Correct!")
            if score == 1:
                print("It took you 1 guess!")
            else:
                print("It took you " + str(score) + " guesses.")
            break
        elif guess > numb:
            print("\n")
            print("Lower...")

        elif guess < numb:
            print("\n")
            print("Higher...")

    while True:

        print("\n")
        play = input("""Would you like to play again? (Y/N)

>>  """)
        if play == "y" or play == "Y" or play == "n" or play == "N":
            break
        else:
            print("""
            Please answer "Y" to play again or "N" to quit""")
    if play == "y" or play == "Y":
        print("\n")
        continue
    else:
        print("\n")
        print("Goodbye!")
        break

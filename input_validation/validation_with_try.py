# Program: validation_with_try.py
# Author: John Ran
# Last modified: 2/12/2020

# The purpose of this program is to accept user inputs consisting of name, age, and
# scores and provide an output displaying a summary of that student and their average
# score
NUMBER_TESTS = 3


def average(score1, score2, score3):
    if score1 < 0 or score2 < 0 or score3 < 0:
        raise ValueError
    else:
        return float((score1 + score2 + score3) / NUMBER_TESTS)


def main():
    # Get the student's first and last name, print out their average scores
    last_name = input("Enter the student's last name: ")  # Accepting inputs
    first_name = input("Enter the student's first name: ")
    age = input("Enter the student's age: ")
    try:
        score1 = int(input('Enter the first score: '))
        score2 = int(input('Enter the second score: '))
        score3 = int(input('Enter the third score: '))
        average_scores = average(score1, score2, score3)
        print(last_name + ", " + first_name + " age: " + age + " average grade: %2.2f" % average_scores)
    except ValueError:
        print("Incorrect input. Restart the program to try again")
    return 0


if __name__ == '__main__':
    main()

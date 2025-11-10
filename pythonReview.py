# create a new document called pythonReview.py and answer the following
# questions. 

# Question 1
# Build a program that determines if a student has submitted their class work 
# and homework assignment. The program should use an operator that allows 
# for evaluating 2 conditions and determining if the conditions are true 
# or false.
class_work_submitted = True  
homework_submitted = True  
def check_submission(class_work_submitted, homework_submitted):
    if class_work_submitted and homework_submitted:
        return "Both class work and homework have been submitted."
    elif class_work_submitted:
        return "Class work has been submitted, but homework is missing."
    elif homework_submitted:
        return "Homework has been submitted, but class work is missing."
    else:
        return "Neither class work nor homework has been submitted."
    
print(check_submission(class_work_submitted, homework_submitted))

# hint: find the a operator that allows you to evaluate 2 condtions.

# Question 2
# Create a function that will take in a string as an argument and output 
# that string in reverse order.

txt = "Good morning" [::-1]
print(txt)

# hint: look into string reverse in w3schools

# Question 3
# Create a number guessing function where the program will continuously 
# ask the user to enter a number until the guess the number correctly. 
# Your program should also give the user information on if their guess 
# is close to the correct number. If the guess is above the correct number 
# it should tell the user it is too high and try again. 
# If the guess is below the number, it should tell the user it is too low, 
# it should tell them it is too low and to guess again. Once the user gets 
# it correct the program should congratulate them, stop, and tell them how 
# many attempts they made.
def random_number():
    import random
    return random.randint(1, 100)
def number_guessing_game(correct_number):
    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < correct_number:
            print("Too low Try again.")
        elif guess > correct_number:
            print("Too high Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {correct_number} in {attempts} attempts.")
            break

correct_number = random_number()
number_guessing_game(correct_number)
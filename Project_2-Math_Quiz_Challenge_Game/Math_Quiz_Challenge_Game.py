import random
import time
from colorama import Fore, Style, init

print(Fore.YELLOW + "-----------------------------")
print(" Welcome to Math Quiz Game")
print("-----------------------------",Style.RESET_ALL)

print("Starting in...")
for i in range(3,0,-1):
    print(i)
    time.sleep(1)

easy_operators = ["+","-"]
medium_operators = ["+","-","*","/"]
hard_operators = ["+","-","*","/","**"]
min_value = 2
max_value = 12
total_problems = int(input("Enter the number of problems you want to solve: "))

print("Choose level: ")
level_choice = ["Easy","Medium","Hard"]

for lvl in level_choice:
    print(lvl)
level = input("Enter level: ")

def generate_problem():
    left_value = random.randint(min_value,max_value)
    right_value = random.randint(min_value,max_value)

    if level.lower() == "easy":
        easy_operator = random.choice(easy_operators)
        expression = str(left_value) + " " + easy_operator + " "+str(right_value)
        answer = round(eval(expression), 2)
        return expression, answer
    
    elif level.lower() == "medium":
        medium_operator = random.choice(medium_operators)
        expression = str(left_value) + " " + medium_operator + " "+str(right_value)
        answer = round(eval(expression), 2)
        return expression, answer
    
    else:
        hard_operator = random.choice(hard_operators)
        expression = str(left_value) + " " + hard_operator + " "+str(right_value)
        answer = round(eval(expression), 2)
        return expression, answer

wrong = 0

start_time = time.time()

for i in range(total_problems):
    expression, answer = generate_problem()
    solve = input("Problem " + str(i+1) + ": " + expression + " = ")
    if float(solve) != answer:
        print(Fore.RED + f"Wrong! Correct answer is {answer}",Style.RESET_ALL)
        wrong += 1
    else:
        print(Fore.GREEN + "Correct!",Style.RESET_ALL)

score = total_problems - wrong
accuracy = (score / total_problems) * 100

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("Final Result is in...")
for i in range(3,0,-1):
    print(i)
    time.sleep(1)

print(Fore.YELLOW + "-----------------------------")
print(f"Level selected: {level.capitalize()}")
print("Your score:", score, "/", total_problems)
print(f"Accuracy: {accuracy:.1f}%")
print("Nice work! You finished in ", total_time, "seconds")
print("-----------------------------")
print("",Style.RESET_ALL)
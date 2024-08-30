import time
import random

operators = ['+', '-', '*']
min_value = 1
max_value = 20


def generate_problem():
    eqn_left = random.randint(min_value, max_value)
    eqn_right = random.randint(min_value, max_value)
    eqn_operator = random.choice(operators)

    eqn = str(eqn_left) + ' ' + eqn_operator + ' ' + str(eqn_right)
    soln = str(eval(eqn))

    return eqn, soln


wrong_answers = 0

input_total_problems = input('How many problems do you want to solve in this round: ')
while True:
    if input_total_problems.isdigit():
        total_problems = int(input_total_problems)
        break
    else:
        print('Kindly enter a numerical value only!')


input('Press any key to start when you are ready!')


start_time = time.time()
print('______________________________________')

for i in range(total_problems):
    equation, solution = generate_problem()
    while True:
        user_guess = input('Question#' + str(i + 1) + ': ' + equation + ' = ')
        if user_guess.isnumeric():
            if user_guess == solution:
                break
            else:
                wrong_answers = wrong_answers + 1
        else:
            print('NUMERIC VALUE ONLY!')

print('______________________________________\n')
end_time = time.time()

total_time = round(end_time - start_time, 2)

print('Congratulations! You have completed the challenge in', total_time, 'seconds.')
print('Wrong Answers given:', wrong_answers, 'times.')

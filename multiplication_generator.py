print('Project - Math Tutor')
import random, timeit

number_of_questions = int(input("How many questions do you want?: "))
highest_multiple = int(input("Whats the highest number you want to practice?: "))

'''
List comprehension version:
multiplication_table = [(random.randint(1, highest_multiple), random.randint(1, highest_multiple) for i in range(1, number_of_questions)]
'''
multiplication_table = []
answered_correct = 0
for i in range(number_of_questions):
    multiplication_table.append((random.randint(1, highest_multiple),random.randint(1, highest_multiple)))

for question in multiplication_table:
    num1, num2 = question[0], question[1]
    correct_answer = num1 * num2
    
    response = int(input(f"What is {num1} * {num2}?: "))
    if response == correct_answer:
        answered_correct +=1
        print("Correct!")
    else:
        print("Sorry, thats incorrect.")
final_grade = (answered_correct/len(multiplication_table))*100
print(f"Your final grade is: {answered_correct}/{number_of_questions} : {final_grade}%!")
#!/usr/bin/env python

print('Hello, Welcome to my quiz game!')

answer = input('Are you ready to play the quiz?(yes/no):')
score = 0
total_question=2

if answer.lower()=='yes':
    answer=input('Question 1:Tajuk Lagu Etnik Kreatif dinyanyikan oleh Siti Nur Haliza?')
    if answer.lower() =='Cindai':
        Score += 1
        print('correct:')
    else:
        print('Wrong Answer:(')

print('Thankyou for playing this small quiz game')
print('bye')
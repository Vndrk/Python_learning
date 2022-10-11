# Поработайте с переменными, создайте несколько, выведите на экран. Запросите у
# пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

name = input('Enter your name:')
age = input('Enter your age:')
weight = float(input('Enter your weight (kgs):'))
height = int(input('Enter your heiht (cm):'))
bmi = (weight / (height / 100) ** 2)
print('Your personal data: \n')
print(f'Name: {name} \n')
print(f'Weight: {weight} \n')
print(f'Height: {height} \n')
print((f'BMI: {bmi:.2f}'))

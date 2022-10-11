# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.
time = int(input('Enter time in seconds:'))
hours = time // 3600
minutes_sec = time % 3600
minutes = minutes_sec // 60
seconds = minutes_sec % 60
print(f'время в формате чч:мм:сс: {hours}:{minutes}:{seconds}')

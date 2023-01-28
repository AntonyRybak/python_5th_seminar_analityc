# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_str = 'Абв ывл ллйоуо абв щдышй'
new_str = list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split()))
print(*new_str)

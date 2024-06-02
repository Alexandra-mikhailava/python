height = int(input("Введите рост в см: "))
weight = int(input("Введите вес в кг: "))
height = height / 100
BMI =int(weight / (height * height)) 
print("Ваш индекс массы тела: ", BMI)
len = 24
steps = BMI - 17
min_index = str(16)
number_of_steps = "=" * steps
index_value = chr(124)
remaining_steps = "=" * (40 - BMI)
max_index = str(40)

print(min_index + number_of_steps + index_value + remaining_steps + max_index)

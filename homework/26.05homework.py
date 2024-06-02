phrase = "Не знаю, как там в Лондоне, я не была. Может, там собака - друг человека. А у нас управдом - друг человека!"
print("Шаг 1: Количество символов = ", len(phrase))

length=len(phrase) 
slicedString=phrase[length::-1] 
print ("Шаг 2: Развернутая строка: ", slicedString)
print ("Шаг 3: Каждое слово с большой буквы: ", phrase.title())
print ("Шаг 4: Весь текст прописными буквами: ", phrase.upper())
count = phrase.count('нд')
print ("Шаг 5: Число вхождений нд- " ,count, "раз")
count = phrase.count('ам')
print ("число вхождений ам - " ,count,"раз")
count = phrase.count('о')
print ("число вхождений о - " ,count,"раз")
print ("Шаг 6: Собственное упражнение (вывод символов с 0 по 10 включительно)- ", phrase[0:11:1])
def reverse_words(phrase):
    words = phrase.split()
    words.reverse()
    return ' '.join(words)
reversed_sentence = reverse_words(phrase)
print("Шаг 7: Строка с обратным порядком слов:", reversed_sentence)
print("Шаг 8: Исходная строка:", phrase)


print("Шаг 8: Исходная строка:", phrase)
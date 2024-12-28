current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 ==0:
        #continue команда пропускает осталную часть циклы,возвращает обрартно в начало цикла
        continue

    print(current_number)

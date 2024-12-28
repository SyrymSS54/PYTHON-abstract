#При создание функции,сразу даем параметр аргументам
def decribe_pet(pet_name, animal_type = 'dog'):
    #Выводим информацию о животных
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#Вызоваем функцию с позиционным аргументом
decribe_pet('willie')
#Вызоваем функцию с именованным аргументом
decribe_pet(pet_name='willie')
#Вызоваем функцию с позиционными аргументами
decribe_pet('harry','hamster')
#Вызоваем функцию с именновами аргументами,с порядкам
decribe_pet(pet_name='harry',animal_type='hamster')
#Вызоваем функцию с именновами аргументами без порядка
decribe_pet(animal_type='hamster',pet_name='harry')

#При создание функции,сразу даем параметр аргументам
def decribe_pet(pet_name, animal_type = 'dog'):
    #Выводим информацию о животных
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#Вызоваем функцию и даем параметр аргументу без параметраба параметр с аргументам не трогаем
decribe_pet(pet_name='willie')    
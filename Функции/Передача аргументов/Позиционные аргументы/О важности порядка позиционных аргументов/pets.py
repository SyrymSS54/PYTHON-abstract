#обьявляем функцию и даем аргумент
def decribe_pet(animal_type, pet_name):
    "Выводим информацию"
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#Вызоваем функцию и даем параметр по позиции аргументам
decribe_pet('hamster', 'harry')
#Вызоваем функцию и даем парметр по позиции аргументам,но с реверсам аргументам
decribe_pet('harry', 'hamster')

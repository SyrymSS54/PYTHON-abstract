#создаем функции
def describe_pet(animal_type,pet_name):
    "Выводим информации"
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#Вызоваем функции,но аргументы по имени вставляем
describe_pet(animal_type='hamster',pet_name='harry')
#Если мы поменяем именнованные аргументы  местоми
describe_pet(pet_name='harry',animal_type='hamster')  
#Пишим алогритом ввод данных в списке
usernames = []
while True:
    usernames.append(input("Введите имена:"))
    r = input("Еще добавить(да/нет):")
    if r == "нет":
        break

#Создаем функции
def greet_users(names):
    for name in names:
        msg = "Привет, " + name.title() + "!"
        print(msg)

greet_users(usernames)        

#Создаем функцию с возвращением
def get_formatted_name(first_name,last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

#Вызоваем функцию с возвращением,чтобы вернуть переменную в musician
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
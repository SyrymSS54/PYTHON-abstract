prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
#message = ""

#active это флаг(Флаг-переменная,отвечающий за продолжение циклы или кода)
active = True

while active:

    message = input(prompt)

    if message == 'quit':
        #Флаг становится отрицательной
        active = False
    else:    
        print(message)
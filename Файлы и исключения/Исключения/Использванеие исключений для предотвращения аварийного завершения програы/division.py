while True:
    first_number =  input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond number:")
    if second_number == 'q':
        break
    answer = int(first_number)/int(second_number)
    print(answer)
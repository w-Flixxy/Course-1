user_text = input('Enter some text: ')

print(user_text.upper())

user_number = input("What do you want to doubel? ")

print(int(user_number) * 2)
        #to use numbers for input, we use (int(input))

user_input = input("What do you want to type? ")

user_dec = input("Enter 1 for lowercase and 2 for uppercase: ")

if (int(user_dec)) == 1:
    print(user_input.lower())

if (int(user_dec)) == 2:
    print(user_input.upper())
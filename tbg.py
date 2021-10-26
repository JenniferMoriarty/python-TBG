room = 1
print("Welcome to the scary haunted house!")
while True:
    if room == 1:
        print("You are in room 1. You can go 'n' or 'e'.")
        choice = input()
        if choice ==  'e':
            room = 2
        elif choice == 'n':
            room = 4
        else:
            print("not an option, dummy")
    if room == 2:
        print("You are in room 2. You can go 'n' or 'w'")
        choice = input()
        if choice == 'w':
            room = 1
        elif choice == 'n':
            room = 3
        else:
            print("not an option, dummy")

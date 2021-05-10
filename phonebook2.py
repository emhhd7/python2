phonebook = {
    'Aquarius': '444-444-4444',
    'Libra': '333-333-3333',
    'Aries': '888-888-8888'
}

while True:
    print('\nElectronic Phone Book\n====================\n1. Look up an entry\n2. Set an entry\n3. Delete an entry\n4. List all entries\n5. Quit')

    choice = int(input('\nWhat do you want to do (1-5)? '))

    if choice == 1:
        search = input('What is the contact\'s name? ')
        print(phonebook[search])

    elif choice == 2:
        newName = input('Name: ')
        newNumber = input('Phone Number: ')
        phonebook[newName] = newNumber
        print('\n')
        print(phonebook)

    elif choice == 3:
        deleteName = input('Who would you like to remove? ')
        del phonebook[deleteName]
        print(phonebook)

    elif choice == 4:
        entries = phonebook.items()
        print('\n')
        for entry in entries:
            print('Found entry for: ' + entry[0]+" : "+entry[1])

    elif choice == 5:
        print('Bye.')
        break

    else:
        print('\nPlease input a valid option.')

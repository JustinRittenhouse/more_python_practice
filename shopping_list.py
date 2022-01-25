def shopping_list():
    print('\nHello! Welcome to the shopping list maker.')
    shopping_list = []
    while True:
        response = input('\nWould you like to add or take something off your shopping list? Or are you finished? ["Add"/"Remove"/"Finish"] ').lower()
        if response == 'add':
            addition = input('\nWhat is the name of the item you would like to add? ').title()
            shopping_list.append(addition)
            print(f'\nYou have added {addition} to the list. Your current shopping list looks like:')
            for item in shopping_list:
                print(item)
        elif response == 'remove':
            deletion = input('\nWhat is the name of the item you would like to remove? ').title()
            if deletion in shopping_list:
                shopping_list.remove(deletion)
                print(f'\nYou have removed {deletion} from the list. Your current shopping list looks like:')
            else:
                print(f"\nI'm sorry, {deletion} is not in your shopping list. Your current shopping list looks like: ")
            for item in shopping_list:
                print(item)
        elif response == 'finish':
            print('\nOk! Your finalized shopping list has the following items:')
            for item in shopping_list:
                print(item)
            print('\nThank you, and have a nice shop!')
            break
        else:
            print('\nWhat, are you some kind of code debugger or sumfin\'? The three options were clearly stated! I\'m not angry at you, I\'m only disappointed.')

shopping_list()
import pickle
import re


def save():
    family_file = open("family.pickle", "wb")
    pickle.dump(family, family_file)
    family_file.close()


def check():
    global family
    try:
        family_file = open("family.pickle", "rb")
        family = pickle.load(family_file)
    except IOError or EOFError:
        family = {}


def main_menu():
    check()
    print("----------------------------------------------------------------------")
    print(f"Hello, You are in the Main menu of the program.")
    print("Please, select one of the following options:")
    print("")
    print("[1] - Search contact by Name.")
    print("[2] - Search contact by City.")
    print("[3] - Search contact by Phone number.")
    print("[4] - Show all contacts.")
    print("[5] - Add new contact.")
    print("[6] - Delete contact.")
    print("[7] - Update contact.")
    print("[8] - Quit the program.")
    print("")
    print("Just type down one of the options in the console and press Enter:")
    choice = input()
    cls()
    choice_menu(choice)


def cls():  # cls - Clean the Console Screen
    print('\n' * 25)


def choice_menu(choice):
    if choice == "1":
        search_by_name()
    elif choice == "2":
        search_by_city()
    elif choice == "3":
        search_by_number()
    elif choice == "4":
        show_contacts()
    elif choice == "5":
        add_contact()
    elif choice == "6":
        delete_contact()
    elif choice == "7":
        update_contact()
    elif choice == "8":
        quit()
    else:
        print("----------------------------------------------------------------------")
        print("-----------------------Invalid Choice---------------------------------")
        print("---------------------Back to Main Menu--------------------------------")
        main_menu()


def search_by_name():  # Choice - 1
    print("------------------------------------------------")
    print("Please Enter the Searched Name and press enter:")

    name = input()
    cls()
    while not validate_name(name):
        validate_name_while_text()
        name = input()

        if name == "y":
            cls()
            main_menu()

    not_found = True
    for key, value in family.items():
        if value[0] == name:
            not_found = False
            iterate_values(key, value)

    if not_found:
        cls()
        print("-----------------------------------------------------------------------------------------")
        print(f"Unfortunately, we did not find a contact with this Name: {name} in the contact list!")
        print("But bare in mind, that you can aways add New Contact with that Name from the Main Menu!")
        print("-----------------------------------------------------------------------------------------")

    print("If you want to try the search again, just press [n] and hit Enter:")
    print(f"If you want to go back to the Main Menu, press [y] and hit Enter")

    back_to_main_2()


def search_by_city():  # Choice - 2
    print("Please Enter the Searched City and press enter:")

    city = input()
    cls()
    while not validate_city(city):
        validate_city_while_text()
        city = input()

        if city == "y":
            cls()
            main_menu()

    not_found = True
    cls()
    print("---------------------------------------")
    for key, value in family.items():
        if value[1] == city:
            not_found = False
            iterate_values(key, value)

    if not_found:
        cls()
        print("-----------------------------------------------------------------------------------------")
        print(f"Unfortunately, we did not find a contact with such City: {city} in the contact list!")
        print("But bare in mind, that you can aways add New Contact with that City from the Main Menu!")
        print("-----------------------------------------------------------------------------------------")

    print("If you want to try the search again, just press [c] and hit Enter:")
    print(f"If you want to go back to the Main Menu, press [y] and hit Enter")
    back_to_main_2()


def search_by_number():  # Choice 3 - Search by Number
    print("Please Enter the Searched Telephone Number and press enter:")

    number = input()
    cls()
    while not validate_phone_number(number):
        validate_phone_while_text()
        number = input()

        if number == "y":
            cls()
            main_menu()

    if number in family:
        cls()
        iterate_values(number, [family[number][0], family[number][1]])
    else:
        cls()
        print("---------------------------------------------------------------------------------------------------")
        print(f"Unfortunately, we did not find a contact with such Telephone number: {number} in the contact list!")
        print("But bare in mind, that you can aways add New Contact with that number, from the Main Menu!")
        print("---------------------------------------------------------------------------------------------------")

    print("If you want to try the search again, just press [u] and hit Enter:")
    print(f"If you want to go back to the Main Menu, press [y] and hit Enter")
    back_to_main_2()


def show_contacts():  # Choice - 4
    if len(family.items()) == 0:
        cls()
        print("Unfortunately, there are no contacts to show yet.")
        print("If you want to create a new contact. Press [c] and hit Enter:")
        print("If you want to go back to Main Menu press [y] and hit Enter:")
        choice = input()
        cls()
        if choice == "c":
            add_contact()
        elif choice == "y":
            main_menu()
        else:
            print("Since you didn't press [c] or [y]. I will quit the program for you!")
            quit()
    cls()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("---- The contacts in the list are: ----")
    for number, value in family.items():
        print_contact(number, value)

    print()
    print("- To see the contacts again, just press [a] and hit Enter.")
    print("- To return in Main Menu, press [y] and hit Enter.")
    print("- То Create a new Contact press [c] and hit Enter.")
    print("- To Delete a Contact press [d] and hit Enter.")
    print("- To Update a Contact press [u] and hit Enter.")
    choice = input()
    cls()
    if choice == "y":
        main_menu()
    elif choice == "a":
        show_contacts()
    elif choice == "c":
        add_contact()
    elif choice == "d":
        delete_contact()
    elif choice == "u":
        update_contact()
    else:
        print("Since you didn't say neither [y], [a], [c], [d] or [u] I will quit the program for you")
        quit()


def add_contact():  # Choice - 5
    name = input("Please enter a name: ")

    while not validate_name(name):
        validate_name_while_text()
        name = input()
        if name == "y":
            cls()
            main_menu()

    city = input("Please enter a city: ")
    while not validate_city(city):
        validate_city_while_text()
        city = input()
        if city == "y":
            cls()
            main_menu()

    number = input("Please enter a phone number: ")
    while not validate_phone_number(number):
        validate_phone_while_text()
        number = input()
        if number == "y":
            cls()
            main_menu()

    while number in family.keys():
        cls()
        print("***WARNING***")
        print("The number you are trying to add already exist in the Contacts!")
        number = input("Please provide a different number and press Enter:")
        while not validate_phone_number(number):
            validate_phone_while_text()
            number = input()

    family[number] = [name, city]
    save()
    cls()

    print("--------------------------------------------------------------------------")
    print("Information is successfully added.")
    print("--------------------------------------------------------------------------")
    print("If you want to go back to the main menu, press [y]:")
    print("If you want to add another contact, press [a]:")
    print("If you want to check all the Contacts in the Contacts Manager press [s]")
    print("--------------------------------------------------------------------------")
    choice = input()
    cls()
    if choice == "y":
        main_menu()
    elif choice == "a":
        add_contact()
    elif choice == "s":
        show_contacts()
    else:
        print("Since you didn't press [y], [a] or [s] I will quit the program for you")
        quit()


def delete_contact():  # Choice - 6
    print("Please select one of the following options and Hit Enter")
    print("To Delete Contact, by Name type down: [name].")
    print("To Delete Contact, by Number type down: [number].")
    print("To check all the contacts in the Contacts Manager press: [s].")
    print("To Escape this menu and go back to Main menu press: [y].")

    choice = input()
    cls()
    if choice == "name":
        option = 1
        change_by_name(option)

    elif choice == "number":
        number = input("Please, enter the Telephone Number of the Contact you wish to Delete: ")
        cls()

        while number not in family:
            print("The contact you are trying to Delete, Does not exist")
            print("Please, try again with a Contact Number that is in the Contact List.")
            print("If you are not sure, about the Contact Number you can check all the contacts from the Main Menu.")
            number = input("Please Enter valid Telephone Number or hit [y] for Main Menu")
            cls()
            while not validate_phone_number(number):
                validate_phone_while_text()
                number = input()
                if number == "y":
                    main_menu()

        cls()
        print("***WARNING****")
        print(f"Are you sure the you want to Delete this contact from the Contact List")
        print("---------------------------------------")
        print_contact(number, family[number])
        print(f"Please type down [y] to confirm or [n] to leave it. And go back to Main Menu: ")

        for_del(number)
    elif choice == "y":
        main_menu()
    elif choice == "s":
        show_contacts()
    else:
        print("Since you didn't press [name], [number], [y] or [s] I will quit the program for you")
        quit()


def update_contact():  # Choice - 7
    print("Please select one of the following options:")
    print("To Update Contact by NAME, type down [name] and hit Enter.")
    print("To Update Contact by NUMBER, type down [number] and hit Enter.")
    print("To check all the contacts in the Contact Manager press [s] and hit Enter:")
    print("To Escape this menu and go back to Main menu press [y] and hit Enter.")

    choice = input()
    cls()
    if choice == "name":
        change_by_name(2)

    elif choice == "number":
        number = input("Please, enter the Number of the Contact you wish to Update: ")
        while not validate_phone_number(number):
            validate_phone_while_text()
            number = input()
            if number == "y":
                cls()
                main_menu()

        while number not in family:
            print("The contact you are trying to Update, Does not exist")
            print("Please, try again with a contact that is in the Contact List.")
            print("If you are not sure, about the contact you can check all the contacts from the Main Menu.")
            number = input("Enter an existing phone number or press [y] and hit Enter to go back in Main Menu: ")
            while not validate_phone_number(number):
                validate_phone_while_text()
                number = input()

            if number == "y":
                cls()
                main_menu()
            print("just to Confirm that you are going to Update the Contact:")
        print_contact(number, family[number])
        print("To Confirm press: [y] and hit Enter.")
        print("If not press any other key and hit Enter go back in the Main Menu:")
        cls()
        update_options(number)

    elif choice == "s":
        show_contacts()
    elif choice == "y":
        main_menu()
    else:
        print("Since, you did't select [number], [s] or [y], I will quit the program for you.")
        quit()


def update_options(number):
    old_name = family[number][0]
    old_city = family[number][1]

    y_or_n = input()
    if y_or_n == "y":
        cls()
        print("-----------------------------------------------------------------------")
        print("Please select one of the following options:")
        print("To Update the Contact's name, type down [name] and hit Enter.")
        print("To Update the Contact's city, type down [city] and hit Enter.")
        print("To Update the Contact's number, type down [number] and hit Enter.")
        print("To Escape this menu and go back to Main menu press [y] and hit Enter.")
        print("-----------------------------------------------------------------------")
        update_command = input()

        if update_command == "name":
            print(f"Please type down a new name for the contact and hit enter:")

            new_name = input()

            while not validate_name(new_name):
                validate_name_while_text()
                new_name = input()

            while old_name == new_name:
                print("This is the current name of the contact. Please type down the New Name and hit Enter:")
                new_name = input()
                while not validate_name(new_name):
                    validate_name_while_text()
                    new_name = input()

            if new_name == "y":
                main_menu()

            family[number] = [new_name, old_city]
            save()

            choice_method_for_7(number)

        elif update_command == "city":
            print(f"Please type down the New City for the contact and hit enter:")

            new_city = input()

            while not validate_city(new_city):
                validate_city_while_text()
                new_city = input()

            while old_city == new_city:
                print("This is the current city of the contact. Please type down the new city and hit enter:")
                new_city = input()
                while not validate_city(new_city):
                    validate_city_while_text()
                    new_city = input()

            if new_city == "y":
                main_menu()

            family[number] = [old_name, new_city]
            save()

            choice_method_for_7(number)

        elif update_command == "number":
            print(f"Please type down the new number for the contact and hit Enter:")

            new_number = input()

            while not validate_phone_number(new_number):
                validate_phone_while_text()
                new_number = input()

            while new_number in family.keys():
                if number == new_number:
                    print("This is the current number of the contact.")
                else:
                    print("This phone number already exist in the Contacts Manager by different name!")

                print("Please type down the new phone number and hit Enter:")
                new_number = input()

                while not validate_phone_number(new_number):
                    validate_phone_while_text()
                    new_number = input()

            if new_number == "y":
                cls()
                main_menu()

            family[new_number] = family.pop(number)
            save()

            choice_method_for_7(new_number)
        else:
            cls()
            main_menu()


# oh gosh we MUST change this name
def choice_method_for_7(number):
    print(f"--------------------------------------------------------------")
    print("The Contact was successfully Updated")
    print_contact(number, family[number])
    print(f"If you want to go back to the Main Menu, press [y]:")
    print(f"If you want to Update another contact, press [a]:")
    print(f"If you want to check all the contacts in the Contact Manager, press [s]:")
    print(f"-------------------------------------------------------------------------")

    choice_2 = input()
    cls()
    if choice_2 == "y":
        main_menu()
    elif choice_2 == "a":
        update_contact()
    elif choice_2 == "s":
        show_contacts()
    else:
        print("Since you didn't press [y], [a] or [s] I will quit the program for you")
        quit()


def search_by_name_for_modifications(name):
    print("-------------------------------------------------------------")
    print("Can you select the number of the Contact you wish to Modify:")
    print("Just type down the number, you have selected and press Enter:")
    selected_contact = {}
    counter = 0
    for key, value in family.items():
        if value[0] == name:
            counter += 1
            print("---------------------------------------")
            print(f"Number {counter}: ")
            print(f"Name: {value[0]}")
            print(f"City: {value[1]}")
            print(f"Telephone Number: {key}")
            print("---------------------------------------")
            selected_contact[counter] = key
    choice = input("Please Enter the selected number:")
    cls()
    try:
        while not 0 < int(choice) <= counter:
            print("The number you have selected does not exist from the ones Above:")
            print(f"The number should be in the range [1.....{counter}]")
            print(f"If you wish to stop and return to Main Menu: press [y] OR:")
            choice = input("Please Enter valid number:")
            if choice == "y":
                main_menu()
    except ValueError:
        pass
    number_to_modify = None
    for key, value in selected_contact.items():
        if str(key) == choice:
            number_to_modify = value
    return number_to_modify


def validate_name(name):
    if re.compile("^[A-Z][a-z]{2,}$|^[A-Z][a-z]{2,}[-][A-Z][a-z]{2,}$").match(name):
        return True


def validate_city(city):
    if re.compile("^[A-Z][a-z]{3,}$|^[A-Z][a-z]{3,}[ ]([A-Z]|[a-z])[a-z]{3,}$").match(city):
        return True


def validate_phone_number(number):
    if re.compile("^[\\d]{5,15}$").match(number):
        return True


def validate_name_while_text():
    cls()
    print("***WARNING***")
    print("Invalid name format! The name must be one word starting with a Capital Letter.")
    print("Or two words starting with capital letters and a dash between them.")
    print("Please enter a valid name, like - [Ivan] or [Anna-Maria] оr press [y] for Main Menu: ")


def validate_phone_while_text():
    cls()
    print("***WARNING***")
    print("Invalid phone number! The telephone number must be between 5 and 15 numbers.")
    print("Please enter a valid phone number, or press [y] for Main Menu: ")


def validate_city_while_text():
    cls()
    print("***WARNING***")
    print("Invalid city format! Please enter a valid city, like - [Sofia] or [Veliko Tarnovo]: ")
    print("Please, enter Valid City or press [y] for Main Menu:")


def iterate_values(key, value):
    print(f"-----------There is a match:-----------")
    print(f"Name: {value[0]}")
    print(f"City: {value[1]}")
    print(f"Telephone Number: {key}")
    print("---------------------------------------")


def print_contact(key, value):
    print("---------------------------------------")
    print(f"Name: {value[0]}")
    print(f"City: {value[1]}")
    print(f"Telephone Number: {key}")
    print("---------------------------------------")


def back_to_main_2():
    #
    choice = input()
    cls()
    if choice == "y":
        main_menu()
    elif choice == "n":
        search_by_name()
    elif choice == "c":
        search_by_city()
    elif choice == "u":
        search_by_number()
    else:
        print("Since you didn't say neither [y], nor [a] I will quit the program for you")
        quit()


def for_del(num):
    y_or_n = input()
    cls()
    if y_or_n == "y":
        del family[num]
        save()
        print(f"--------------------------------------------------------------")
        print("The Contact was successfully Deleted")
        print(f"If you want to go back to the main menu, press [y]:")
        print(f"If you want to review all the remaining contacts, press [s]:")
        print(f"--------------------------------------------------------------")
    elif y_or_n == "n":
        cls()
        main_menu()
    else:
        print("Since you didn't press [y] or [n] I will quit the program for you")
        quit()

    choice_2 = input()
    cls()
    if choice_2 == "y":
        main_menu()
    elif choice_2 == "s":
        show_contacts()
    else:
        print("Since you didn't press [y] or [s] I will quit the program for you")
        quit()


def change_by_name(option):
    checker = False
    name = None
    while not checker:
        name = input("Please Enter a name: ")
        cls()

        if name == "y":
            main_menu()

        for key, value in family.items():
            if name == value[0]:
                checker = True
                break

        if not checker:
            cls()
            print("---------------------------------------------------------------------------")
            print("The name you have Entered is NOT in the Contact Manager.")
            print("Try again with a different name. OR press [y] to go back in the Main Menu.")
            print("---------------------------------------------------------------------------")

    count_equal_names = 0
    for key, value in family.items():
        if value[0] == name:
            count_equal_names += 1

    if count_equal_names == 1:
        number = None
        city = None
        for key, value in family.items():
            if value[0] == name:
                number = key
                city = value[1]
                break
        cls()

        if option == 1:
            print("***WARNING****")
            print(f"Are you sure you want to Delete this contact from the Contact List")
            print_contact(number, [name, city])
            print(f"Please type down [y] to confirm or [n] to leave it. And go back to Main Menu: ")
            for_del(number)
        elif option == 2:
            print("***WARNING****")
            print(f"Are you sure the you want to Update this contact from the Contact List")
            print_contact(number, [name, city])
            print(f"Please type down [y] to confirm or [n] to leave it. And go back to Main Menu: ")
            # TO DO
            update_options(number)

    if count_equal_names > 1:
        num_to_del = search_by_name_for_modifications(name)
        cls()

        print("***WARNING****")
        print(f"Are you sure the you want to Update this contact from the Contact List")
        print_contact(num_to_del, [family[num_to_del][0], family[num_to_del][1]])
        print(f"Please type down [y] to confirm or [n] to leave it. And go back to Main Menu: ")
        if option == 1:
            for_del(num_to_del)
        elif option == 2:
            update_options(num_to_del)


if __name__ == "__main__":
    main_menu()

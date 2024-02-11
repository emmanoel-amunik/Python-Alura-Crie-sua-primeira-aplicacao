import os


def _finalize_the_app():
    os.system("cls")
    print("Shutting down the app...\n")


def display_program_name():
    print("Sabor Express\n")


def display_options():
    print("1. Register restaurant")
    print("2. List restaurant")
    print("3. Activate restaurant")
    print("4. Exit\n")


def chose_option():

    chosen_option = int(input("Choose an option: "))

    if chosen_option == 1:
        print("Register restaurant")
    elif chosen_option == 2:
        print("List restaurant")
    elif chosen_option == 3:
        print("Activate restaurant")
    else:
        _finalize_the_app()


def main():
    display_program_name()
    display_options()
    chose_option()


if __name__ == "__main__":
    main()

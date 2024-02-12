import os


restaurants = [{"name": "Square", "category": "Japanese", "activate": False},
               {"name": "Supreme", "category": "Italian", "activate": True},
               {"name": "Cantina", "category": "Italian", "activate": False}]


def display_program_name():
    print("Sabor Express\n")


def display_options():
    print("1. Register restaurant")
    print("2. List restaurant")
    print("3. Activate restaurant")
    print("4. Exit\n")


def chose_option():
    try:
        chosen_option = int(input("Choose an option: "))

        if chosen_option == 1:
            register_new_restaurant()
        elif chosen_option == 2:
            list_restaurants()
        elif chosen_option == 3:
            print("Activate restaurant")
        elif chosen_option == 4:
            _finalize_the_app()
        else:
            invalid_option()
    except ValueError:
        invalid_option()


def invalid_option():

    print("Invalid option!\n")
    return_to_the_main_menu()


def register_new_restaurant():

    show_subtitle("New restaurants register")

    restaurant_name = input("Type the restaurant's name: ")
    category = input(f"Type the {restaurant_name}'s category: ")

    restaurant_data = {"name": restaurant_name, "category": category,
                       "activate": False}
    restaurants.append(restaurant_data)

    print(f"The restaurant {restaurant_name} is successfully registered.")

    return_to_the_main_menu()


def list_restaurants():

    show_subtitle("Listing restaurants...")

    for restaurant in restaurants:
        restaurant_name = restaurant["name"]
        category = restaurant["category"]
        status = restaurant["activate"]
        print(f"-> {restaurant_name} | {category} | {status}")

    return_to_the_main_menu()


def show_subtitle(text):

    os.system("cls")
    print(f"{text}\n")


def return_to_the_main_menu():
    input("\nPress a key to return to the main menu ")
    main()


def _finalize_the_app():
    os.system("cls")
    print("Shutting down the app...\n")


def main():
    display_program_name()
    display_options()
    chose_option()


if __name__ == "__main__":
    main()

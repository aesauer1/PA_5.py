from rental import Rental
import file_handler
import helpers
import manager_menu


def customer_sign_in(gear_list, points, customers, rentals):
    helpers.clear_screen()
    print("Customer Sign In")
    print("=" * 25)
    email = helpers.get_email("Enter your email: ")
    index = file_handler.find_customer(customers, email)

    if index == -1:
        print("No customer found with that email.")
        helpers.pause()
    else:
        customer_menu(customers[index], gear_list, points, rentals)


def customer_menu(customer, gear_list, points, rentals):
    choice = 0
    while choice != 6:
        helpers.clear_screen()
        print(f"Customer Menu - Welcome, {customer.get_first_name()}!")
        print("=" * 25)
        print("1. Browse Available Gear")
        print("2. Search Gear by Type or Name")
        print("3. Start a Rental")
        print("4. End a Rental")
        print("5. View My Rental History")
        print("6. Back to Main Menu")
        choice = helpers.get_menu_choice(1, 6)

        if choice == 1:
            browse_gear(gear_list, points)
        elif choice == 2:
            search_gear(gear_list)
        elif choice == 3:
            start_rental(customer, gear_list, points, rentals)
        elif choice == 4:
            end_rental(customer, gear_list, rentals)
        elif choice == 5:
            view_history(customer, gear_list, rentals)

        if choice != 6:
            helpers.pause()


def print_gear_heading():
    print(f"{'ID':<5}{'Item':<30}{'Type':<10}{'Rate/hr':<9}{'Status':<13}{'Pickup':<8}Units")
    print("-" * 82)


def browse_gear(gear_list, points):
    helpers.clear_screen()
    print("Available Gear")
    print("=" * 25)
    print(f"{'ID':<5}{'Item':<30}{'Type':<10}{'Rate/hr':<9}{'Pickup Point':<28}Units Left")
    print("-" * 92)
    for gear in gear_list:
        if gear.get_status() == "Available" and gear.get_units_available() > 0:
            point_index = file_handler.binary_search_point(
                points, gear.get_pickup_id())
            location = "Unknown"
            if point_index != -1:
                location = points[point_index].get_location()
            print(f"{gear.get_gear_id():<5}{gear.get_item():<30}{gear.get_gear_type():<10}${gear.get_rate():<8.2f}{location:<28}{gear.get_units_available()}")


def search_gear(gear_list):
    helpers.clear_screen()
    print("Search Gear")
    print("=" * 25)
    print("1. Search by Type")
    print("2. Search by Name")
    choice = helpers.get_menu_choice(1, 2)

    if choice == 1:
        search_word = helpers.get_option("Enter a type (Shade, Cooler, Seating, Audio): ",
                                         ["Shade", "Cooler", "Seating", "Audio"])
    else:
        search_word = helpers.get_text("Enter part of the item name: ")

    print()
    print_gear_heading()
    found = 0
    for gear in gear_list:
        if choice == 1 and gear.get_gear_type() == search_word:
            print(gear)
            found = found + 1
        elif choice == 2 and search_word.lower() in gear.get_item().lower():
            print(gear)
            found = found + 1

    if found == 0:
        print("No gear matched your search.")


def start_rental(customer, gear_list, points, rentals):
    helpers.clear_screen()
    print("Start a Rental")
    print("=" * 25)

    if customer.get_status() != "Active":
        print("Your account is inactive, so you cannot start a rental.")
        return

    gear_id = helpers.get_whole_number("Enter the Gear ID you want to rent: ")
    gear_index = file_handler.binary_search_gear(gear_list, gear_id)
    if gear_index == -1:
        print("No gear found with that ID.")
        return

    gear = gear_list[gear_index]
    if gear.get_status() != "Available" or gear.get_units_available() == 0:
        print(f"Sorry, {gear.get_item()} is not available right now.")
        return

    point_index = file_handler.binary_search_point(
        points, gear.get_pickup_id())
    if point_index == -1 or points[point_index].get_status() != "Active":
        print("Sorry, the pickup point for this gear is inactive.")
        return

    date = helpers.get_date("Enter today's date (MM/DD/YYYY): ")
    start = helpers.get_time("Enter the start time (HH:MM, 24-hour): ")

    new_id = file_handler.next_rental_id(rentals)
    rental = Rental(new_id, customer.get_email(), gear.get_gear_id(), gear.get_pickup_id(),
                    date, start, "N/A", "N/A", "Active")
    rentals.append(rental)

    gear.set_units_available(gear.get_units_available() - 1)

    file_handler.save_rentals(rentals)
    file_handler.save_gear(gear_list)

    print()
    print("Rental Started")
    print("=" * 25)
    print(f"Rental ID: {new_id}")
    print(f"Gear: {gear.get_item()}")
    print(f"Pickup Point: {points[point_index].get_location()}")
    print(f"Date: {date}")
    print(f"Start: {start}")
    print(f"Rate: ${gear.get_rate():.2f} per hour")


def end_rental(customer, gear_list, rentals):
    helpers.clear_screen()
    print("End a Rental")
    print("=" * 25)

    count = 0
    for rental in rentals:
        if rental.get_email() == customer.get_email():
            if rental.get_status() == "Active" or rental.get_status() == "Overdue":
                gear_index = file_handler.binary_search_gear(
                    gear_list, rental.get_gear_id())
                print(
                    f"Rental {rental.get_rental_id()}: {gear_list[gear_index].get_item()} - started {rental.get_date()} at {rental.get_start()}")
                count = count + 1

    if count == 0:
        print("You have no rentals to end.")
        return

    rental_id = helpers.get_whole_number("Enter the Rental ID to end: ")
    rental_index = file_handler.find_rental(rentals, rental_id)

    if rental_index == -1:
        print("No rental found with that ID.")
        return

    rental = rentals[rental_index]
    if rental.get_email() != customer.get_email():
        print("That rental does not belong to you.")
        return
    if rental.get_status() == "Completed":
        print("That rental is already completed.")
        return

    manager_menu.finish_rental(rental, gear_list, rentals)


def view_history(customer, gear_list, rentals):
    helpers.clear_screen()
    print("My Rental History")
    print("=" * 25)
    print(f"{'ID':<5}{'Item':<30}{'Date':<12}{'Start':<7}{'End':<7}{'Cost':<9}Status")
    print("-" * 78)

    count = 0
    for rental in rentals:
        if rental.get_email() == customer.get_email():
            gear_index = file_handler.binary_search_gear(
                gear_list, rental.get_gear_id())
            item = "Unknown"
            if gear_index != -1:
                item = gear_list[gear_index].get_item()
            cost = rental.get_cost()
            if cost != "N/A":
                cost = "$" + cost
            print(f"{rental.get_rental_id():<5}{item:<30}{rental.get_date():<12}{rental.get_start():<7}{rental.get_end():<7}{cost:<9}{rental.get_status()}")
            count = count + 1

    if count == 0:
        print("You have no rentals yet.")

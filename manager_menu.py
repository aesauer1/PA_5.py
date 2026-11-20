from gear import Gear
from pickup_point import PickupPoint
from customer import Customer
import file_handler
import helpers


def manager_menu(gear_list, points, customers, rentals):
    choice = 0
    while choice != 4:
        helpers.clear_screen()
        print("Manager Menu")
        print("="*26)
        print("1. Manage Gear")
        print("2. Manage Pickup Points and Rentals")
        print("3. Manage Customers")
        print("4. Back to Main Menu")
        choice = helpers.get_menu_choice(1, 4)

        if choice == 1:
            gear_menu(gear_list, points, rentals)
        elif choice == 2:
            points_menu(gear_list, points, rentals)
        elif choice == 3:
            customers_menu(customers)


def gear_menu(gear_list, points, rentals):
    choice = 0
    while choice != 4:
        helpers.clear_screen()
        print("Manage Gear")
        print("="*26)
        print("1. Add a Gear Item")
        print("2. Remove a Gear Item")
        print("3. Edit a Gear Item")
        print("4. Back")
        choice = helpers.get_menu_choice(1, 4)

        if choice == 1:
            add_gear(gear_list, points)
        elif choice == 2:
            remove_gear(gear_list, rentals)
        elif choice == 3:
            edit_gear(gear_list, points)

        if choice != 4:
            helpers.pause()


def show_all_gear(gear_list):
    print(f"{'ID':<5}{'Item':<30}{'Type':<10}{'Rate/hr':<9}{'Status':<13}{'Pickup':<8}Units")
    print("-" * 82)
    for gear in gear_list:
        print(gear)
    print()


def get_existing_pickup_id(points):
    pickup_id = helpers.get_whole_number("Enter the Pickup ID: ")
    while file_handler.binary_search_point(points, pickup_id) == -1:
        print("No pickup point has that ID.")
        pickup_id = helpers.get_whole_number("Enter the Pickup ID: ")
    return pickup_id


def add_gear(gear_list, points):
    helpers.clear_screen()
    print("Add a Gear Item")
    print("="*26)
    item = helpers.get_text("Item name: ")
    gear_type = helpers.get_option("Type (Shade, Cooler, Seating, Audio): ", [
                                   "Shade", "Cooler", "Seating", "Audio"])
    rate = helpers.get_rate("Hourly rate: ")
    status = helpers.get_option("Status (Available, Unavailable): ", [
                                "Available", "Unavailable"])
    pickup_id = get_existing_pickup_id(points)
    total_units = helpers.get_whole_number("Total units: ")

    new_id = file_handler.next_gear_id(gear_list)
    gear = Gear(new_id, item, gear_type, rate, status,
                pickup_id, total_units, total_units)
    gear_list.append(gear)
    file_handler.save_gear(gear_list)
    print(f"{item} was added with Gear ID {new_id}.")


def remove_gear(gear_list, rentals):
    helpers.clear_screen()
    print("Remove a Gear Item")
    print("="*26)
    show_all_gear(gear_list)
    gear_id = helpers.get_whole_number("Enter the Gear ID to remove: ")
    index = file_handler.binary_search_gear(gear_list, gear_id)

    if index == -1:
        print("No gear found with that ID.")
        return

    gear = gear_list[index]
    for rental in rentals:
        if rental.get_gear_id() == gear_id:
            if rental.get_status() == "Active" or rental.get_status() == "Overdue":
                print("This item has units rented out. End those rentals first.")
                return

    answer = helpers.get_option(
        f"Remove {gear.get_item()}? (Y/N): ", ["Y", "N"])
    if answer == "Y":
        gear_list.pop(index)
        file_handler.save_gear(gear_list)
        print("Gear item removed.")
    else:
        print("Nothing was removed.")


def edit_gear(gear_list, points):
    helpers.clear_screen()
    print("Edit a Gear Item")
    print("="*26)
    show_all_gear(gear_list)
    gear_id = helpers.get_whole_number("Enter the Gear ID to edit: ")
    index = file_handler.binary_search_gear(gear_list, gear_id)

    if index == -1:
        print("No gear found with that ID.")
        return

    gear = gear_list[index]
    print()
    print(f"Editing: {gear.get_item()}")
    print("1. Name")
    print("2. Type")
    print("3. Hourly Rate")
    print("4. Status")
    print("5. Pickup Point")
    print("6. Total Units")
    print("7. Cancel")
    choice = helpers.get_menu_choice(1, 7)

    if choice == 1:
        gear.set_item(helpers.get_text("New name: "))
    elif choice == 2:
        gear.set_gear_type(helpers.get_option("New type (Shade, Cooler, Seating, Audio): ", [
                           "Shade", "Cooler", "Seating", "Audio"]))
    elif choice == 3:
        gear.set_rate(helpers.get_rate("New hourly rate: "))
    elif choice == 4:
        gear.set_status(helpers.get_option(
            "New status (Available, Unavailable): ", ["Available", "Unavailable"]))
    elif choice == 5:
        gear.set_pickup_id(get_existing_pickup_id(points))
    elif choice == 6:
        units_out = gear.get_total_units() - gear.get_units_available()
        new_total = helpers.get_whole_number("New total units: ")
        while new_total < units_out:
            print(
                f"There are {units_out} units rented out, so the total must be at least {units_out}.")
            new_total = helpers.get_whole_number("New total units: ")
        gear.set_total_units(new_total)
        gear.set_units_available(new_total - units_out)
    else:
        print("No changes made.")
        return

    file_handler.save_gear(gear_list)
    print("Gear item updated.")


def points_menu(gear_list, points, rentals):
    choice = 0
    while choice != 5:
        helpers.clear_screen()
        print("Manage Pickup Points and Rentals")
        print("="*26)
        print("1. Add a Pickup Point")
        print("2. Edit a Pickup Point")
        print("3. Change Pickup Point Status")
        print("4. Mark a Rental Completed")
        print("5. Back")
        choice = helpers.get_menu_choice(1, 5)

        if choice == 1:
            add_point(points)
        elif choice == 2:
            edit_point(points)
        elif choice == 3:
            change_point_status(points)
        elif choice == 4:
            mark_rental_completed(gear_list, rentals)

        if choice != 5:
            helpers.pause()


def show_all_points(points):
    print(f"{'ID':<5}{'Location':<28}{'Status':<10}{'Capacity':<10}Last Restocked")
    print("-" * 67)
    for point in points:
        print(point)
    print()


def add_point(points):
    helpers.clear_screen()
    print("Add a Pickup Point")
    print("="*26)
    location = helpers.get_text("Location: ")
    status = helpers.get_option(
        "Status (Active, Inactive): ", ["Active", "Inactive"])
    capacity = helpers.get_whole_number("Capacity: ")
    restocked = helpers.get_date("Last restocked date (MM/DD/YYYY): ")

    new_id = file_handler.next_pickup_id(points)
    point = PickupPoint(new_id, location, status, capacity, restocked)
    points.append(point)
    file_handler.save_pickup_points(points)
    print(f"{location} was added with Pickup ID {new_id}.")


def edit_point(points):
    helpers.clear_screen()
    print("Edit a Pickup Point")
    print("="*26)
    show_all_points(points)
    pickup_id = helpers.get_whole_number("Enter the Pickup ID to edit: ")
    index = file_handler.binary_search_point(points, pickup_id)

    if index == -1:
        print("No pickup point found with that ID.")
        return

    point = points[index]
    print()
    print(f"Editing: {point.get_location()}")
    print("1. Location")
    print("2. Capacity")
    print("3. Last Restocked Date")
    print("4. Cancel")
    choice = helpers.get_menu_choice(1, 4)

    if choice == 1:
        point.set_location(helpers.get_text("New location: "))
    elif choice == 2:
        point.set_capacity(helpers.get_whole_number("New capacity: "))
    elif choice == 3:
        point.set_restocked(helpers.get_date(
            "New restocked date (MM/DD/YYYY): "))
    else:
        print("No changes made.")
        return

    file_handler.save_pickup_points(points)
    print("Pickup point updated.")


def change_point_status(points):
    helpers.clear_screen()
    print("Change Pickup Point Status")
    print("="*26)
    show_all_points(points)
    pickup_id = helpers.get_whole_number("Enter the Pickup ID: ")
    index = file_handler.binary_search_point(points, pickup_id)

    if index == -1:
        print("No pickup point found with that ID.")
        return

    point = points[index]
    status = helpers.get_option(
        "New status (Active, Inactive): ", ["Active", "Inactive"])
    point.set_status(status)
    file_handler.save_pickup_points(points)
    print(f"{point.get_location()} is now {status}.")


def mark_rental_completed(gear_list, rentals):
    helpers.clear_screen()
    print("Mark a Rental Completed")
    print("="*26)

    count = 0
    for rental in rentals:
        if rental.get_status() == "Active" or rental.get_status() == "Overdue":
            print(rental)
            count = count + 1

    if count == 0:
        print("There are no rentals out right now.")
        return

    rental_id = helpers.get_whole_number("Enter the Rental ID to complete: ")
    index = file_handler.find_rental(rentals, rental_id)

    if index == -1:
        print("No rental found with that ID.")
        return
    if rentals[index].get_status() == "Completed":
        print("That rental is already completed.")
        return

    finish_rental(rentals[index], gear_list, rentals)


def finish_rental(rental, gear_list, rentals):
    end_date = helpers.get_date("Enter the return date (MM/DD/YYYY): ")
    end_time = helpers.get_time("Enter the return time (HH:MM, 24-hour): ")
    minutes = helpers.minutes_between(
        rental.get_date(), rental.get_start(), end_date, end_time)
    while minutes <= 0:
        print("The return must be after the start time.")
        end_date = helpers.get_date("Enter the return date (MM/DD/YYYY): ")
        end_time = helpers.get_time("Enter the return time (HH:MM, 24-hour): ")
        minutes = helpers.minutes_between(
            rental.get_date(), rental.get_start(), end_date, end_time)

    gear_index = file_handler.binary_search_gear(
        gear_list, rental.get_gear_id())
    gear = gear_list[gear_index]
    hours = helpers.billed_hours(minutes)
    rental_cost = hours * gear.get_rate()

    discount = 0
    if "@crimson.ua.edu" in rental.get_email():
        discount = rental_cost * 0.10

    late_fee = 0
    if minutes > 240:
        late_fee = 10.00

    cost = rental_cost - discount + late_fee

    rental.set_end(end_time)
    rental.set_cost(f"{cost:.2f}")
    rental.set_status("Completed")

    gear.set_units_available(gear.get_units_available() + 1)

    file_handler.save_rentals(rentals)
    file_handler.save_gear(gear_list)

    print()
    print("Rental Complete")
    print("="*26)
    print(f"Gear: {gear.get_item()}")
    print(f"Start: {rental.get_start()}")
    print(f"End: {end_time}")
    print(f"Billed: {hours} hours x ${gear.get_rate():.2f}")
    if discount > 0:
        print(f"Student Discount (10%): -${discount:.2f}")
    if late_fee > 0:
        print(f"Overdue Fee: ${late_fee:.2f}")
    print(f"Cost: ${cost:.2f}")


def customers_menu(customers):
    choice = 0
    while choice != 4:
        helpers.clear_screen()
        print("Manage Customers")
        print("="*26)
        print("1. Add a Customer")
        print("2. Edit Customer Info")
        print("3. Deactivate a Customer")
        print("4. Back")
        choice = helpers.get_menu_choice(1, 4)

        if choice == 1:
            add_customer(customers)
        elif choice == 2:
            edit_customer(customers)
        elif choice == 3:
            deactivate_customer(customers)

        if choice != 4:
            helpers.pause()


def show_all_customers(customers):
    print(f"{'Email':<25}{'Name':<22}{'Phone':<15}Status")
    print("-" * 68)
    for customer in customers:
        print(customer)
    print()


def add_customer(customers):
    helpers.clear_screen()
    print("Add a Customer")
    print("="*26)
    email = helpers.get_email("Email: ")
    while file_handler.find_customer(customers, email) != -1:
        print("A customer with that email already exists.")
        email = helpers.get_email("Email: ")
    first_name = helpers.get_text("First name: ")
    last_name = helpers.get_text("Last name: ")
    phone = helpers.get_phone("Phone (205-555-0101): ")

    customer = Customer(email, first_name, last_name, phone, "Active")
    customers.append(customer)
    file_handler.save_customers(customers)
    print(f"{first_name} {last_name} was added.")


def edit_customer(customers):
    helpers.clear_screen()
    print("Edit Customer Info")
    print("="*26)
    show_all_customers(customers)
    email = helpers.get_email("Enter the customer's email: ")
    index = file_handler.find_customer(customers, email)

    if index == -1:
        print("No customer found with that email.")
        return

    customer = customers[index]
    print()
    print(f"Editing: {customer.get_first_name()} {customer.get_last_name()}")
    print("1. First Name")
    print("2. Last Name")
    print("3. Phone")
    print("4. Cancel")
    choice = helpers.get_menu_choice(1, 4)

    if choice == 1:
        customer.set_first_name(helpers.get_text("New first name: "))
    elif choice == 2:
        customer.set_last_name(helpers.get_text("New last name: "))
    elif choice == 3:
        customer.set_phone(helpers.get_phone("New phone (205-555-0101): "))
    else:
        print("No changes made.")
        return

    file_handler.save_customers(customers)
    print("Customer updated.")


def deactivate_customer(customers):
    helpers.clear_screen()
    print("Deactivate a Customer")
    print("="*26)
    show_all_customers(customers)
    email = helpers.get_email("Enter the customer's email: ")
    index = file_handler.find_customer(customers, email)

    if index == -1:
        print("No customer found with that email.")
        return

    customer = customers[index]
    if customer.get_status() == "Inactive":
        print("That customer is already inactive.")
        return

    customer.set_status("Inactive")
    file_handler.save_customers(customers)
    print(f"{customer.get_first_name()} {customer.get_last_name()} has been deactivated.")

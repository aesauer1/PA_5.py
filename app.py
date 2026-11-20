import file_handler
import helpers
import customer_menu
import manager_menu
import reports


def main():
    gear_list = file_handler.get_all_gear()
    points = file_handler.get_all_pickup_points()
    customers = file_handler.get_all_customers()
    rentals = file_handler.get_all_rentals()

    choice = 0
    while choice != 4:
        helpers.clear_screen()
        print("Tide Tailgate Main Menu")
        print("="*26)
        print("1. Customer Menu")
        print("2. Manager Menu")
        print("3. Reports")
        print("4. Exit")
        choice = helpers.get_menu_choice(1, 4)

        if choice == 1:
            customer_menu.customer_sign_in(
                gear_list, points, customers, rentals)
        elif choice == 2:
            if helpers.check_manager_pin():
                manager_menu.manager_menu(
                    gear_list, points, customers, rentals)
        elif choice == 3:
            if helpers.check_manager_pin():
                reports.reports_menu(gear_list, points, customers, rentals)

    print("Thanks for using Tide Tailgate. Roll Tide!")


main()

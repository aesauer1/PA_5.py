import file_handler
import helpers


def reports_menu(gear_list, points, customers, rentals):
    choice = 0
    while choice != 6:
        helpers.clear_screen()
        print("Reports")
        print("="*25)
        print("1. Daily Rentals")
        print("2. Gear Currently Out")
        print("3. Overdue Rentals")
        print("4. Most Popular Gear")
        print("5. Revenue")
        print("6. Back to Main Menu")
        choice = helpers.get_menu_choice(1, 6)

        if choice == 1:
            daily_rentals(gear_list, points, rentals)
        elif choice == 2:
            gear_currently_out(gear_list, rentals)
        elif choice == 3:
            overdue_rentals(gear_list, rentals)
        elif choice == 4:
            most_popular_gear(gear_list, rentals)
        elif choice == 5:
            revenue_report(gear_list, points, rentals)

        if choice != 6:
            helpers.pause()


def show_and_save(lines, filename):
    for line in lines:
        print(line)

    print()
    answer = helpers.get_option(
        "Save this report to a text file? (Y/N): ", ["Y", "N"])
    if answer == "Y":
        out_file = open(filename, "w")
        for line in lines:
            out_file.write(line + "\n")
        out_file.close()
        print(f"Report saved to {filename}.")


def get_item_name(gear_list, gear_id):
    index = file_handler.binary_search_gear(gear_list, gear_id)
    if index == -1:
        return "Unknown"
    return gear_list[index].get_item()


def get_location_name(points, pickup_id):
    index = file_handler.binary_search_point(points, pickup_id)
    if index == -1:
        return "Unknown"
    return points[index].get_location()


def daily_rentals(gear_list, points, rentals):
    helpers.clear_screen()
    date = helpers.get_date("Enter a date (MM/DD/YYYY): ")
    lines = []
    lines.append("")
    lines.append(f"Daily Rentals for {date}")
    lines.append("="*25)
    lines.append(
        f"{'ID':<5}{'Customer':<25}{'Item':<30}{'Pickup Point':<28}{'Start':<7}{'End':<7}{'Cost':<10}Status")
    lines.append("-" * 122)

    count = 0
    for rental in rentals:
        if rental.get_date() == date:
            item = get_item_name(gear_list, rental.get_gear_id())
            location = get_location_name(points, rental.get_pickup_id())
            cost = rental.get_cost()
            if cost != "N/A":
                cost = "$" + cost
            lines.append(
                f"{rental.get_rental_id():<5}{rental.get_email():<25}{item:<30}{location:<28}{rental.get_start():<7}{rental.get_end():<7}{cost:<10}{rental.get_status()}")
            count = count + 1

    if count == 0:
        lines.append("No rentals on that date.")
    else:
        lines.append("")
        lines.append(f"Total rentals: {count}")

    show_and_save(lines, "report_daily_rentals.txt")


def gear_currently_out(gear_list, rentals):
    helpers.clear_screen()
    lines = []
    lines.append("Gear Currently Out")
    lines.append("="*25)
    lines.append(
        f"{'ID':<5}{'Item':<30}{'Customer':<25}{'Date':<12}{'Start':<7}Status")
    lines.append("-" * 87)

    count = 0
    for rental in rentals:
        if rental.get_status() == "Active" or rental.get_status() == "Overdue":
            item = get_item_name(gear_list, rental.get_gear_id())
            lines.append(
                f"{rental.get_rental_id():<5}{item:<30}{rental.get_email():<25}{rental.get_date():<12}{rental.get_start():<7}{rental.get_status()}")
            count = count + 1

    if count == 0:
        lines.append("No gear is out right now.")
    else:
        lines.append("")
        lines.append(f"Total out: {count}")

    show_and_save(lines, "report_gear_out.txt")


def overdue_rentals(gear_list, rentals):
    helpers.clear_screen()
    print("Overdue Rentals")
    print("="*25)
    today = helpers.get_date("Enter the current date (MM/DD/YYYY): ")
    now = helpers.get_time("Enter the current time (HH:MM, 24-hour): ")

    lines = []
    lines.append("")
    lines.append(f"Rentals out past the 4-hour limit as of {today} {now}")
    lines.append(
        f"{'ID':<5}{'Item':<30}{'Customer':<25}{'Date':<12}{'Start':<7}Time Out")
    lines.append("-" * 91)

    count = 0
    changed = False
    for rental in rentals:
        if rental.get_status() == "Active" or rental.get_status() == "Overdue":
            minutes = helpers.minutes_between(
                rental.get_date(), rental.get_start(), today, now)
            if minutes > 240:
                if rental.get_status() == "Active":
                    rental.set_status("Overdue")
                    changed = True
                item = get_item_name(gear_list, rental.get_gear_id())
                time_out = f"{minutes // 60}h {minutes % 60}m"
                lines.append(
                    f"{rental.get_rental_id():<5}{item:<30}{rental.get_email():<25}{rental.get_date():<12}{rental.get_start():<7}{time_out}")
                count = count + 1

    if changed:
        file_handler.save_rentals(rentals)

    if count == 0:
        lines.append("No rentals are overdue.")
    else:
        lines.append("")
        lines.append(f"Total overdue: {count}")

    show_and_save(lines, "report_overdue.txt")


def most_popular_gear(gear_list, rentals):
    helpers.clear_screen()

    popular = []
    for gear in gear_list:
        count = 0
        for rental in rentals:
            if rental.get_gear_id() == gear.get_gear_id():
                count = count + 1
        popular.append({"item": gear.get_item(), "count": count})

    for i in range(len(popular) - 1):
        max_index = i
        for j in range(i + 1, len(popular)):
            if popular[j]["count"] > popular[max_index]["count"]:
                max_index = j
        popular[i], popular[max_index] = popular[max_index], popular[i]

    lines = []
    lines.append("Most Popular Gear")
    lines.append("="*25)
    lines.append(f"{'Rank':<6}{'Item':<30}Rentals")
    lines.append("-" * 43)
    rank = 1
    for gear in popular:
        lines.append(f"{rank:<6}{gear['item']:<30}{gear['count']}")
        rank = rank + 1

    show_and_save(lines, "report_popular_gear.txt")


def revenue_report(gear_list, points, rentals):
    helpers.clear_screen()
    lines = []
    lines.append("Revenue Report")
    lines.append("="*25)
    lines.append("")
    lines.append("Revenue by Gear Item")
    lines.append(f"{'Item':<30}Revenue")
    lines.append("-" * 40)

    grand_total = 0
    for gear in gear_list:
        total = 0
        for rental in rentals:
            if rental.get_gear_id() == gear.get_gear_id() and rental.get_cost() != "N/A":
                total = total + float(rental.get_cost())
        lines.append(f"{gear.get_item():<30}${total:.2f}")
        grand_total = grand_total + total

    lines.append("")
    lines.append("Revenue by Pickup Point")
    lines.append(f"{'Pickup Point':<30}Revenue")
    lines.append("-" * 40)

    for point in points:
        total = 0
        for rental in rentals:
            if rental.get_pickup_id() == point.get_pickup_id() and rental.get_cost() != "N/A":
                total = total + float(rental.get_cost())
        lines.append(f"{point.get_location():<30}${total:.2f}")

    lines.append("")
    lines.append(f"Total Revenue: ${grand_total:.2f}")

    show_and_save(lines, "report_revenue.txt")

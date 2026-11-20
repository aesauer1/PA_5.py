def clear_screen():
    print("\n" * 50)


def pause():
    input("Press Enter to continue...")


def check_manager_pin():
    pin = input("Enter the manager PIN: ").strip()
    tries = 1
    while pin != "0329" and tries < 3:
        print("Incorrect PIN.")
        pin = input("Enter the manager PIN: ").strip()
        tries = tries + 1

    if pin == "0329":
        return True

    print("Too many incorrect tries. Returning to the main menu.")
    pause()
    return False


def get_menu_choice(low, high):
    choice = input(f"Enter a choice ({low}-{high}): ").strip()
    while not choice.isdigit() or int(choice) < low or int(choice) > high:
        print(f"Invalid choice. Enter {low}-{high}.")
        choice = input(f"Enter a choice ({low}-{high}): ").strip()
    return int(choice)


def get_whole_number(prompt):
    number = input(prompt).strip()
    while not number.isdigit():
        print("Please enter a whole number (0 or more).")
        number = input(prompt).strip()
    return int(number)


def get_rate(prompt):
    rate = input(prompt).strip()
    while rate.count(".") > 1 or not rate.replace(".", "").isdigit():
        print("Please enter a number, like 4.50.")
        rate = input(prompt).strip()
    return float(rate)


def get_text(prompt):
    text = input(prompt).strip()
    while text == "" or "#" in text:
        print("This cannot be blank or contain #.")
        text = input(prompt).strip()
    return text


def get_option(prompt, options):
    answer = input(prompt).strip().capitalize()
    while answer not in options:
        print("Invalid entry. Please type one of the choices shown.")
        answer = input(prompt).strip().capitalize()
    return answer


def get_email(prompt):
    email = input(prompt).strip().lower()
    while "@" not in email or "." not in email or " " in email or "#" in email:
        print("Invalid email. Example: john@email.com")
        email = input(prompt).strip().lower()
    return email


def get_phone(prompt):
    phone = input(prompt).strip()
    while len(phone) != 12 or phone[3] != "-" or phone[7] != "-" or not phone.replace("-", "").isdigit():
        print("Invalid phone. Use the format 205-555-0101.")
        phone = input(prompt).strip()
    return phone


def is_valid_time(time):
    if len(time) != 5 or time[2] != ":":
        return False
    hour = time[0:2]
    minute = time[3:5]
    if not hour.isdigit() or not minute.isdigit():
        return False
    if int(hour) > 23 or int(minute) > 59:
        return False
    return True


def get_time(prompt):
    time = input(prompt).strip()
    while not is_valid_time(time):
        print("Invalid time. Use 24-hour HH:MM, like 08:30 or 14:45.")
        time = input(prompt).strip()
    return time


def is_valid_date(date):
    if len(date) != 10 or date[2] != "/" or date[5] != "/":
        return False
    month = date[0:2]
    day = date[3:5]
    year = date[6:10]
    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if int(month) < 1 or int(month) > 12:
        return False
    if int(day) < 1 or int(day) > days_in_month[int(month) - 1]:
        return False
    return True


def get_date(prompt):
    date = input(prompt).strip()
    while not is_valid_date(date):
        print("Invalid date. Use MM/DD/YYYY, like 10/10/2026.")
        date = input(prompt).strip()
    return date


def time_to_minutes(time):
    return int(time[0:2]) * 60 + int(time[3:5])


def date_to_days(date):
    days_before_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    month = int(date[0:2])
    day = int(date[3:5])
    year = int(date[6:10])
    return year * 365 + days_before_month[month - 1] + day


def minutes_between(start_date, start_time, end_date, end_time):
    days = date_to_days(end_date) - date_to_days(start_date)
    return days * 24 * 60 + time_to_minutes(end_time) - time_to_minutes(start_time)


def billed_hours(minutes):
    hours = minutes // 60
    if minutes % 60 > 0:
        hours = hours + 1
    if hours == 0:
        hours = 1
    return hours

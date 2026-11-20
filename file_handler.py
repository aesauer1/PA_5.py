from gear import Gear
from pickup_point import PickupPoint
from customer import Customer
from rental import Rental


def get_all_gear():
    gear_list = []
    in_file = open("gear.txt", "r")
    for line in in_file:
        temp_list = line.strip().split("#")
        gear = Gear(int(temp_list[0]), temp_list[1], temp_list[2], float(temp_list[3]),
                    temp_list[4], int(temp_list[5]), int(temp_list[6]), int(temp_list[7]))
        gear_list.append(gear)
    in_file.close()
    selection_sort_gear(gear_list)
    return gear_list


def get_all_pickup_points():
    points = []
    in_file = open("pickup_points.txt", "r")
    for line in in_file:
        temp_list = line.strip().split("#")
        point = PickupPoint(int(temp_list[0]), temp_list[1], temp_list[2], int(
            temp_list[3]), temp_list[4])
        points.append(point)
    in_file.close()
    selection_sort_points(points)
    return points




def get_all_customers():
    customers = []
    in_file = open("customers.txt", "r")
    for line in in_file:
        temp_list = line.strip().split("#")
        customer = Customer(
            temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4])
        customers.append(customer)
    in_file.close()
    return customers


def get_all_rentals():
    rentals = []
    in_file = open("rentals.txt", "r")
    for line in in_file:
        temp_list = line.strip().split("#")
        rental = Rental(int(temp_list[0]), temp_list[1], int(temp_list[2]), int(temp_list[3]),
                        temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8])
        rentals.append(rental)
    in_file.close()
    return rentals


def save_gear(gear_list):
    out_file = open("gear.txt", "w")
    for gear in gear_list:
        out_file.write(gear.to_file() + "\n")
    out_file.close()


def save_pickup_points(points):
    out_file = open("pickup_points.txt", "w")
    for point in points:
        out_file.write(point.to_file() + "\n")
    out_file.close()


def save_customers(customers):
    out_file = open("customers.txt", "w")
    for customer in customers:
        out_file.write(customer.to_file() + "\n")
    out_file.close()


def save_rentals(rentals):
    out_file = open("rentals.txt", "w")
    for rental in rentals:
        out_file.write(rental.to_file() + "\n")
    out_file.close()


def selection_sort_gear(gear_list):
    for i in range(len(gear_list) - 1):
        minimum = i
        for j in range(i+1, len(gear_list)):
            if gear_list[j].get_gear_id() < gear_list[minimum].get_gear_id():
                minimum = j
        gear_list[i], gear_list[minimum] = gear_list[minimum], gear_list[i]


def selection_sort_points(points):
    for i in range(len(points) - 1):
        minimum = i
        for j in range(i+1, len(points)):
            if points[j].get_pickup_id() < points[minimum].get_pickup_id():
                minimum = j
        points[i], points[minimum] = points[minimum], points[i]


def binary_search_gear(gear_list, gear_id):
    low = 0
    high = len(gear_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if gear_list[mid].get_gear_id() == gear_id:
            return mid
        elif gear_list[mid].get_gear_id() < gear_id:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_point(points, pickup_id):
    low = 0
    high = len(points) - 1
    while low <= high:
        mid = (low + high) // 2
        if points[mid].get_pickup_id() == pickup_id:
            return mid
        elif points[mid].get_pickup_id() < pickup_id:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def find_customer(customers, email):
    for i in range(len(customers)):
        if customers[i].get_email() == email:
            return i
    return -1


def find_rental(rentals, rental_id):
    for i in range(len(rentals)):
        if rentals[i].get_rental_id() == rental_id:
            return i
    return -1


def next_gear_id(gear_list):
    highest = 0
    for gear in gear_list:
        if gear.get_gear_id() > highest:
            highest = gear.get_gear_id()
    return highest + 1


def next_pickup_id(points):
    highest = 0
    for point in points:
        if point.get_pickup_id() > highest:
            highest = point.get_pickup_id()
    return highest + 1


def next_rental_id(rentals):
    highest = 0
    for rental in rentals:
        if rental.get_rental_id() > highest:
            highest = rental.get_rental_id()
    return highest + 1

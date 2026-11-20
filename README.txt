PA 5 MIS 221
Tide Tailgate Gear Rental

An application for Tide Tailgate for customers to browse, search, rent and return any gear. Managers can maintain gear, pickup points, customers, and rentals, all while viewing all the reports. Every change will be saved to the text files.


HOW TO RUN

1. Keep all files in the same folder
2. Open the folder in VS Code
3. Run app.py


FILES

app.py - Main menu so run this file
customer_menu.py - Customer sign in and customer menu
manager_menu.py - Manager menu for gear, pickup points, rentals, and customers
reports.py - The five reports
file_handler.py - Reads and writes the text files, selection sort, binary search, sequential search
helpers.py - Input validation and time/cost calculations
gear.py, pickup_point.py, customer.py, rental.py - One class for each record type
gear.txt, pickup_points.txt, customers.txt, rentals.txt - Data files (# delimited)
MIS_Design_doc.docx - A UML for every class and module
flowchart.png - Program flowchart
test_log.txt - A test log


TEST ACCOUNTS

Customer: john@email.com
Inactive customer: sara@email.com
Student customer: alex@crimson.ua.edu
Manager PIN: 0329 (my birthday)


EXTRAS

1. Manager pin: A pin (0329) is required before the Manager Menu and the Reports Menu. After 3 wrong tries the program goes back to the main menu.
2. Overdue fees: A $10.00 overdue fee is added at return when a rental is out longer than the 4hr limit which is shown on the receipt.
3. Student discount: Customers with a @crimson.ua.edu email get 10% off the rental cost, also shown on receipt.
4. Save reports to a text file: After any report, the user can choose to save it to a text file.

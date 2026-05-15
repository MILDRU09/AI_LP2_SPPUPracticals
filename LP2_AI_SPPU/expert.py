# Expert System for Airline Scheduling

# Flight Database
flights = [
    {"flight_no": "AI101", "source": "Mumbai", "destination": "Delhi", "time": "10:00 AM", "seats": 5},
    {"flight_no": "AI202", "source": "Pune", "destination": "Bangalore", "time": "1:00 PM", "seats": 3},
    {"flight_no": "AI303", "source": "Delhi", "destination": "Chennai", "time": "5:00 PM", "seats": 2},
    {"flight_no": "AI404", "source": "Mumbai", "destination": "Bangalore", "time": "8:00 PM", "seats": 4}
]

# Function to display all flights
def display_flights():

    print("\nAll Available Flights:\n")

    for flight in flights:
        print("Flight Number :", flight["flight_no"])
        print("Source         :", flight["source"])
        print("Destination    :", flight["destination"])
        print("Departure Time :", flight["time"])
        print("Available Seats:", flight["seats"])
        print("-----------------------------")


# Function to search flights
def search_flight(source, destination):

    found = False

    print("\nMatching Flights:\n")

    for flight in flights:

        if (flight["source"].lower() == source.lower() and
            flight["destination"].lower() == destination.lower()):

            print("Flight Number :", flight["flight_no"])
            print("Departure Time:", flight["time"])
            print("Available Seats:", flight["seats"])
            print("-----------------------------")

            found = True

    if not found:
        print("No flights available.")


# Function to book seat
def book_ticket(flight_no):

    found = False

    for flight in flights:

        if flight["flight_no"].lower() == flight_no.lower():

            found = True

            if flight["seats"] > 0:
                flight["seats"] -= 1
                print("Ticket Booked Successfully")
                print("Remaining Seats:", flight["seats"])

            else:
                print("No seats available")

    if not found:
        print("Invalid Flight Number")


# Main Program
while True:

    print("\n=== Airline Scheduling Expert System ===")
    print("1. Display All Flights")
    print("2. Search Flight")
    print("3. Book Ticket")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_flights()

    elif choice == 2:
        src = input("Enter Source City: ")
        dest = input("Enter Destination City: ")
        search_flight(src, dest)

    elif choice == 3:
        fno = input("Enter Flight Number: ")
        book_ticket(fno)

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
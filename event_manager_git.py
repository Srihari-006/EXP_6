from datetime import datetime
#This the main class
class Event:
    def __init__(self, event_id, name, date, venue, total_tickets, ticket_price):
        self.event_id = event_id
        self.name = name
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.venue = venue
        self.total_tickets = total_tickets
        self.available_tickets = total_tickets
        self.ticket_price = ticket_price
# This fucn displays details of booking
    def display_details(self):
        print(f"\nEvent ID: {self.event_id}")
        print(f"Event Name: {self.name}")
        print(f"Date: {self.date.strftime('%Y-%m-%d')}")
        print(f"Venue: {self.venue}")
        print(f"Available Tickets: {self.available_tickets}/{self.total_tickets}")
        print(f"Ticket Price: ${self.ticket_price:.2f}")

    def book_tickets(self, quantity):
        if quantity <= self.available_tickets:
            self.available_tickets -= quantity
            return True
        return False

class Booking:
    def __init__(self, booking_id, event_id, customer_name, quantity, total_cost):
        self.booking_id = booking_id
        self.event_id = event_id
        self.customer_name = customer_name
        self.quantity = quantity
        self.total_cost = total_cost
        self.booking_date = datetime.now().date()
    
    def display_details(self):
        print(f"\nBooking ID: {self.booking_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Event ID: {self.event_id}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Cost: ${self.total_cost:.2f}")
        print(f"Booking Date: {self.booking_date.strftime('%Y-%m-%d')}")

class EventManagementSystem:
    def __init__(self):
        self.events = {}
        self.bookings = {}
        self.next_event_id = 1
        self.next_booking_id = 1
    
    def create_event(self, name, date, venue, total_tickets, ticket_price):
        event_id = str(self.next_event_id)
        event = Event(event_id, name, date, venue, total_tickets, ticket_price)
        self.events[event_id] = event
        self.next_event_id += 1
        print(f"\nEvent created successfully with ID: {event_id}")
        return event_id
    
    def display_all_events(self):
        if not self.events:
            print("\nNo events available.")
            return
        
        print("\nAvailable Events:")
        for event in self.events.values():
            event.display_details()
    
    def book_tickets(self, event_id, customer_name, quantity):
        if event_id not in self.events:
            print("\nEvent not found!")
            return None
        
        event = self.events[event_id]
        
        if event.book_tickets(quantity):
            booking_id = str(self.next_booking_id)
            total_cost = quantity * event.ticket_price
            booking = Booking(booking_id, event_id, customer_name, quantity, total_cost)
            self.bookings[booking_id] = booking
            self.next_booking_id += 1
            
            print("\nBooking successful!")
            booking.display_details()
            return booking_id
        else:
            print("\nNot enough tickets available!")
            return None
    
    def display_event_bookings(self, event_id):
        if event_id not in self.events:
            print("\nEvent not found!")
            return
        
        event_bookings = [b for b in self.bookings.values() if b.event_id == event_id]
        
        if not event_bookings:
            print(f"\nNo bookings found for event {event_id}")
            return
        
        print(f"\nBookings for Event {event_id}:")
        for booking in event_bookings:
            booking.display_details()

    def display_all_bookings(self):
        if not self.bookings:
            print("\nNo bookings available.")
            return
        
        print("\nAll Bookings:")
        for booking in self.bookings.values():
            booking.display_details()
# main func
def main():
    system = EventManagementSystem()
    
    while True:
        print("\nEvent Management and Ticket Booking System")
        print("1. Create Event")
        print("2. View All Events")
        print("3. Book Tickets")
        print("4. View Bookings for an Event")
        print("5. View All Bookings")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter event name: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            venue = input("Enter venue: ")
            total_tickets = int(input("Enter total tickets available: "))
            ticket_price = float(input("Enter ticket price: "))
            system.create_event(name, date, venue, total_tickets, ticket_price)
        
        elif choice == "2":
            system.display_all_events()
        
        elif choice == "3":
            event_id = input("Enter event ID: ")
            customer_name = input("Enter your name: ")
            quantity = int(input("Enter number of tickets: "))
            system.book_tickets(event_id, customer_name, quantity)
        
        elif choice == "4":
            event_id = input("Enter event ID: ")
            system.display_event_bookings(event_id)
        
        elif choice == "5":
            system.display_all_bookings()
        
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
# main program
if __name__ == "__main__":
    main()
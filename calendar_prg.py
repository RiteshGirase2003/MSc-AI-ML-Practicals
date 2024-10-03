# calendar module helps in generating and manipulating calendars and dates.
import calendar

def generate_calendar(year, month):
    # Create a TextCalendar instance
    cal = calendar.TextCalendar() #creates a plain-text representation of a calendar.
    
    # Print the month and year
    print(cal.formatmonth(year, month)) # generates a formatted calendar for a specific month and year.

# Main function
def main():
    # Get user input for the year and month
    year = int(input("Enter the year (e.g., 2024): "))
    month = int(input("Enter the month (1-12): "))
    
    # Validate month input
    if month < 1 or month > 12:
        print("Invalid month! Please enter a value between 1 and 12.")
        return

    # Generate and display the calendar
    generate_calendar(year, month)

# Run the program
if __name__ == "__main__":
    main()

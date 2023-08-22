from datetime import datetime

# Function to calculate age
def calculate_age(birth_year, birth_month, birth_day):
    birth_date = datetime(birth_year, birth_month, birth_day)
    current_date = datetime.now()
    age = current_date - birth_date

    years = age.days // 365
    remaining_days = age.days % 365
    months = remaining_days // 30
    days = remaining_days % 30

    return years, months, days

# Main program
print("Welcome to the Age Calculator")
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

if birth_year > datetime.now().year:
    print("Invalid birth year. Please enter a valid year.")
else:
    years, months, days = calculate_age(birth_year, birth_month, birth_day)
    print(f"You are {years} years, {months} months, and {days} days old.")

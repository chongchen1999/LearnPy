# time_conversions.py

from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta

# Example 1: Basic Time Conversions using timedelta
def basic_time_conversions():
    # Creating timedelta instances
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    
    # Adding two timedelta instances
    c = a + b
    
    # Accessing days and seconds
    print(f"Days: {c.days}")  # Output: 2
    print(f"Seconds: {c.seconds}")  # Output: 37800
    print(f"Hours from seconds: {c.seconds / 3600}")  # Output: 10.5
    print(f"Total hours: {c.total_seconds() / 3600}")  # Output: 58.5

# Example 2: Working with datetime and timedelta
def datetime_operations():
    # Creating datetime instances
    a = datetime(2012, 9, 23)
    print(f"10 days after {a} is: {a + timedelta(days=10)}")  # Output: 2012-10-03 00:00:00
    
    b = datetime(2012, 12, 21)
    d = b - a
    print(f"Days between {a} and {b}: {d.days}")  # Output: 89
    
    # Current time
    now = datetime.today()
    print(f"Current time: {now}")
    print(f"10 minutes from now: {now + timedelta(minutes=10)}")

# Example 3: Handling Leap Years
def leap_year_example():
    a = datetime(2012, 3, 1)
    b = datetime(2012, 2, 28)
    print(f"Days between {b} and {a}: {(a - b).days}")  # Output: 2
    
    c = datetime(2013, 3, 1)
    d = datetime(2013, 2, 28)
    print(f"Days between {d} and {c}: {(c - d).days}")  # Output: 1

# Example 4: Using dateutil.relativedelta for Complex Date Manipulations
def complex_date_manipulations():
    a = datetime(2012, 9, 23)
    
    # Adding months using relativedelta
    print(f"1 month after {a} is: {a + relativedelta(months=+1)}")  # Output: 2012-10-23 00:00:00
    print(f"4 months after {a} is: {a + relativedelta(months=+4)}")  # Output: 2013-01-23 00:00:00
    
    # Calculating the difference between two dates using relativedelta
    b = datetime(2012, 12, 21)
    delta = relativedelta(b, a)
    print(f"Difference between {a} and {b}: {delta.months} months and {delta.days} days")  # Output: 2 months and 28 days

# Main function to run all examples
def main():
    print("Basic Time Conversions:")
    basic_time_conversions()
    
    print("\nDatetime Operations:")
    datetime_operations()
    
    print("\nLeap Year Example:")
    leap_year_example()
    
    print("\nComplex Date Manipulations:")
    complex_date_manipulations()

if __name__ == "__main__":
    main()
age = int(input("Enter Your Age:").strip())

months = age * 12
Weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"Your Age {age} in Months is {months}\nand Weeks {Weeks}\nand Days {days:,}\nand hours {hours:,}\nand minutes{minutes:,}\nand seconds{seconds:,}")

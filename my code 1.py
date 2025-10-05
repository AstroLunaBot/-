import random
pin = random.randint(1000,9999)
print("your bassord is: 4 PIN")
PIN = int (input("Enter your 4 digit pin: "))
if len(str(PIN)) > 4 or len(str(PIN)) < 4:
    print("Invalid PIN")
elif PIN == pin:
    print("Wlcome")
else:
    print("Incorrect PIN you PIN is ", pin)

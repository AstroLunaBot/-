color = []
color.append(input("add your favorite color: ").lower())
choose = input("do you want to add more colors? (yes - no): ".lower())
if choose == "yes":
    color.append( input("add your favorite color: ").lower())
    print(f"your favorite colors " + str(color))
elif choose == "no":
    print("your favorite color " + str(color))
else:
    print("invalid choice yes or no sorry bro :D")

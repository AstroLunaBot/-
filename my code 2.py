import random
print("welcome to the coin flip simulator")
print("1. useng random.random()")
print("2. useng random.rendint()")
choice = input("wat need 1 or 2 \n")
if choice == "1":
    cone1 = random.random()
    if cone1 >= 0.5:
        com_test = "heads"
    else:
        com_test = "tails"
elif choice == "2":
    if random.randint(0,1) == 1:
       com_test = "heads"
    else:
       com_test = "tails"
else:
    print('lost to choose 1 or 2')
    exit()
cone = input("press enter to cone Heads or Tails ")
if cone.lower() == com_test.lower():
    print("you win")
else:
    print("you lose")
print(f"the coin is {com_test}")

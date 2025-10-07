Mylist = ["one", "Two", "one", 1, 100.5, True]
Mylist2 = ["a", "b", "c"]
print(Mylist)
print(Mylist[1])
print(Mylist[-1])
print(Mylist[1:4])
print(Mylist[:4])
print(Mylist[1:])
print(Mylist[::1])
print(Mylist[::4])

Mylist[1] = 2
print(Mylist)

Mylist.append("new")
print(Mylist)

Mylist.append(Mylist2)
print(Mylist)
print(Mylist[7][1])

a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)
print(a)

S = [10, 50, 30, 40, 20]
S.sort()
#S.sort(reverse=True)
print(S)

S1 = [10, 50, 30, 40, 20, "A", "B","C"]
S1.reverse()
print(S1)


friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends[0:1])

print(friends[-1])
print(friends[-1::])

print(friends[::2])
print(friends[1::2])

print(friends[1:4])
print(friends[-2:])

friends[-1] = "EXE"
friends[-2] = "EXE2"
friends.append("EXE3")
friends.insert(0, "EXE4")
print(friends)

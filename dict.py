user = {
    "name" : "Alice",
    "age" : 30,
    "city" : "New York"
}
print(user)
print(type(user))
print(user.keys())
print(user.values())

users = {
    "name" : "Bob",
    "age" : 25,
    "city" : "Los Angeles"
}

all_users = {
    "user1" : user,
    "user2" : users,
}

print(all_users)

users = []
for _ in range(int(input())):
    age, name = input().split()
    users.append({"age": int(age), "name": name})

for user in sorted(users, key=lambda x: x["age"]):
    print(user["age"], user["name"])

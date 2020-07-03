ages = {"Alice": 22, "Bob": 27, "shiva": 20}
ages["charlie"] = 30
ages["Alice"] += 1
ages["shiva"] += 5
print(ages)
x = ages["Alice"]
y = ages["Bob"]
z = ages["charlie"]
a = ages["shiva"]
print(f"Alice age is {x}")
print(f"Bob age is {y}")
print(f"charlie age is {z}")
print(f"shiva's age is {a}")
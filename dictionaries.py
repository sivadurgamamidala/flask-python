ages = {"Alice": 22, "Bob": 27}
ages["charlie"] = 30
ages["Alice"] += 1
print(ages)
x = ages["Alice"]
y = ages["Bob"]
z = ages["charlie"]
print(f"Alice age is {x}")
print(f"Bob age is {y}")
print(f"charlie age is {z}")
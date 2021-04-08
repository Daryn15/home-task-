
# task0
data = {"name" : "Daryn", "age" : "28" }
user_on_none = (data
                    if "name" in data and "age" in data
                else None)
print(user_on_none)
print(data["name"])


# task1
a = 8783
b = 6452
sum = a + b
diff = a - b
mult = a * b
print(sum)
print(diff)
print(mult)

# task2
length = 3
volume = int(length ** 3)
s_full = int(6*(length ** 2))
s_side = int(4*(length ** 2))
print(volume)
print(s_full)
print(s_side)


# task3
a = 2
b = 4
c = 8
m = float((a + b + c)/ 3)
n_1 = float((a * b * c) ** (1./3))
n_2 = pow((a * b * c), 1./3)
print(m)
print(n_1)
print(n_2)
import numpy as np

# pole = np.arange(1,10)
# print(pole)

# print(np.flip(pole))

# pole1 = np.array([1, 23, 4, 31 ,1 , 1, 4, 23, 4, 1])
# print(pole1)

# print(np.unique(pole1))

# print(np.max(pole1))


# pole3 = np.arange(2, 14).reshape(3,2,2)
# print(pole3)

# pole4 = np.random.randint(10,30, size=6)
# print(pole4)

#task 5

# pole5 = np.array([23, 45, 112, 150, 43, 254, 95, 8])
# filter_pole5 = pole5 > 100
# nove_pole5 = pole5[filter_pole5]
# print(nove_pole5)


#task 6

pole6 = np.random.random(16).reshape(4,4)
print(f"{pole6}\n")
print(f"V druhom riadku a tretom stlpci sa nachádza {pole6[1,2]}\n")

print(f"Determinant je :{np.linalg.det(pole6)}\n")
print(f"Najmensie cislo je: {pole6.argmin}\nNajvacsie cislo je: {pole6.argmax}")


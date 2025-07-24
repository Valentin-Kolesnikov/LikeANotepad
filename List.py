# нужно сделать цикл, спрашивая каждый раз нужен ли параметр
parameters = int(
    input("Do you need " "1" "-name, " "2" "-name and additional parameter?:")
)
names = []
additionalp = []
total = int(input("How many?:"))
i = 0
a = 1
while i < total:
    name = input("Name:")
    if parameters == 2:
        point = input("Additional info:")
        additionalp.append(point)
    names.append(name)
    i += 1
print("")
print("List:")

if parameters == 1:
    for first in names:
        print(f"{a}) {first}")
        a += 1

elif parameters == 2:
    for first, second in zip(names, additionalp):
        print(f" {a}) {first} - {second}")
        a += 1
parameters = int(
    input("Do you need " "1" "- the main info, " "2" " - the main info and additional info?: ")
)

names = []
additionalp = []
a = 1
stopped = False

while True:
    name = input("Info or stop: ")
    names.append(name)

    if name.lower() in ["stop", "enough", "yes", "-"]:
        names.pop()
        stopped = True
        break

    if parameters == 2 and not stopped:
        point = input("Additional info: ")
        additionalp.append(point)

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
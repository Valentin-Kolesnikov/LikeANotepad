parameters = int(
    input("\nDo you need " "1" "- the main info, " "2" " - the main info and additional info?: ")
)

names = []
additionalp = []
a = 1
stopped = False

while True:
    name = input("\nInfo or stop: ")
    names.append(name)

    if name.lower() in ["stop", "enough", "yes", "-"]:
        names.pop()
        stopped = True
        break

    if parameters == 2 and not stopped:
        point = input("\n-Additional info: ")
        additionalp.append(point)

print("\n------------------------List:------------------------\n")
if parameters == 1:
    for first in names:
        print(f"    {a}) {first}\n")
        a += 1

elif parameters == 2:
    for first, second in zip(names, additionalp):
        print(f"    {a}) {first} -- {second}\n")
        a += 1

print("\n-----------------------------------------------------\n")

input("\nPress Enter to exit...")
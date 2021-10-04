#An empty lis 
items = []


while True:

    n = input("enter anything: ",)
    print(" ",)
    if n == "":
        break

    items.append(n)

print(items,)

print("1.To remove something")
print("2.To insert something")


choice = input("Enter choice(1/2/3/4): ")

if choice not in ("1", "2", "3", "4"):
    print("Wrong choice")


if choice == "1":
    remove = input("Enter what u want to remove: ")
    items.remove(remove)
        

if choice == "2":
    add = input("Enter what u want to add: ")
    print("At any specific Index ")
    pos = input("Y or N")
    if pos != "n":
        index = int(input("Type Index: "))
        items.insert(index, add)

    items.append(add)

print(items)

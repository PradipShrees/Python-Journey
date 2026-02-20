names = []
while True:
    name = (input("Enter your name or type exit to stop -->"))
    if name.lower() == "exit":
        break
    if name:
        names.append(name)
names_sorted = sorted(names)
print(names_sorted)

"""HERE WE GET NEMAES AS INPUT AND SORT IT AND PRINT ONCE AT LAST"""
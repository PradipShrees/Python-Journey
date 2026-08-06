names = []
with open("CustomerNames.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    # for name in sorted(names, reverse = True):
    print(f'Hello,{name}')

with open("Names.txt", "r") as file:
# lines = file.readlines()

    for line in sorted(file):
        print("Hello,",line.rstrip())
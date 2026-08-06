import csv
with open("CustomerData.csv", newline="") as file:
    reader = csv.reader(file)
    for Name, House in reader:
        print(f"{Name} is in {House}")



    """for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")"""
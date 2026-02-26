import csv
name = input("Waht's ypur name?")
home = input("What's your home location ? ")

with open("Salesfile.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"home": home, "name": name})

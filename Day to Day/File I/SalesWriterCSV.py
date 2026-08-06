import csv

name = input("What's your name ? ")
home = input("What's your home location ? ")

with open("Salesfile.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name ,home])

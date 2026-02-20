import csv

workers = []

with open("Workers.csv", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        workers.append({
            "Name": row["Name"],
            "House": row["House"],
            "Vehicle": row["Vehicle"],
            # "Profession": row["Profession"],  # include if you want
        })

for worker in sorted(workers, key=lambda w: w["Name"]):
    print(f"{worker['Name']} is in {worker['House']} and has {worker['Vehicle']}")


"""Now this can handle change """
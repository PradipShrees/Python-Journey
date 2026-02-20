import csv
Workers = []
with open("Workers.csv") as file:
    for line in file:
        Name, House , Vehicle = line.rstrip().split(",")

        worker = {"Names": Name, "House": House, "Vehicles": Vehicle}
        Workers.append(worker)
def get_name(worker):
    return worker["Names"]
for worker in sorted(Workers, key=get_name):
    print(f"{worker['Names']} is in {worker['House']} and has {worker['Vehicles']}")


"""Command + r to replace all at once but recheck
SAME STUFF HAPPENED HERE AS BEN IS SEEN AT LAST DUE
 TO BOM AND TO FIX THIS CODE IN VS CODE.
 
 here the code assumes things and if there is third column then my whole code will
 break like this </usr/local/bin/python3.12 /Users/pradipshrees/Desktop/Python-Journey/Day to Day/File I/WorkerDATA.py 
Traceback (most recent call last):
  File "/Users/pradipshrees/Desktop/Python-Journey/Day to Day/File I/WorkerDATA.py", line 5, in <module>
    Name, House , Vehicle = line.rstrip().split(",")
    ^^^^^^^^^^^^^^^^^^^^^
ValueError: too many values to unpack (expected 3)

Process finished with exit code 1
>

so to defend and make a break-proof code , we are using csv reader with DictReader function
as it lets each row act as a piece if Dictionary
 """
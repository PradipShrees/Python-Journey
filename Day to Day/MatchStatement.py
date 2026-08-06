month = 5
day = 4
match day:
  # match expression(param):
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    # case (possibilities of param)
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

# if there are many caes or possibilities of happening then use match statement
# for better example look paper scissor game in projects

# | MEANS OR STATEMENT
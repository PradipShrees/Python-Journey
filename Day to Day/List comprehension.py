def main():
    yell("This","is","Cs 50")


def yell(*words):
    uppercased = [word.upper() for word in words] # This is list comprehension
    print(*uppercased)

students = ["Ron","sita","Gita"]

gryffindors = [{"name": student, "house": "Gryffindors"} for student in students]


print(gryffindors)


if __name__=="__main__":
    main()
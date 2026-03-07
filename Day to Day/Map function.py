def main():
    yell("This","is","Cs 50")


def yell(*words):
    uppercased = map(str.upper, words) # map = (function, iterable)
    print(*uppercased)


if __name__=="__main__":
    main()
# generators -----> yield helps print data in portion if it is returning back a large output at once 
# this is better for program that returns large value which would consume large cpu if set to return all return data at once

def main():
    n = int(input("What's n ?"))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "⚠️" * 1

if __name__ == "__main__":
    main()
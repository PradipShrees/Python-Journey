def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("Enter A NUMBER:"))

        except ValueError:
            pass
        #pass will not show anything but will transfer process to enter again
main()
#handeling error by adding else statement which fill force to
# give either of one result
#make a infinte loop with While loop to ask user again until you get
#user to type right answer
# return will break and return x to main function


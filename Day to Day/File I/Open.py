while True:
    name = input("Enter your name or exit to stop: ")
    if name.lower() == "exit":
        break
    with open("CustomerNames.txt", "a") as file:
        file.write(f"{name} \n")



#file.close()
""""with we don't have to worry about closing the file"""


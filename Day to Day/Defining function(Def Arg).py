def ask_ok(prompt, retries=4, reminder='Please try again'):
   # This function asks the user to confirm an action by entering 'yes' or 'no'.
   # here the value after = are default values for the parameters, if the user does not provide a value for those parameters when calling the function, the default values will be used.
   # only used when the user does not provide a value for those parameters when calling the function.
   while True:
        reply = input(prompt)
        if reply in ('y', 'ye', 'yes'):
            print("Thanks for your duty!")
            break
        if reply in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries -1
        if retries == 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?', 2, 'come on, only yes or no')

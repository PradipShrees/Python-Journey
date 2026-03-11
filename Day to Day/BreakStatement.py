# Real-life example: ATM PIN attempts (stop after success or 3 failures)

correct_pin = "4321"
attempts = 0

while True:
    pin = input("Enter PIN: ")
    attempts += 1

    if pin == correct_pin:
        print("✅ PIN correct. Access granted.")
        break  # stop the loop because we succeeded

    print("❌ Wrong PIN.")
    if attempts == 3:
        print("🔒 Too many attempts. Card blocked.")
        break  # stop the loop because limit reached
import random

# Real-world-ish example:
# A small "login attempt + security check" loop.
# - continue: skip invalid inputs (empty username/password)
# - pass: placeholder for features not implemented yet (2FA/admin tools)
# - again: ask user if they want to try again

valid_users = {"pradip": "1234", "admin": "adminpass"}

while True:
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    # CONTINUE example: skip bad/empty input and restart loop
    if not username or not password:
        print("⚠️  Missing username or password. Try again.")
        continue

    # Check login
    if username in valid_users and valid_users[username] == password:
        print("✅ Login successful!")

        # PASS example: placeholder for future features
        if username == "admin":
            print("📊 [Admin Dashboard - Coming Soon]")
        else:
            print("👤 [User Profile - Coming Soon]")

        # Simulate 2FA placeholder
        if random.choice([True, False]):
            print("📱 [2FA Code Sent - Coming Soon]")
        print("Logged in (demo).")

    else:
        print("❌ Wrong credentials.")

    # AGAIN control
    again = input("Try again? (y/n): ").strip().lower()
    if again != "y":
        print("Goodbye!")
        break


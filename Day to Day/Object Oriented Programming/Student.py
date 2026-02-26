def main():
    name, house = get_students()
    print(f"{name} from {house}")

def get_students():
    name = input("Name: ").strip()
    house = input("House: ").strip()
    return name, house


if __name__ == "__main__":
# Only run this code when this file is executed directly (python file.py).
# If the file is imported (import file), this block will NOT run.
# This lets the file be both a reusable module and a runnable script entry point.
    main()
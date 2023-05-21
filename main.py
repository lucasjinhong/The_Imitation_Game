from Controller.Controller import Controller

def print_menu():
    print()
    print("1. Level1 ")
    print("2. Level2 ")
    print("3. Level3 ")
    print("or 'exit' to leave ")
    print()

    level = input("Please select the level(number): ")

    return level

def main():
    while True:
        level = print_menu()

        if level == "exit":
            break
        else:
            Controller(level).execute()

if __name__ == '__main__':
    main()
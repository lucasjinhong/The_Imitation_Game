from Controller.Substitution import Substitution
from Controller.Atbash import Atbash
from Controller.Caesar import Caesar
from Controller.Xor import Xor
from Text.Random import Random

method = {
    "0": Substitution,
    "1": Atbash,
    "2": Caesar,
    "3": Xor
}

def print_menu():
    print()
    print("0. Substitution ")
    print("1. Atbash ")
    print("2. Caesar ")
    print("3. Xor ")
    print("or 'exit' to leave ")
    print()
    choose = input("Please select the encoding to use(number): ")

    return choose

def main():
    rand = Random()
    word = rand.random_word()

    while True:
        choose = print_menu()

        if choose == "exit":
            break
        else:
            try:
                method[choose]().execute(word)
            except:
                pass

if __name__ == '__main__':
    main()
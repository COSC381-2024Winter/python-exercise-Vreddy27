def show_menu():
    print("Menu:")
    print("Enter q to Quit")

def main():
    while True:
        show_menu()
        choice = input("Choose from the following menu options: ").strip().lower()

        if choice == 'q':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

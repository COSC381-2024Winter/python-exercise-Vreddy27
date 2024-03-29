from movies import Movies

def show_menu():
    print("Menu:")
    print("Enter list to list all movies")
    print("Enter q to Quit")

def list_all_movies(movies):
    print("Movie list:")
    movie_names = movies.list_movie_names()
    for idx, movie_name in enumerate(movie_names, start=1):
        print(f"{idx}. {movie_name}")

def main():
    movies = Movies('./movies.txt') 

    while True:
        show_menu()
        choice = input("Choose from the following menu options: ").strip().lower()

        if choice == 'q':
            print("Exiting program.")
            break
        elif choice == 'list':
            list_all_movies(movies)
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

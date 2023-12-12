from movies import Movies

movies = Movies('./movies.txt')

def display_menu():
    print("===== Movie Database Menu =====")
    print("1. View all movies")
    print("2. Search for a movie")
    print("3. Add a new movie")
    print("q. Quit")
    print("===============================")

def main():
    while True:
        display_menu()
        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            # Add code to view all movies
            movies.display_all_movies()
        elif user_choice == '2':
            # Add code to search for a movie
            search_term = input("Enter the movie title to search: ")
            movies.search_movie(search_term)
        elif user_choice == '3':
            # Add code to add a new movie
            title = input("Enter the movie title: ")
            genre = input("Enter the movie genre: ")
            year = input("Enter the release year: ")
            movies.add_movie(title, genre, year)
        elif user_choice.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


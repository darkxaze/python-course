MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def enter_movie_details():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def listing_movies():
    print("\nList of movies:")
    movie_list = [
        f"Title: {m['title']}, Director: {m['director']}, Year: {m['year']}"
        for m in movies
    ]
    print("\n".join(movie_list))


def finding_movies():
    record = input("Enter the movie title to search: ").lower()

    match = {
        m["title"]: {"director": m["director"], "year": m["year"]}
        for m in movies
        if m["title"].lower() == record
    }

    if match:
        print("\nFound movie:")
        print(match)
    else:
        print("Movie not found.")


# Main loop
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        enter_movie_details()
    elif selection == "l":
        listing_movies()
    elif selection == "f":
        finding_movies()
    else:
        print("Unknown command. Please try again.")
    
    selection = input(MENU_PROMPT)

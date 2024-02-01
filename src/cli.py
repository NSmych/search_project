from spotify_requests import search_tracks, search_albums, search_artists, search_genres

welcome = True


def cli():
    global welcome
    if welcome:
        print("Welcome to the Spotify Data Analyzer!")
    print("What would you like to search for?")
    print("1: Tracks\n2: Albums\n3: Artists\n4: Genres")

    options = {"1": search_tracks, "2": search_albums, "3": search_artists, "4": search_genres}
    choice = input("Enter the number of your choice: ")
    try:
        if choice.isnumeric() and 0 < int(choice) <= len(options):
            options[choice]()
        else:
            raise ValueError("Invalid choice")
    except ValueError as e:
        print(e)
        welcome = not welcome
        cli()

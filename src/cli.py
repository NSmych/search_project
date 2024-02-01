from spotify_requests import search_for

welcome = True
options = {
    "1": "artist",
    "2": "track",
    "3": "album",
    "4": "playlist"
}


def cli():
    global welcome
    if welcome:
        print("Welcome to the Spotify Data Analyzer!")
    print("What would you like to search for?")
    print(
        f"1: {options['1'].capitalize()}\n2: {options['2'].capitalize()}\n3: {options['3'].capitalize()}\n4: {options['4'].capitalize()}")

    choice = input("Enter the number of your choice: ")
    if choice.isnumeric() and 0 < int(choice) <= len(options):
        chosen_type = options[choice]
        search_for(chosen_type)
    else:
        print("Invalid choice")
        welcome = not welcome
        cli()


def inner_search(search_object):
    result = input(f"Enter name of the {search_object}: ")
    return result

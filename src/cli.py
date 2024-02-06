from spotify_requests import search_for

WELCOME = True
OPTIONS = {
    "1": "artist",
    "2": "track",
    "3": "album",
    "4": "playlist"
}


def cli():
    global WELCOME
    while True:
        if WELCOME:
            print("Welcome to the Spotify Data Analyzer!")
            WELCOME = False

        print("What would you like to search for?")
        print(f"1: {OPTIONS['1'].capitalize()}\n2: {OPTIONS['2'].capitalize()}\n3: {OPTIONS['3'].capitalize()}\n4: {OPTIONS['4'].capitalize()}\n")

        choice = input("Enter the number of your choice: ")
        if choice.isnumeric() and 0 < int(choice) <= len(OPTIONS):
            chosen_type = OPTIONS[choice]
            search_for(chosen_type)
            break
        else:
            print("Invalid choice\n")


def inner_search(search_object):
    result = input(f"Enter name of the {search_object}: ")
    return result

# Music Library Management Program

def add_album(library, album_info):
    artist, title, year, songs = album_info
    library[title] = (artist, year, songs)
    return library

def create_playlist(library, selections):
    playlist = []
    for album_title, song in selections:
        if album_title in library and song in library[album_title][2]:
            playlist.append(song)
    return playlist

def add_song_to_album(library, album_title, new_song):
    if album_title in library:
        artist, year, songs = library[album_title]
        if new_song not in songs:
            songs.append(new_song)
        library[album_title] = (artist, year, songs)
    return library

def remove_song_from_playlist(playlist, song):
    if song in playlist:
        playlist.remove(song)
    return playlist

def display_library(library):
    for title, (artist, year, songs) in library.items():
        print(f"Album: {title}, Artist: {artist}, Year: {year}, Songs: {songs}")

def display_playlist(playlist):
    print("Playlist:", playlist)

# Main program loop
library = {}
playlist = []

while True:
    print("\n--- Music Library Menu ---")
    print("1. Add a new album")
    print("2. Create a playlist")
    print("3. Add song to album")
    print("4. Remove song from playlist")
    print("5. Display library")
    print("6. Display playlist")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        artist = input("Enter artist name: ")
        title = input("Enter album title: ")
        year = int(input("Enter release year: "))
        songs = input("Enter song titles separated by commas: ").split(",")
        album_info = (artist, title, year, [song.strip() for song in songs])
        library = add_album(library, album_info)

    elif choice == "2":
        selections = []
        n = int(input("How many songs do you want to add to the playlist? "))
        for _ in range(n):
            album = input("Enter album title: ")
            song = input("Enter song title: ")
            selections.append((album, song))
        playlist = create_playlist(library, selections)

    elif choice == "3":
        title = input("Enter album title: ")
        new_song = input("Enter song to add: ")
        library = add_song_to_album(library, title, new_song)

    elif choice == "4":
        song = input("Enter song to remove from playlist: ")
        playlist = remove_song_from_playlist(playlist, song)

    elif choice == "5":
        display_library(library)

    elif choice == "6":
        display_playlist(playlist)

    elif choice == "7":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

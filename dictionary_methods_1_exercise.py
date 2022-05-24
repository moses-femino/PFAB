songs = {"Queen": "Bohemian Rhapsody", 
         "Bee Gees": "Stayin' Alive", 
         "U2": "One", 
         "Michael Jackson": "Billie Jean", 
         "The Beatles": "Hey Jude", 
         "Bob Dylan": "Like A Rolling Stone"}

print(len(songs))

for key in songs.keys():
    print(key)

print(songs.values())

for key, value in songs.items():
    print(key, value)

print(songs.get("Promise of the Real", "Not a key in this dictionary"))

# Amazon | OA 2019 | Favorite Genres

Given a map `Map<String, List<String>> userSongs` with user names as keys and a list of all the songs that the user has listened to as values.



Also given a map `Map<String, List<String>> songGenres`, with song genre as keys and a list of all the songs within that genre as values. The song can only belong to only one genre.



The task is to return a map `Map<String, List<String>>`, where the key is a user name and the value is a list of the user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one favorite genre if he/she has listened to the same number of songs per each of the genres.



**Example 1:**



```
Input:
userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
},
songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

Output: {  
   "David": ["Rock", "Techno"],
   "Emma":  ["Pop"]
}

Explanation:
David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.
```



**Example 2:**



```
Input:
userSongs = {  
   "David": ["song1", "song2"],
   "Emma":  ["song3", "song4"]
},
songGenres = {}

Output: {  
   "David": [],
   "Emma":  []
}
```



## Code

```python
def favoritegenre(userSongs, songGenres):
    song_genre = {}
    # user_genre = {}
    res = {}
    for genre in songGenres.keys():
        for song in songGenres[genre]:
            song_genre[song] = genre

    for user in userSongs.keys():
        res[user] = []
        user_genre = {}
        for song in userSongs[user]:
            if song in song_genre:
                user_genre[song_genre[song]] = user_genre.get(song_genre[song], 0) + 1
        if user_genre:
            max_times = max(val for val in user_genre.values())
            for genre in user_genre.keys():
                if user_genre[genre] == max_times:
                    res[user].append(genre)
    return res

userSongs = {
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}
songGenres = {}
# {
#    "Rock":    ["song1", "song3"],
#    "Dubstep": ["song7"],
#    "Techno":  ["song2", "song4"],
#    "Pop":     ["song5", "song6"],
#    "Jazz":    ["song8", "song9"]
# }

print(favoritegenre(userSongs, songGenres))
```


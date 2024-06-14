import random
import string

user_count = 100
playlist_count_range = (1, 5)
music_count_range = (10, 20)
share_count_range = (1, 10)
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack",
         "Karen", "Leo", "Mia", "Nina", "Oscar", "Paul", "Quincy", "Rita", "Sam", "Tina",
         "Uma", "Victor", "Wendy", "Xander", "Yara", "Zane", "Aaron", "Bella", "Chris", "Diana",
         "Ethan", "Fiona", "George", "Hazel", "Ian", "Jade", "Kyle", "Luna", "Mason", "Nora",
         "Owen", "Piper", "Quinn", "Ruby", "Sean", "Tara", "Ursula", "Vincent", "Willow", "Xavier",
         "Yasmine", "Zach", "Adam", "Brenda", "Carl", "Daisy", "Edward", "Faith", "Gavin", "Holly",
         "Isaac", "Jenna", "Kevin", "Laura", "Mark", "Nadia", "Olivia", "Peter", "Queenie", "Ryan",
         "Sophia", "Thomas", "Una", "Violet", "Wesley", "Xia", "Yosef", "Zoe", "Arthur", "Beth",
         "Connor", "Dylan", "Elena", "Felix", "Gabby", "Henry", "Isla", "Jake", "Kara", "Liam"]

# Helper function to generate random strings
def random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

output = []

# Store user IDs to ensure they are referenced correctly
user_ids = []

# User Data
for i in range(1, user_count + 1):
    name = names[i % len(names)]
    user_id = f"user_{random_string(6)}"
    user_ids.append(user_id)
    output.append(f"INSERT OR IGNORE INTO User (id, password, username) VALUES ('{user_id}', 'password{i}', '{name}');")

# Playlist Data
playlist_data = []
for user_id in user_ids:
    for j in range(random.randint(*playlist_count_range)):
        playlist_name = f"Playlist_{random_string(6)}"
        img_name = f"img_{random_string(6)}.jpg"
        playlist_data.append((user_id, playlist_name))
        output.append(f"INSERT OR IGNORE INTO Playlist (id, name, img) VALUES ('{user_id}', '{playlist_name}', '{img_name}');")

# Music Data
for user_id, playlist_name in playlist_data:
    for k in range(random.randint(*music_count_range)):
        song_title = f"Song_{random_string(6)}"
        artist_name = f"Artist_{random_string(6)}"
        song_url = f"url_{random_string(6)}.mp3"
        output.append(f"INSERT OR IGNORE INTO Music (plid, title, artist, url) VALUES ((SELECT plid FROM Playlist WHERE id='{user_id}' AND name='{playlist_name}'), '{song_title}', '{artist_name}', '{song_url}');")

# Share Data
for user_id in user_ids:
    shared_users = random.sample(user_ids, random.randint(*share_count_range))
    for share_user_id in shared_users:
        if share_user_id != user_id:  # Avoid sharing with self
            output.append(f"INSERT OR IGNORE INTO Share (id, shareid) VALUES ('{user_id}', '{share_user_id}');")

# Write to file
with open("output.txt", "w") as file:
    file.write("\n".join(output))

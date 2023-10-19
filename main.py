import json
import sys

class UserNotFound(Exception):
    pass

class SongNotFound(Exception):
    pass

class PlaylistNotFound(Exception):
    pass

def read_json(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def write_json(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def add_song_to_playlist(data, song_id, playlist_id):
    for playlist in data['playlists']:
        if playlist['id'] == playlist_id:
            playlist['song_ids'].append(song_id)
            return
    raise PlaylistNotFound(f"Playlist with ID {playlist_id} not found.")

def add_playlist_for_user(data, user_id, existing_song_id):
    user = next((u for u in data['users'] if u['id'] == user_id), None)
    if user:
        existing_song = next((s for s in data['songs'] if s['id'] == existing_song_id), None)
        if existing_song:
            new_playlist_id = str(len(data['playlists']) + 1)
            new_playlist = {
                "id": new_playlist_id,
                "owner_id": user_id,
                "song_ids": [existing_song_id]
            }
            data['playlists'].append(new_playlist)
            return
        else:
            raise SongNotFound(f"Song with ID {existing_song_id} not found.")
    else:
        raise UserNotFound(f"User with ID {user_id} not found.")

def remove_playlist(data, playlist_id):
    found = False
    for playlist in data['playlists']:
        if playlist['id'] == playlist_id:
            data['playlists'].remove(playlist)
            found = True
            break
    if not found:
        raise PlaylistNotFound(f"Playlist with ID {playlist_id} not found.")

if __name__ == '__main__':
    input_file = sys.argv[1]
    changes_file = sys.argv[2]
    output_file = sys.argv[3]

    spotify_data = read_json(input_file)
    changes_data = read_json(changes_file)

    for change in changes_data:
        if change['type'] == 'add_song_to_playlist':
            add_song_to_playlist(spotify_data, change['song_id'], change['playlist_id'])
        elif change['type'] == 'add_playlist_for_user':
            add_playlist_for_user(spotify_data, change['user_id'], change['existing_song_id'])
        elif change['type'] == 'remove_playlist':
            remove_playlist(spotify_data, change['playlist_id'])

    write_json(spotify_data, output_file)
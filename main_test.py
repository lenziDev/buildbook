import subprocess

def test_command_line_interface():
    command_string = "python main.py spotify.json changes.json output.json"
    result = subprocess.run(command_string, shell=True, text=True, capture_output=True)

    assert result.returncode == 0

def test_command_line_user_error_interface():
    command_string = "python main.py spotify.json changes_user_none.json output_user.json"
    result = subprocess.run(command_string, shell=True, text=True, capture_output=True)

    assert result.returncode == 1

def test_command_line_playlist_error_interface():
    command_string = "python main.py spotify.json changes_playlist_none.json output_playlist.json"
    result = subprocess.run(command_string, shell=True, text=True, capture_output=True)

    assert result.returncode == 1

def test_command_line_song_error_interface():
    command_string = "python main.py spotify.json changes_song_none.json output_song.json"
    result = subprocess.run(command_string, shell=True, text=True, capture_output=True)

    assert result.returncode == 1
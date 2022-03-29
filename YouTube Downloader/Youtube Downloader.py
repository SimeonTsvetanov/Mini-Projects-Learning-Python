from pytube import YouTube
from pytube import Playlist


def download_playlist(url: str, type_stream: str):
    playlist = Playlist(url)
    for song in playlist:
        if type_stream == "a":
            yt = YouTube(song).streams.get_audio_only()
            if yt:
                yt.download(output_path=playlist.title)
        elif type_stream == "v":
            yt = YouTube(song).streams.get_highest_resolution()
            if yt:
                yt.download(output_path=playlist.title)
    return


def download_song(url: str, type_stream: str):
    song = YouTube(url)
    if song:
        if type_stream == "a":
            song.streams.get_audio_only().download()
        elif type_stream == "v":
            song.streams.get_highest_resolution().download()
    return


def validate(url, p_or_s, a_or_v):
    valied_url = False
    valid_p_or_s = False
    valid_a_or_v = False

    try:
        YouTube(url)
        valied_url = True
    except Exception:
        pass
    if (p_or_s == "p") or (p_or_s == "s"):
        valid_p_or_s = True
    if (a_or_v == "a") or (a_or_v == "v"):
        valid_a_or_v = True

    if valied_url and valid_p_or_s and valid_a_or_v:
        return True
    else:
        return False


def run():
    playlist_or_song = input("Type  p  for Playlist or  s  for ONE Song Only and hit ENTER:\n").lower()
    song_or_video = input("Type  a  for AUDIO onli or type  v  for Video\n").lower()
    url_to_download = input("Place the link here:\n")
    if not validate(url=url_to_download, p_or_s=playlist_or_song, a_or_v=song_or_video):
        print("Invalid Input")
        print()
        run()
    if playlist_or_song == "p":
        download_playlist(url=url_to_download, type_stream=song_or_video)
    elif playlist_or_song == "s":
        download_song(url=url_to_download, type_stream=song_or_video)
    print("Download Compleate!")
    print()
    run()


if __name__ == '__main__':
    run()

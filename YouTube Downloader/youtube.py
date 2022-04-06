# pyinstaller installation command: pyinstaller --onefile -w --icon=youtube.ico youtube.py

# Importing the libraries needed for the project
import PySimpleGUI as pg
from pytube import YouTube
from pytube import Playlist


class App:
    def __init__(self):
        self.name = "YouTube Downloader"
        self.theme = pg.theme("Reds")
        self.window = pg.Window(self.name, self.layout())

    @staticmethod
    def layout():
        """
        The Layout create is using normal list MATRIX: [[], [], []].
        Just take a look at the code below it is pretty simple.
        """
        output = [
            [pg.Text("", text_color="white", font=("Helvetica", 12), key="label")],
            [pg.Text("Select Playlist or Song:")],
            [pg.Radio("Song", 'playlist_or_song', default=True, size=(10, 1)),
             pg.Radio("Playlist", 'playlist_or_song', size=(10, 1))],
            [pg.Text("Select the format you want to Download:")],
            [pg.Radio("Audio", 'audio_or_video', default=True, size=(10, 1)),
             pg.Radio("Video", 'audio_or_video', size=(10, 1))],
            [pg.Text("Past the YouTube link here:")],
            [pg.InputText(do_not_clear=False)],
            [pg.Button('Download', button_color="red"), pg.Button('Cancel')]
                 ]
        return output

    @staticmethod
    def validate_url(url):
        try:
            YouTube(url)
            return True
        except Exception:
            return False

    def download(self, song, playlist, audio, video, link):
        """
        bool :param song: True if we wish to download just a song, else False
        bool :param playlist: True if we wish to download the whole Playlist, else False
        bool :param audio: True if we wish to download in MP3 format, else False
        bool :param video: True if we wish to download in MP4 format, else False
        str(URL) :param link: the link from YouTube we wish to download
        :return: The program will Download the selected song/playlist in the selected format
        """
        if song:
            s = YouTube(link)  # Create the Youtube Object
            if audio:
                s.streams.get_audio_only().download()  # Get the best audio quality and download it.
            elif video:
                s.streams.get_highest_resolution().download()  # Get the best video quality and download it.
        elif playlist:
            p = Playlist(link)  # Create the Youtube Playlist Object
            # Now let's iterate through the playlist
            for s in p:
                # Check for the wated format:
                if audio:
                    yt = YouTube(s).streams.get_audio_only()  # Filter the playlist to audio mp3 only
                    if yt:
                        yt.download(output_path=p.title)  # And download it.
                elif video:
                    yt = YouTube(s).streams.get_highest_resolution()  # Filter the playlist to video mp4 only
                    if yt:
                        yt.download(output_path=p.title)  # And download it.
        return self.window['label'].update("Downloaded!")

    def start(self):
        # Create an event loop to run the program:
        while True:
            # Fetch the input data
            event, data = self.window.read()

            # Check if the user would like to stop the program:
            if event in (pg.WIN_CLOSED, 'Cancel'):
                break  # If so kill it!

            # Check if the button Download is clicked!
            elif event == "Download":
                "Update the LABEL if any information was there from before"
                self.window['label'].update("")

                # get all the data on the screen:
                s, p, a, v, li = data[0], data[1], data[2], data[3], data[4]

                # Check if the URL is valid and if so DOWNLOAD whatever is wanted!
                if self.validate_url(li):
                    self.download(song=s, playlist=p, audio=a, video=v, link=li)
                # If the link is invalid just update the LABEL
                else:
                    self.window['label'].update("Invalid or Private Link, Try again:")

        # Close the window
        self.window.close()


def run():
    # Create the Application and Run it!
    app = App()
    app.start()


if __name__ == '__main__':
    run()

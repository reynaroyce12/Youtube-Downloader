from pytube import YouTube


class Download:
    def __init__(self, file_url, save_path):
        self.file_url = file_url
        self.save_path = save_path
        self.yt = YouTube(self.file_url)
        self.video_title = self.yt.title
        self.video = self.yt.streams.filter(res="720p").first()

    def download_file(self):
        self.video.download(self.save_path, self.video_title + '.mp4')

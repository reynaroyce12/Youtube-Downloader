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
        print(f"{self.yt.title} Downloaded")




# yt_link = 'https://youtu.be/ZGmpyiFcQ7M?list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbAVMZGmpyiFcQ7M'
# save_path = r"C:\Users\REYNA ROYCE\Desktop"
# yt = YouTube(yt_link)
# video = yt.streams.filter(res="720p").first()
# video.download(save_path, f'{yt.title}'+'.mp4')
# print(f"{yt.title} Downloaded")

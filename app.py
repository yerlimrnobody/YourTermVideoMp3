import sys
import os
import time
import pytubefix
import pyfiglet
from moviepy.editor import AudioFileClip


def progress_end():
    print(" ")
    print("DOWNLOAD COMPLETED...")
    time.sleep(3)

file_size = 0
def progress_function(stream, chunk, bytes_remaining):
    global file_size
    current = ((file_size - bytes_remaining) / file_size)
    percent = ('{0:.1f}').format(current * 100)
    progress = int(50 * current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()

def video_download():
    url_video = input("Please Enter The Url Of YouTube Video : ")
    print("Path Example For Mac/Linux Users : /home/YourUsername/Download")
    path = input("Please Enter Path To Download : ")
    video_title = pytubefix.YouTube(url_video)
    print(video_title.title)
    yt = pytubefix.YouTube(url_video)

    yt.register_on_progress_callback(progress_function)

    stream = yt.streams.get_highest_resolution()

    global file_size
    file_size = stream.filesize
    print(f"Please Wait Up to {round(file_size /(1024*1024),2)} MB Downloading...")
    print("You Will Turn Back To Main Menu When Download Completed.")
    stream.download(path)
    progress_end()
    os.system("clear")



def audio_download():
    url_audio = input("Please Enter The Url Of Youtube Video : ")
    print("Path Example For Mac/Linux Users : /home/yourusername/Desktop")
    path = input("Please Enter The Path You Want To Download : ")
    video_title = pytubefix.YouTube(url_audio)
    print(video_title.title)
    pytubefix.YouTube(url_audio).streams.get_audio_only().download(path)


def mp4tomp3convert(name):

    audio = AudioFileClip(name + ".mp4")
    audio.write_audiofile(name + ".mp3")


def list_files_in_directory(directory):
    try:
        # Klasördeki dosyaları listele
        files = os.listdir(directory)
        if not files:
            print("Klasörde dosya bulunamadı.")
            return None

        # Dosyaları numaralandırarak ekrana yazdır
        print("Klasördeki dosyalar:")
        for idx in range(len(files)):
            print(f"{idx + 1}. {files[idx]}")

        return files
    except FileNotFoundError:
        print("Geçersiz klasör yolu.")
        return None

def select_file(files):
    while True:
        try:
            # Kullanıcıdan dosya numarası girmesini iste
            file_index = int(input("Seçmek istediğiniz dosyanın numarasını girin: ")) - 1
            if 0 <= file_index < len(files):
                return files[file_index]
            else:
                print("Geçersiz numara. Lütfen tekrar deneyin.")
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")


#ASCII ART
figlet_text = "YOU TERM VIDEO MP3"
figlet_text_2 = "DOWNLOADER"
figlet_art = pyfiglet.figlet_format(figlet_text, font="bubble")
figlet_art_2 = pyfiglet.figlet_format(figlet_text_2)
print(figlet_art)
print(figlet_art_2)


while True:
    # MENU FOR USER
    print("""
    Terminal Youtube Video And Mp3 Downloader

    1. Video Downloader
    2. Audio Downloader
    3. Convert MP4 Audio To MP3 Audio
    Q. Quit
    """)

    user_input = input("Choose 1, 2, 3 or Q for Exit : ")

    if user_input == "1":
        print("1")
        video_download()

    elif user_input == "2":
        print("2")
        audio_download()

    elif user_input == "3":
        directory = input("Lütfen Dosya Yolunu Giriniz : ")
        files = list_files_in_directory(directory)
        selected_file = select_file(files)
        print(selected_file[:-4])
        #break
        mp4tomp3convert(selected_file[:-4])



    elif user_input == "q" or user_input == "Q":
        print("Quitting...")
        break

    else:
        print("Please choose 1, 2, 3 or Q")

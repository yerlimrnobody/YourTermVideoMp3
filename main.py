#import os
#os.system("apt-get install figlet") #NEED SUPER USER PERMISION THIS IS NOT WORKING
#os.system("clear")
#os.system("figlet YouTermVideoMp3")

#STANDART LIBRARIES THAT WE WILL USE TO INSTALL REQUIRED LIBRARIES

import subprocess
import sys
import os

#import pyfiglet
#import pytube
#import moviepy

#Yüklenmesi Gereken Paketleri Kontrol Edip Yükleyelim

try:
    import pyfiglet
    print("pyfiglet Library is Allready Installed")
    import pytube
    print("pytube Library is Allready Installed")
    from moviepy.editor import AudioFileClip
    print("moviepy.editor Library is Allready Installed")

except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyfiglet"])
    print("pyfiglet Installed")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytube"])
    print("pyfiglet Installed")
    subprocess.check_call([sys.executable,"-m", "pip", "install", "moviepy"])

finally:
    os.system("clear")


def video_download():
    url_video = input("Please Enter The Url Of Youtube Video : ")
    print("Path Example For Mac/Linux Users : /home/yourusername/Download")
    path = input("Please Enter The Path You Want To Download : ")
    video_title = pytube.YouTube(url_video)
    print(video_title.title)
    pytube.YouTube(url_video).streams.get_highest_resolution().download(path)

def audio_download():
    url_audio = input("Please Enter The Url Of Youtube Video : ")
    print("Path Example For Mac/Linux Users : /home/yourusername/Desktop")
    path = input("Please Enter The Path You Want To Download : ")
    video_title = pytube.YouTube(url_audio)
    print(video_title.title)
    pytube.YouTube(url_audio).streams.get_audio_only().download(path)

def mp4_converter():
    print(os.system("ls"))


#ASCII ART ---- ARTISTIK YAZI YAZAN
figlet_text = "YOUR TERM VIDEO MP3"
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
    4. Quit
    """)

    user_input = input("Choose 1, 2 or Q for Exit : ")

    if user_input == "1":
        print("1")
        video_download()

    elif user_input == "2":
        print("2")
        audio_download()

    elif user_input == "3":
        print("3")
        mp4_converter()

    elif user_input == "q" or user_input == "Q":
        print("Quitting...")
        break

    else:
        print("Please choose 1, 2, 3 or Q")
import yt_dlp
import os
import pyfiglet

#ASCII ART
figlet_text = "YOU TERM VIDEO MP3"
figlet_text_2 = "DOWNLOADER"
figlet_art = pyfiglet.figlet_format(figlet_text, font="bubble")
figlet_art_2 = pyfiglet.figlet_format(figlet_text_2)
print(figlet_art)
print(figlet_art_2)


def download_video(url):

    youtube_standart = {
        '144p': '256x144',
        '240p': '426x240',
        '360p': '640x360',
        '480p': '854x480',
        '720p': '1280x720',
        '1080p': '1920x1080',
        '1440p': '2560x1440',
        '2160p': '3840x2160'
    }

    ydl_opts_info = {
    'quiet': True,
    'no_warnings': True
    }

    ydl_obj = yt_dlp.YoutubeDL(ydl_opts_info)

    infos = ydl_obj.extract_info(url=url, download=False)

    resolutions = set()

    for format in infos['formats']:
        if format.get('resolution') != 'audio only':
            standart_resolution = f"{format.get('width')}x{format.get('height')}"
            if standart_resolution in youtube_standart.values():
                for quality, res in youtube_standart.items():
                    if res == standart_resolution and res != None:
                        resolutions.add(quality)

    resolutions = sorted(resolutions, key=lambda r: (int(r[:-1]), 'p' in r))

    for index, r in enumerate(resolutions, start=1):
        print(f"{index}. for {r}")

    while True:
        try:
            choice = int(input("Please Choose a Resolution : "))
            if 1<= choice <=len(resolutions):
                break
            else:
                print("Invalid Choice. Please Enter a Number Between 1 and", len(resolutions))

        except ValueError:
            print("Invalid Input. Please Enter an Integer.")
                        

    for index, r in enumerate(resolutions, start=1):
        if index == choice:
            print(r)

    ydl_opts_video = {
        'format': None,
        'paths' : {
            'home' : os.path.join('.', 'Downloads')
        },
        'merge_output_format' : 'mp4',
        'writethumbnail': True,
        'embed_thumbnail': True,
    }

    chosen_resolution = resolutions[choice-1]
    height = chosen_resolution[:-1]
    ydl_opts_video['format'] = f'bestvideo[height={height}]+bestaudio/best'


    ydl_video = yt_dlp.YoutubeDL(ydl_opts_video)
    ydl_video.download([url])
    


def download_audio(url):

    ydl_opts_audio = {
        'format' : 'bestaudio/best',
        'paths' : {
            'home' : os.path.join('.','Downloads')
        },
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192'
        },
        {
            'key': 'EmbedThumbnail'
        }],

        'writethumbnail': True,
        'embed_thumbnail': True,

    }

    ydl_audio = yt_dlp.YoutubeDL(ydl_opts_audio)
    ydl_audio.download([url])


while True:
    # MENU FOR USER
    print("""
    Terminal Youtube Video And Mp3 Downloader

    1. Video Downloader
    2. Audio Downloader
    Q. Quit
    """)

    user_input = input("Choose 1, 2 or Q for Exit : ")

    if user_input == "1":
        
        video_url = input('Please Enter The URL of Youtube Video : ')
        download_video(video_url)

        os.system("clear")
        download_path = os.getcwd() + '/Downloads'
        print(f'\nFile Successfuly Downloaded To {download_path}')

        figlet_text = "YOU TERM VIDEO MP3"
        figlet_text_2 = "DOWNLOADER"
        figlet_art = pyfiglet.figlet_format(figlet_text, font="bubble")
        figlet_art_2 = pyfiglet.figlet_format(figlet_text_2)
        print(figlet_art)
        print(figlet_art_2)
        

    elif user_input == "2":
        
        audio_url = input('Please Enter The URL of Youtube Video : ')
        download_audio(audio_url)

        os.system("clear")

        download_path = os.getcwd() + '/Downloads'
        print(f'\nFile Successfuly Downloaded To {download_path}')

        figlet_text = "YOU TERM VIDEO MP3"
        figlet_text_2 = "DOWNLOADER"
        figlet_art = pyfiglet.figlet_format(figlet_text, font="bubble")
        figlet_art_2 = pyfiglet.figlet_format(figlet_text_2)
        print(figlet_art)
        print(figlet_art_2)
        

    elif user_input == "q" or user_input == "Q":
        print("Quitting...")
        break

    else:
        print("Please choose 1, 2 or Q")




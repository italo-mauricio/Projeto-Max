from pytube import YouTube
import moviepy.editor as mp
import re 
import os

def download():
    os.system("cls")
    print('''
    |================================================================== |
    |                   Welcome to MP3 Converter!                       |
    |                                                                   |
    | ----------------------------------------------------------------- |
    | Step 1: The converter requires a youtube link with the video you  |
    | just want to extract the audio                                    |
    |                                                                   |
    | Step 2: Then choose the directory to deposit the file             |
    |                                                                   |
    | ================================================================= |
          
    ''')
    
    link = input("Enter the link of the video you want to extract the audio: ")
    path = input("Choose directory: ")
    yt = YouTube(link)

    print("Downloading...")
    ys = yt.streams.filter(only_audio=True).first().download(path)
    print("Download Successfully!")

    print("Converting file..")
    print("Wait...")

    for file in os.listdir(path):
        if re.search('mp4', file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
            
    print("Complete!")
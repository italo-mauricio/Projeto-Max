from pytube import YouTube
import moviepy.editor as mp
import re 
import os

def download():
    print('''
    |==================================================================|
    |                   Welcome to MP3 Converter!    
          
          
          
          
          ''')
    link = input("Digite o link do vídeo que você quer baixar: ")
    path = input("Digite o diretório que deseja salvar o vídeo: ")
    yt = YouTube(link)

    print("Baixando...")
    ys = yt.streams.filter(only_audio=True).first().download(path)
    print("Download completo!")

    print("Convertendo arquivo..")
    print("Aguarde")

    for file in os.listdir(path):
        if re.search('mp4', file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
            
    print("Concluido")
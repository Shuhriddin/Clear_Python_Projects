from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        higest_res_stream = streams.get_highest_resolution()
        higest_res_stream.download(output_path=save_path)
        print("Видео успешно загружено!!!")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Выберите папка: {folder}")
    return folder


if __name__=="__main__":
    root = tk.Tk()
    root.withdraw()
    video_url = input("Введите YouTube ссылку: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Скачивается...")
        download_video(video_url, save_dir)
    else:
        print("Неверное место сохранения.")

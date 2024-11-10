from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Файл изменен: {event.src_path}")


observer = Observer()
observer.schedule(MyHandler(), path=".", recursive=True)
observer.start()

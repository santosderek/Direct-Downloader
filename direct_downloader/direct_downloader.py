# Written by: Derek Santos

# 3rd Party Modules
import requests

# Python Modules
import os
import re
from threading import Thread, active_count
from queue import Queue
import shutil


class Download_Manager():
    def __init__(self, list_of_urls: list, threads: int, directory_path: str):

        # Setting up queue
        self.queue = Queue()

        # Number of threads
        self.number_of_threads = threads

        # Directory downloading to
        self.directory_path = directory_path

        # Putting all urls into the queue
        for url in list_of_urls:
            # If url is blank, continue
            if url == '' or url == ' ':
                continue
            self.queue.put(url)

    def start(self):
        """ Start the threads to download urls within the queue """
        # Setting up thread
        self.workers = [Download_Worker(self.queue, self.directory_path)
                        for pos in range(self.number_of_threads)]

        # While the queue is not empty and the amount of threads are only 1
        # NOTE: When all threads are done, there should only be the main thread
        while not self.queue.empty() or active_count() > 1:
            pass


class Download_Worker():
    def __init__(self, queue, directory_path):
        # Init Queue
        self.queue = queue

        # Path to download to
        self.directory_path = directory_path

        # Init Thread
        self.thread = Thread(target=self.download, daemon=True, args=())
        self.thread.start()

    def download(self):
        """ Downloads a url that is stored within the queue variable """

        while not self.queue.empty():
            try:
                # Store the url to use
                url = self.queue.get()

                # Attempt connection to url
                req = requests.get(url, stream=True)

                # If could not finish download alert user and skip
                if req.status_code != 200:
                    print('Could not download:', url)
                    continue

                # The name of the file will be extracted from the url.
                file_name_start_pos = url.rfind('/') + 1
                file_name = url[file_name_start_pos:]

                # If a file within the directory exists, skip the file
                if os.path.exists(self.directory_path + file_name):
                    print('Skipping:', url)
                    continue

                # Start storing the contents of the url within a file.
                print('Downloading', url, end=' ', flush=True)
                with open(self.directory_path + file_name, 'wb') as current_file:
                    req.raw.decode_content = True
                    shutil.copyfileobj(req.raw, current_file)
                print('- Done.')
            except Exception as e:
                print('ERROR DOWNLOADING:', e)

                # If an error occured during downloading,
                # then delete the incomplete file
                try:
                    if os.path.exists(self.directory_name + file_name):
                        os.remove(self.directory_name + file_name)
                except Exception:
                    pass

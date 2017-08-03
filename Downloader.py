# Written by: Derek Santos

import requests
import os
import re
from threading import Thread, active_count
from queue import Queue
import shutil


class Download_Manager():
    def __init__(self, list_of_urls: list, threads: int):

        # Setting up queue
        self.queue = Queue()
        self.number_of_threads = threads

        for url in list_of_urls:
            # If url is blank, continue
            if url == '' or url == ' ':
                continue

            self.queue.put(url)

    def start(self):
        """ Start the threads to download urls within the queue """
        # Setting up thread
        self.workers = [Download_Worker(self.queue)
                        for pos in range(self.number_of_threads)]

        # While the queue is not empty and the amount of threads are only 1
        # NOTE: When all threads are done, there should only be the main thread
        while not self.queue.empty() or active_count() > 1:
            pass


class Download_Worker():
    def __init__(self, queue):
        # Init Queue
        self.queue = queue

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

                # Start storing the contents of the url within a file.
                print('Downloading', url, end=' ', flush=True)
                with open(file_name, 'wb') as current_file:
                    req.raw.decode_content = True
                    shutil.copyfileobj(req.raw, current_file)
                print('- Done.')
            except Exception as e:
                print('ERROR DOWNLOADING:', e)


def main():
    """ Read a file of urls and download them using Download_Manager """

    # Check if url files exists, else make it
    if not os.path.exists('urls.txt'):
        with open('urls.txt', 'w') as current_file:
            current_file.write('')
        print('urls.txt was created. Please put urls within this file.')
        return

    # Open the file, and read urls into a list
    with open('urls.txt', 'r') as current_file:
        list_of_urls = current_file.read().split('\n')

    # Put the list into a Download_Manager and start the downloads
    manager = Download_Manager(list_of_urls, threads=3)
    manager.start()


if __name__ == '__main__':
    main()

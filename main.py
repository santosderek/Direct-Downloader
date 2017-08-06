# Written by: Derek Santos

# Python Modules
import os

# Developer Modules
from downloader import Download_Manager


def main(path):
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
    manager = Download_Manager(list_of_urls, threads=3, path)
    manager.start()


if __name__ == '__main__':
    path = ''
    main(path)

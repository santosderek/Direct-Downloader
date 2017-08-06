# Written by: Derek Santos

# Python Modules
import os
from argparse import ArgumentParser

# Developer Modules
from downloader import Download_Manager


def parse_arguments():
    parser = ArgumentParser(description='Download a list of urls.')
    parser.add_argument('urls', metavar='urls', type=str,
                        nargs='+', help='single url to download')
    parser.add_argument('-f', '--folder', metavar='folder',
                        type=str, nargs='?', help='Change download folder')
    parser.add_argument('-t', '--threads', metavar='threads',
                        type=int, nargs='?', help='Number of threads to be used')
    parser.add_argument('-u', '--urlfile', metavar='urlfile',
                        type=bool, nargs='?', help='Use the urls within "url.txt"')
    return parser.parse_args()


def main():
    arguments = parse_arguments()

    if arguments.urlfile:
        # Check if url files exists, else make it
        if not os.path.exists('urls.txt'):
            with open('urls.txt', 'w') as current_file:
                current_file.write('')
            print('urls.txt was created. Please put urls within this file.')
            exit(1)
        # Open the file, and read urls into a list
        with open('urls.txt', 'r') as current_file:
            list_of_urls = current_file.read().split('\n')
    else:
        list_of_urls = arguments.urls

    # Path to download folder
    path = arguments.folder
    if path is None:
        path = '.'

    # Number of threads
    number_of_threads = arguments.threads

    if number_of_threads is None:
        number_of_threads = 3
    else:
        number_of_threads = int(number_of_threads)

    # print('Threads:', number_of_threads)
    # print('Path:', path)
    # print('List of Urls:', list_of_urls)

    # Put the list into a Download_Manager and start the downloads
    manager = Download_Manager(list_of_urls, number_of_threads, path)
    manager.start()


if __name__ == '__main__':
    main()

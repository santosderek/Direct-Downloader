dDownloader (Direct-Downloader)
===========

Download a list of direct urls, using a multi-threaded approach.

***

### How to install:

*** Repository developed in Python 3.6.x ***

*Can be downloaded from pip!*

    pip3 install Direct-Downloader

*OR*

*Copy repository from github:*

    git clone https://github.com/santosderek/Direct-Downloader

*Move into repository*

    cd Direct-Downloader

*Install Python Package*

    python3 setup.py install

*Congrats, it's installed! Now you can proceed bellow*

***

### How to use:
#### Following commands can be used:
***Base command:***

    dDownloader [options] URLS



***Help page***

*View the help page*

    dDownloader --help

***Base Command***

*Multiple urls can be used at once.*

    dDownloader URLS


***Number Of Threads To Use***

*By default 3 threads will be used.*

    dDownloader --threads [NUMBER_OF_THREADS] URLS | OR | dDownloader -t [NUMBER_OF_THREADS] URLS

***Folder Download Path To Use***

    dDownloader --folder [path/to/download/directory] URLS | OR | dDownloader -f [path/to/download/directory] URLS

***Bulk Download using a url.txt file***

*Download a list of urls from a file named url.txt.*

*Makes it easier for bulk downloads.*

*Run the command within the same directory as the .txt, and have urls on different lines.*

    dDownloader --urlfile | OR | dDownloader -u

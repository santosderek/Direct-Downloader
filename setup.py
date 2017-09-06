from setuptools import setup, find_packages

setup(name='Direct Downloader',
      version='0.3',
      description='Download a list of direct links using multi-threading.',
      author='Derek Santos',
      license='The MIT License (MIT)',
      url='https://github.com/santosderek/Direct-Downloader',
      packages=['direct_downloader'],
      scripts=['direct_downloader/main.py',
               'direct_downloader/direct_downloader.py'],
      entry_points={
          'console_scripts':
              ['dDownloader = direct_downloader.main:main',
               'direct_downloader = direct_downloader.main:main']
      },
      install_requires=[
          'requests',
          'bs4'
      ],
      keywords=['testing', 'logging', 'example']
      )

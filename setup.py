from setuptools import setup, find_packages

setup(name='Direct Downloader',
      version='0.6',
      description='Download a list of direct links using multi-threading.',
      author='Derek Santos',
      author_email='derek@dyrenex.com',
      license='The MIT License (MIT)',
      url='https://github.com/santosderek/Direct-Downloader',
      packages=find_packages(),
      scripts=['directdownloader/__main__.py',
               'directdownloader/direct_downloader.py'],
      entry_points={
          'console_scripts': [
              'dDownloader = directdownloader.__main__:main'

          ]
      },
      install_requires=[
          'requests',
          'bs4'
      ],
      keywords=['testing', 'logging', 'example']
      )

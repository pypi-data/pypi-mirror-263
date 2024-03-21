from setuptools import setup

setup(
    name='SpotifyLinuxOpen',
    version='0.1.0',
    url='https://git.orudo.ru/trueold89/SpotifyLinuxOpen',
    author='trueold89',
    author_email='trueold89@orudo.ru',
    description="A simple cli-utility that allows you to open 'open.spotify.com' in the Spotify desktop client on Linux",
    packages=['sllo'],
    long_description=open('README.md').read(),
    entry_points={
        "console_scripts": ["slopen = sllo.Main:main"]
    }
)

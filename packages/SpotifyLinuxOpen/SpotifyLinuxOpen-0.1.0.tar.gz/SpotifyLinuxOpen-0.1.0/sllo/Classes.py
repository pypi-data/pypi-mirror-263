from enum import Enum
from sys import orig_argv as argv
from subprocess import run as execute
from subprocess import PIPE
from subprocess import Popen as subExecute


class SpotifyLink:
    class SMTH(Enum):
        CTYPE = 0
        CID = 1

    def __init__(self, link: str) -> None:
        """
        :rtype: None
        """
        if not ("open.spotify.com" in link):
            raise ValueError("This is not a SpotifyOpen link")
        self.__link = link

    def __getsmth(self, item: SMTH) -> str:
        """
        :type item: SMTH
        :rtype: str
        """
        split = self.__link[8:].split("/")[1:]
        return split[item.value]

    def __gettype(self) -> str:
        """
        :return: Content type
        :rtype: str
        """
        return self.__getsmth(self.SMTH.CTYPE)

    def __getid(self) -> str:
        """
        :return: Spotify content id
        :rtype: str
        """
        return self.__getsmth(self.SMTH.CID)

    def uri(self) -> str:
        """
        :return: Spotify URI
        :rtype: str 
        """
        ctype = self.__gettype()
        cid = self.__getid()
        return f"spotify:{ctype}:{cid}"


class Interface:

    @staticmethod
    def __getlink() -> SpotifyLink:
        """
        :rtype: SpotifyLink
        """
        args = argv[2:]
        if len(args) != 1:
            raise ValueError("Bad usage")
        return SpotifyLink(args[0])

    @staticmethod
    def __check() -> bool:
        """
        :rtype: bool
        """
        stoud = execute("dbus-send --session --dest=org.freedesktop.DBus --type=method_call --print-reply "
                        "/org/freedesktop/DBus org.freedesktop.DBus.ListNames | grep spotify", shell=True, text=True,
                        stdout=PIPE).stdout
        if stoud == "":
            return True

    def open(self) -> None:
        """
        :rtype: None
        """
        uri = self.__getlink().uri()
        if self.__check():
            subExecute(["spotify", f"--uri={uri}"])
        else:
            execute(f"dbus-send --type=method_call --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 "
                    f"org.mpris.MediaPlayer2.Player.OpenUri string:'{uri}'", shell=True)

    @staticmethod
    def help() -> None:
        """
        :rtype: None
        """
        msg = ("\nUsage:\nslopen 'https://open.spotify.com/<type>/<id>'\n\nExample:\n"
               "slopen 'https://open.spotify.com/track/4PTG3Z6ehGkBFwjybzWkR8?si=a4ec356b33fd49d3'")
        print(msg)

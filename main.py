import os

os.environ['PYTHON_VLC_MODULE_PATH'] = 'vlc'
import sys

from PySide2 import QtWidgets

import vlc

file = "/path/xxx.mp4"


class Player(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Player, self).__init__(parent)
        self.setWindowTitle("Media Player")
        # creating a basic vlc instance
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        ##########video frame
        self.videoframe = QtWidgets.QFrame(
            frameShape=QtWidgets.QFrame.Box, frameShadow=QtWidgets.QFrame.Raised
        )

        if sys.platform.startswith("linux"):  # for Linux using the X Server
            self.mediaplayer.set_xwindow(self.videoframe.winId())
        elif sys.platform == "win32":  # for Windows
            self.mediaplayer.set_hwnd(self.videoframe.winId())
        elif sys.platform == "darwin":  # for MacOS
            self.mediaplayer.set_nsobject(self.videoframe.winId())

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QVBoxLayout(central_widget)
        lay.addWidget(self.videoframe)

        filename = file
        media = self.instance.media_new(filename)
        self.mediaplayer.set_media(media)
        self.mediaplayer.play()


def main():
    app = QtWidgets.QApplication(sys.argv)

    player = Player()
    player.show()
    player.resize(320, 240)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

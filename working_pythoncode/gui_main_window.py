#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
A Simple sketch of the Gui
author: H. Zhu
"""

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from gui_utils import *

class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow,self).__init__()
        self.setAcceptDrops(True)
        self.init_ui()

    def init_ui(self):

        def addspeaker():

            new_speaker = Speaker(1+len(gui_dict))
            scene.addItem(new_speaker)
            view.viewport().update()

        def reset():

            for item in scene.items():
                scene.removeItem(item)

            gui_dict.clear()
            del speaker_list[:]

            new_speaker = Speaker(1)
            new_head = Head()

            scene.addItem(new_speaker)
            scene.addItem(new_head)
            view.viewport().update()

        # set items
        default_speaker = Speaker(1)

        head = Head()

        # set scene and view
        scene = Room()
        scene.setSceneRect(0,0,250,250)
        scene.addItem(default_speaker)
        scene.addItem(head)
        view = View(scene)

        # set buttons
        add_speaker_button = AddSpeakerButton()
        reset_button = ResetButton()

        # set layout
        layout = QVBoxLayout()
        layout.addWidget(view)
        layout.addWidget(add_speaker_button)
        layout.addWidget(reset_button)

        # connect signal and slots
        add_speaker_button.clicked.connect(addspeaker)
        reset_button.clicked.connect(reset)

        # set window
        self.setLayout(layout)
        self.resize(640,480)
        self.setWindowTitle('3D Audio')
        self.show()

def main():

    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

from PyQt4 import QtCore, QtGui

gui_dict = {}
head_pos = QtCore.QPoint(100, 100)
speaker_list = []

class Item(QtGui.QGraphicsPixmapItem):

    origin_image = QtGui.QImage('./image/speaker.png')

    def __init__(self):

        image = self.origin_image.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        super(Item, self).__init__(QtGui.QPixmap.fromImage(image))
        self.setToolTip("Click and drag this speaker!")
        self.setCursor(QtCore.Qt.OpenHandCursor)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)

    def mousePressEvent(self, event):
        if event.button() != QtCore.Qt.LeftButton:
            event.ignore()
            return

        self.setCursor(QtCore.Qt.ClosedHandCursor)

    def mouseMoveEvent(self, event):
        if QtCore.QLineF(QtCore.QPointF(event.screenPos()), QtCore.QPointF(event.buttonDownScreenPos(QtCore.Qt.LeftButton))).length() < QtGui.QApplication.startDragDistance():
            return

        drag = QtGui.QDrag(event.widget())
        mime = QtCore.QMimeData()
        drag.setMimeData(mime)

        image = self.origin_image.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        pixmap = QtGui.QPixmap.fromImage(image)

        pixmap.setMask(pixmap.createHeuristicMask())

        drag.setPixmap(pixmap)
        drag.setHotSpot(QtCore.QPoint(30, 30))

        drag.exec_()
        self.setCursor(QtCore.Qt.OpenHandCursor)

    def mouseReleaseEvent(self, event):
        self.setCursor(QtCore.Qt.OpenHandCursor)


class Room(QtGui.QGraphicsScene):

    current_item = 0

    def mousePressEvent(self, e):
        self.current_item = self.itemAt(e.scenePos())
        QtGui.QGraphicsScene.mousePressEvent(self, e)

    def dragEnterEvent(self, e):
        e.acceptProposedAction()

    def dropEvent(self, e):
        global head_pos
        global speaker_list
        self.current_item.setPos(e.scenePos())

        if self.current_item.type == 'head':
            head_pos = e.scenePos()

            for speaker in speaker_list:
                speaker.cal_rel_pos()

        elif self.current_item.type == 'speaker':
            self.current_item.cal_rel_pos()

    def dragMoveEvent(self, e):
        e.acceptProposedAction()

class View(QtGui.QGraphicsView):

    def dragEnterEvent(self, e):
        e.acceptProposedAction()
        QtGui.QGraphicsView.dragEnterEvent(self, e)

    def dropEvent(self, e):
        self.viewport().update()
        QtGui.QGraphicsView.dropEvent(self, e)

    def dragMoveEvent(self, e):
        e.acceptProposedAction()
        QtGui.QGraphicsView.dragMoveEvent(self, e)

class AddSpeakerButton(QtGui.QPushButton):

    def __init__(self):
        super(AddSpeakerButton,self).__init__('Add Speaker')

class ResetButton(QtGui.QPushButton):

    def __init__(self):
        super(ResetButton,self).__init__('Reset')

class Speaker(Item):

    index = 1
    type = 'speaker'
    origin_image = QtGui.QImage('./image/speaker.png')

    def __init__(self, index):
        global gui_dict
        global speaker_list

        super(Speaker, self).__init__()
        self.setPos(0,0)
        self.index = index
        speaker_list.append(self)
        self.cal_rel_pos()

    def cal_rel_pos(self):
        global head_pos
        global gui_dict
        dx = self.x() - head_pos.x()
        dy = head_pos.y() - self.y()
        dis = (dx**2+dy**2)**0.5

        from math import acos, degrees
        deg = degrees(acos(dy/dis))
        if dx < 0:
            deg = 360 - deg

        gui_dict['sp'+str(self.index)] = [deg, dis, 0]
        print(gui_dict)

class Head(Item):

    type = 'head'
    origin_image = QtGui.QImage('./image/head.jpeg')

    def __init__(self):
        global head_pos

        super(Head,self).__init__()
        self.setPos(100,100)
        head_pos = self.pos()

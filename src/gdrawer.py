import sys
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class GDrawer(QWidget):

    def __init__(self, parent = None ):
        QWidget.__init__(self, parent )
        #print("gesture drawer")
        self.square_size = 100
        self.margin = 8
        self.setMinimumSize( self.square_size + self.margin, self.square_size + self.margin )
        self.setMaximumSize( self.square_size + self.margin, self.square_size + self.margin )

        self.path = QPolygon()
        self.label = "Label"


    ##############################
    def scaleToSquare(self, points):
        max_x, max_y = np.max(points, 0)
        min_x, min_y = np.min(points, 0)
        b_width = max_x - min_x
        b_height = max_y - min_y
        newPoints = np.zeros((1, 2))
        for point in points:
            q = np.array([0., 0.])
            q[0] = ( (point[0]-min_x) * self.square_size) / b_width + self.margin /2
            q[1] = ( (point[1]-min_y) * self.square_size) / b_height + self.margin /2
            newPoints = np.append(newPoints, [q], 0)
        return newPoints[1:]


    ##############################
    def set_gesture_path(self, points, label="No Label"):
        self.path.clear()
        norm_points = self.scaleToSquare( points )
        #print(norm_points)
        for p in norm_points:
            self.path.append( QPoint(p[0], p[1]) )
        self.label = label
        self.repaint()


    ##############################
    def paintEvent(self, QPaintEvent):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        if self.path == QPolygon():
            return
        p.setPen(Qt.red)
        p.setBrush(Qt.red)
        p.drawPolyline( self.path )
        p.drawEllipse( self.path[0], 2, 2 )


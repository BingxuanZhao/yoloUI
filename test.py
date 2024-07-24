import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsPolygonItem
from PyQt5.QtGui import QPolygonF, QPainter, QPen
from PyQt5.QtCore import Qt, QPointF

class PolygonDrawer(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setRenderHint(QPainter.Antialiasing)
        
        # Initialize variables for polygon drawing
        self.polygon_points = []
        self.point_items = []
        self.polygon_item = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            point = self.mapToScene(event.pos())
            self.polygon_points.append(point)
            
            # Draw point
            point_item = QGraphicsEllipseItem(point.x() - 3, point.y() - 3, 6, 6)
            point_item.setBrush(Qt.black)
            self.scene.addItem(point_item)
            self.point_items.append(point_item)
        
        super().mousePressEvent(event)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return and len(self.polygon_points) > 2:
            # Finalize the polygon by connecting points
            if self.polygon_item:
                self.scene.removeItem(self.polygon_item)
            self.polygon_item = QGraphicsPolygonItem(QPolygonF(self.polygon_points))
            self.polygon_item.setPen(QPen(Qt.red, 2))
            self.polygon_item.setBrush(Qt.transparent)
            self.scene.addItem(self.polygon_item)
            self.polygon_points = []
            for item in self.point_items:
                self.scene.removeItem(item)
            self.point_items.clear()
            self.scene.update()
        
        super().keyPressEvent(event)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Draw Polygon')
        self.setGeometry(100, 100, 800, 600)
        self.polygon_drawer = PolygonDrawer()
        self.setCentralWidget(self.polygon_drawer)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

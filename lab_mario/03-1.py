# 02. pyqt_widget.py
# PyQt 위젯
import sys
import retro
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,\
    QWidget, QLabel, QPushButton
import numpy as np

env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')

env.reset()

screen = env.get_screen()


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        # 창 크기 고정
        self.setFixedSize(224, 240)
        # 창 제목 설정
        self.setWindowTitle('GA Mario')

        # 이미지
        label_image = QLabel(self)

        image = np.array(screen)
        qimage = QImage(image, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(2000, 2000, Qt.IgnoreAspectRatio)

        label_image.setPixmap(pixmap)
        label_image.setGeometry(0, 0, 224, 240)

        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MyApp()
   sys.exit(app.exec_())
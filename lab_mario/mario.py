import sys, retro
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import numpy as np

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        # 게임 환경 생성
        self.env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        # 새게임 시작
        self.env.reset()

        self.screen_size = 1

        # 키배열 : B, NULL, SELECT, START, U, D, L, R, A
        self.button = [0, 0, 0, 0, 0, 0, 0, 0, 0]


        self.setWindowTitle('GA-Mario')
        self.label_image = QLabel(self)

        # 타이머 생성
        qtimer = QTimer(self)
        # 타이머에 실행할 함수 연결
        qtimer.timeout.connect(self.timer)
        # 1초(1000밀리초)마다 연결된 함수를 실행
        qtimer.start(1000//60)

        # 창 띄우기
        self.show()

    def timer(self):
        self.env.step(np.array(self.button))

        #화면 가져오기
        screen = self.env.get_screen()

        # 창 크기 고정
        self.setFixedSize(screen.shape[0]*3, screen.shape[1]*3)
        # 창 제목 설정
        self.setWindowTitle('GA-Mario')

        image = np.array(screen)
        qimage = QImage(image, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(screen.shape[0]*3, screen.shape[1]*3, Qt.IgnoreAspectRatio)

        self.label_image.setPixmap(pixmap)
        self.label_image.setGeometry(0, 0, screen.shape[0]*3, screen.shape[1]*3)

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Up:
            self.button[8] = 1
        if key == Qt.Key_Down:
            self.button[5] = 1
        if key == Qt.Key_Left:
            self.button[6] = 1
        if key == Qt.Key_Right:
            self.button[7] = 1
        if key == Qt.Key_A:
            self.button[4] = 1
        if key == Qt.Key_B:
            self.button[0] = 1
        if key == Qt.Key_R:
                self.env.reset()



    def keyReleaseEvent(self, event):
        key = event.key()

        if key == Qt.Key_Up:
            self.button[8] = 0
        if key == Qt.Key_Down:
            self.button[5] = 0
        if key == Qt.Key_Left:
            self.button[6] = 0
        if key == Qt.Key_Right:
            self.button[7] = 0
        if key == Qt.Key_A:
            self.button[4] = 0
        if key == Qt.Key_B:
            self.button[0] = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
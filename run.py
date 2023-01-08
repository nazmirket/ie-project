import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QPushButton

from scripts import *

from listeners import *

app = QApplication(sys.argv)

window = uic.loadUi('main.ui')
window.show()


btn_upload = window.findChild(QPushButton, "btn_upload")
btn_upload.clicked.connect(lambda:btn_upload_click_listener(window, btn_upload))

btn_forecast = window.findChild(QPushButton, "btn_forecast")
btn_forecast.clicked.connect(lambda:btn_forecast_click_listener(window, btn_forecast))



app.exec()

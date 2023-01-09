from PyQt5.QtWidgets import QFileDialog
import shutil
from pathlib import Path

from scripts import *

def btn_upload_click_listener(window, self):
    source = QFileDialog.getOpenFileName(window)
    target = Path('resources/data.xlsx').absolute()
    shutil.copyfile(source[0], target)
    self.setText(source[0])
    self.setStyleSheet('QPushButton {background-color: green; color: white;}')
    init()

def btn_forecast_click_listener(window, self, mvg, exp, reg):
    if(mvg):
        forecast('mvg')
    elif(exp):
        forecast('exp')
    elif(reg):
        forecast('reg')


        
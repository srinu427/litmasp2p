import os
import sys
import json
import requests
import threading

from PyQt5 import QtWidgets, QtGui, QtCore
from qt_material import apply_stylesheet

import qtcustomwidgets


class UIApp(QtWidgets.QMainWindow):
    def __init__(self, master=None):
        QtWidgets.QMainWindow.__init__(self, master)
        self.setWindowTitle("Main Window")
        self.create_ui()
        
        
    def create_ui(self):
        """Set up the user interface, signals & slots
        """
        self.widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.widget)
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.widget.setLayout(self.vboxlayout)
        
        self.cipdata = qtcustomwidgets.customIPSelect()
        
        self.vboxlayout.addWidget(self.cipdata)
    
    
    def create_connect_page(self):
        self.conn_widget = QtWidgets.QWidget(self)
        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    gui = UIApp()
    gui.show()
    gui.resize(960, 600)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
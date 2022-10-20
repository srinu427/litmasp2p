
from PyQt5 import QtWidgets, QtGui, QtCore

class customIPSelect(QtWidgets.QWidget):
    def __init__(self, master=None):
        QtWidgets.QWidget.__init__(self, master)
        self.vlayout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vlayout)

        self.ip_hlay = QtWidgets.QHBoxLayout()
        self.ip_lbl = QtWidgets.QLabel("Peer IP")
        self.ip_lbl.setFixedHeight(20)
        self.ip_txt = QtWidgets.QLineEdit()
        self.ip_txt.setFixedHeight(20)
        self.ip_hlay.addWidget(self.ip_lbl, 2)
        self.ip_hlay.addStretch(3)
        self.ip_hlay.addWidget(self.ip_txt, 5)

        self.sport_hlay = QtWidgets.QHBoxLayout()
        self.sport_lbl = QtWidgets.QLabel("Peer Send Port")
        self.sport_lbl.setFixedHeight(20)
        self.sport_val = QtWidgets.QSpinBox()
        self.sport_val.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sport_val.setFixedHeight(20)
        self.sport_val.setFixedWidth(60)
        self.sport_val.setMinimum(500)
        self.sport_val.setMaximum(20000)
        self.sport_val.setValue(4278)
        self.sport_hlay.addWidget(self.sport_lbl)
        self.sport_hlay.addWidget(self.sport_val)

        self.rport_hlay = QtWidgets.QHBoxLayout()
        self.rport_lbl = QtWidgets.QLabel("Peer Recv Port")
        self.rport_lbl.setFixedHeight(20)
        self.rport_val = QtWidgets.QSpinBox()
        self.rport_val.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.rport_val.setFixedHeight(20)
        self.rport_val.setFixedWidth(60)
        self.rport_val.setMinimum(500)
        self.rport_val.setMaximum(20000)
        self.rport_val.setValue(4279)
        self.rport_hlay.addWidget(self.rport_lbl)
        self.rport_hlay.addWidget(self.rport_val)

        self.vlayout.addLayout(self.ip_hlay)
        self.vlayout.addLayout(self.sport_hlay)
        self.vlayout.addLayout(self.rport_hlay)

        self.vlayout.addStretch(1)


    def get_ip(self):
        return self.ip_txt.text()

    def get_sport(self):
        return self.sport_val.value()

    def get_rport(self):
        return self.rport_val.value()
#Snap Metronome
import threading
from playsound import playsound
from PyQt5.QtWidgets import * 
import time

global stopThread

app = QApplication([])
window=QWidget()
layout=QVBoxLayout()

def defaultClick():
    global stopThread
    stopThread = False
    x = threading.Thread(target=startMetronome, args=("default",))
    x.start()
def halfClick():
    global stopThread
    stopThread = False
    x = threading.Thread(target=startMetronome, args=("half",))
    x.start()
def quarterClick():
    global stopThread
    stopThread = False
    x = threading.Thread(target=startMetronome, args=("quarter",))
    x.start()
def jazzClick():
    global stopThread
    stopThread = False
    x = threading.Thread(target=startMetronome, args=("jazz",))
    x.start()

def startMetronome(interval):
    global stopThread
    if interval == "default":
        while True:
            playsound("snap.wav")
            time.sleep(0.9)
            if stopThread:
                break
    if interval =="half":
        while True:
            playsound("snap.wav")
            time.sleep(0.4)
            if stopThread:
                break
    if interval =="quarter":
        while True:
            playsound("snap.wav")
            time.sleep(0.233)
            if stopThread:
                break
    if interval =="jazz":
        while True:
            playsound("snap.wav")
            time.sleep(0.4)
            playsound("snap.wav")
            time.sleep(0.2)
            playsound("snap.wav")
            time.sleep(0.1)
            if stopThread:
                break

def stopThread():
    global stopThread
    stopThread = True

defaultBtn = QPushButton('default')
defaultBtn.clicked.connect(defaultClick)
layout.addWidget(defaultBtn)

halfBtn = QPushButton('half')
halfBtn.clicked.connect(halfClick)
layout.addWidget(halfBtn)

quarterBtn = QPushButton('quarter')
quarterBtn.clicked.connect(quarterClick)
layout.addWidget(quarterBtn)

jazzBtn = QPushButton('jazz')
jazzBtn.clicked.connect(jazzClick)
layout.addWidget(jazzBtn)

stopBtn = QPushButton('stop')
stopBtn.clicked.connect(stopThread)
layout.addWidget(stopBtn)

window.setLayout(layout)
window.show()

app.exec_()
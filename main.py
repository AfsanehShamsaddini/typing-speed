import string
import time

from  PyQt5.QtWidgets import  QMainWindow, QApplication,QLabel,QPushButton,QLineEdit,QCheckBox,QMessageBox
from PyQt5 import uic
import sys
import random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi('speed_type.ui',self)
        self.label = self.findChild(QLabel,"title_lbl")
        self.text_label = self.findChild(QLabel,"text_lbl")
        self.time_label = self.findChild(QLabel, "time_lbl")
        self.accuracy_label = self.findChild(QLabel, "accuracy_lbl")
        self.wpm_label = self.findChild(QLabel, "wpm_lbl")
        self.input_text = self.findChild(QLineEdit, "textinput")

        self.user_input = ''
        self.end_time = 0
        self.start_time = 0
        self.show()

    def enterPress(self):
            self.user_input = self.input_text.text()
            self.end_time = time.time()
            time_lapsed = self.end_time - self.start_time
            sen_lst = self.text_label.text().split()
            wpm = len(sen_lst) * 60 / (5 * time_lapsed)
            words_lst = self.user_input.split()
            words_count = len(sen_lst)
            correct_words = 0
            for i,word in enumerate(words_lst):
                if sen_lst[i] == word:
                    correct_words += 1
            accuracy = (correct_words / words_count) * 100

            self.time_label.setText(f"Time:  {round(time_lapsed)} secs")
            self.accuracy_label.setText(f"Accuracy:  {round(accuracy)}% ")
            self.wpm_label.setText(f"Wpm:  {round(wpm)} ")
            # self.main()





    def get_random_sentense(self):
        data = open('sentenses.txt' , 'r').read().split(',')
        sentense = random.choice(data)
        return sentense

    def reset_speed(self):
        self.user_input = ''
        self.end_time = 0
        self.start_time = 0
        self.input_text.clear()
        self.text_label.setText('')


    def main(self):
        self.reset_speed()
        self.text_label.setText(self.get_random_sentense())
        self.start_time = time.time()
        self.input_text.editingFinished.connect(self.enterPress)




if __name__ == '__main__':

    app=QApplication(sys.argv)
    UIWindow = UI()
    UIWindow.main()
    app.exec_()


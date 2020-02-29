# coding: utf8
# PyQt5录频软件
# 

import sys, os

from PyQt5 import QtCore, QtGui, QtWidgets
from RecordMainWindow import Ui_PyQt5Recording
from record import *

class MainWindow(QtWidgets.QMainWindow, Ui_PyQt5Recording):
    video_thread = VideoCapThread('tmp.avi')
    sys_thread = SoundRecThread('sys.wav')
    mic_thread = AudioRecThread('mic.wav')
    def __init__(self):
        super(MainWindow, self).__init__()
        self.record_flag = True
        self.system = True
        self.mic = False
        self.file_path = QtCore.QDir.currentPath()
        self.out_file_name = "outfile"
        self.initUi()
        self.fit_in_file_name()
        self.change_record_flag()


    def initUi(self):
        self.setupUi(self)
        self.file_path_btn.clicked.connect(self.fit_in_file_path)
        self.file_path_text.selectionChanged.connect(self.fit_in_file_path)
        self.system_cbx.stateChanged.connect(self.change_system)
        self.microphone_cbx.stateChanged.connect(self.change_microphone)
        self.file_name_text.editingFinished.connect(self.fit_in_file_name)
        self.fit_in_file_name(self.out_file_name)
        self.out_file_name = self.prepare_file_name(self.out_file_name)
        self.fit_in_file_path(self.file_path)
        self.start_stop_btn.clicked.connect(self.start_stop_record)


    def prepare_file_name(self, file_name):
        path = self.file_path
        of = file_name
        if len(of)<=4:
            pass
        elif of[-4:] == ".mp4":# 去后缀
            of = of[:-4]
        os.chdir(path)
        fn = path + "/" + of + ".mp4"
        name = of + ".mp4"
        i = 1
        while os.path.exists(fn):
            name = of + "_" + str(i) + ".mp4"
            fn = path + "/" + name
            i += 1
        self.out_file_name = name
        return name


    def fit_in_file_path(self, path=None):
        file_path = path
        if not file_path:
            file_path = self.open_file_path()
        self.file_path = file_path
        self.file_path_text.setText(file_path)
        return


    def fit_in_file_name(self, name=None):
        file_name = name
        if not file_name:
            file_name = self.prepare_file_name(self.file_name_text.text())
        self.file_name = file_name
        self.file_name_text.setText(file_name)
        return


    def open_file_path(self):
        cur_path = QtCore.QDir.currentPath()
        dlgTitle = "选择存储路径"
        selected_path = QtWidgets.QFileDialog.getExistingDirectory(self, dlgTitle, cur_path, QtWidgets.QFileDialog.ShowDirsOnly)
        return selected_path


    def change_system(self):
        self.system = not self.system


    def change_microphone(self):
        self.mic = not self.mic


    def change_record_flag(self):
        self.record_flag = not self.record_flag
        if self.record_flag:
            # self.record_label.setText("<p background-color:rgb(0, 255, 0)>T</p>")
            self.record_label.setText('<p style="font-family:Monotype Corsiva;color:red">录制中</p>')
        else:
            # self.record_label.setText('<p style="font-family:Monotype Corsiva;color:red">F</p>')
            self.record_label.setText('<p style="font-family:Monotype Corsiva;color:green">未在录制</p>')
        return


    def start_stop_record(self):
        if not self.record_flag:
            self.sys_thread = SoundRecThread('sys.wav') if self.system else None
            self.mic_thread = AudioRecThread('mic.wav') if self.mic else None
            time.sleep(1)
            self.change_record_flag()
            self.video_thread.start()
            if self.sys_thread is not None:
                self.sys_thread.start()
            if self.mic_thread is not None:
                self.mic_thread.start()
        else:
            self.video_thread.stoprecord()
            self.video_thread.join()
            if self.sys_thread is not None:
                self.sys_thread.stoprecord()
                self.sys_thread.join()
            if self.mic_thread is not None:
                self.mic_thread.stoprecord()
                self.mic_thread.join()
            ffmpeg_thread = None
            if (self.sys_thread is not None) and (self.mic_thread is not None):
                print("1"+self.file_path+'/'+self.out_file_name)
                ffmpeg_thread = FFmpegThread('tmp.avi', 'sys.wav', self.file_path+'/'+self.out_file_name, 'mic.wav')
            elif self.sys_thread is not None:
                print("2"+self.file_path+'/'+self.out_file_name)
                ffmpeg_thread = FFmpegThread('tmp.avi', 'sys.wav', self.file_path+'/'+self.out_file_name)
                print("aa")
            elif self.mic_thread is not None:
                print("3"+self.file_path+'/'+self.out_file_name)
                ffmpeg_thread = FFmpegThread('tmp.avi', 'mic.wav', self.file_path+'/'+self.out_file_name)
            else:
                print("4"+self.file_path+'/'+self.out_file_name)
                ffmpeg_thread = FFmpegThread('tmp.avi', None, self.file_path+'/'+self.out_file_name)
            ffmpeg_thread.start()
            self.change_record_flag()
            while True:
                if ffmpeg_thread.finish:
                    break
            ffmpeg_thread.join()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
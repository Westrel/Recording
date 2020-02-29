# 录音录屏，合成
import queue
import sys
import threading
import wave
import subprocess
import os
import time
from cv2 import cv2
import numpy as np
import sounddevice as sd
import soundfile as sf
from PIL import ImageGrab
from pyaudio import PyAudio, paInt16
from scipy.io import wavfile

# 视频
class VideoCapThread(threading.Thread):
    def __init__(self, videofile='record.avi'):
        threading.Thread.__init__(self)
        self.bRecord = True
        self.video = cv2.VideoWriter(videofile,
                                     cv2.VideoWriter_fourcc(*'XVID'), 32,# (1919, 1079))
                                     ImageGrab.grab(bbox=(0,0,1920,1080)).size)  # 帧率为32，可以调节
        # print(ImageGrab.grab(bbox=(0,0,1920,1080)).size)

    def run(self):
        while self.bRecord:
            im = ImageGrab.grab(bbox=(0,0,1920,1080))
            imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
            self.video.write(imm)
        self.video.release()
        cv2.destroyAllWindows()
 
    def stoprecord(self):
        self.bRecord = False

# 系统声音
class SoundRecThread(threading.Thread):
    def __init__(self, audiofile='record.wav'):
        threading.Thread.__init__(self)
        self.bRecord = True
        self.filename = audiofile
        self.samplerate = 44100
        self.channels = 2
 
    def run(self):
        q = queue.Queue()
        sd.default.device[0] = 11
        def callback(indata, frames, time, status):
            q.put(indata.copy())
 
        with sf.SoundFile(self.filename,mode='x',samplerate=self.samplerate,
                          channels=self.channels) as file:
            with sd.InputStream(samplerate=self.samplerate,channels=self.channels,
                                callback=callback):
                while self.bRecord:
                    file.write(q.get())
 
    def stoprecord(self):
        self.bRecord = False

# 麦克风声音
class AudioRecThread(threading.Thread):
    def __init__(self, audiofile='record.wav'):
        threading.Thread.__init__(self)
        self.bRecord = True
        self.audiofile = audiofile
        self.chunk = 1024
        self.format = paInt16
        self.channels = 1
        self.rate = 16000

    def run(self):
        audio = PyAudio()
        wavfile = wave.open(self.audiofile, 'wb')
        wavfile.setnchannels(self.channels)
        wavfile.setsampwidth(audio.get_sample_size(self.format))
        wavfile.setframerate(self.rate)
        wavstream = audio.open(format=self.format,
                               channels=self.channels,
                               rate=self.rate,
                               input=True,
                               frames_per_buffer=self.chunk)
        while self.bRecord:
            wavfile.writeframes(wavstream.read(self.chunk))
        wavstream.stop_stream()
        wavstream.close()
        audio.terminate()

    def stoprecord(self):
        self.bRecord = False

# 音视频拼接
class FFmpegThread(threading.Thread):
    def __init__(self, avi_file, wav1_file, mp4_file, wav2_file=None):
        threading.Thread.__init__(self)
        self.avi_file = avi_file
        self.wav1_file = wav1_file
        self.mp4_file = mp4_file
        if wav2_file:
            self.wav2_file = wav2_file
        else:
            self.wav2_file = None
        self.finish = False
 
    def run(self):
        self.finish = False
        if self.wav2_file:
            command = ['ffmpeg', '-i' , self.avi_file, '-i', self.wav1_file, '-i', self.wav2_file,'-strict', '-2', '-f', 'mp4', self.mp4_file]
        elif not self.wav1_file:
            command = ['ffmpeg', '-i' , self.avi_file, '-c', 'copy', '-map', '0', self.mp4_file]
        else:
            command = ['ffmpeg', '-i' , self.avi_file, '-i', self.wav1_file, '-strict', '-2', '-f', 'mp4', self.mp4_file]
        ret = subprocess.call(command)
        print(ret)
        os.remove(self.avi_file)
        if self.wav1_file:
            os.remove(self.wav1_file)
        if self.wav2_file:
            os.remove(self.wav2_file)
        self.finish = True
    




if __name__ == "__main__":
    t1 = VideoCapThread('tmp1.avi')
    # t2 = SoundRecThread('sys.wav')
    # t3 = AudioRecThread('mic.wav')
    t1.start()
    # t2.start()
    # t3.start()
    time.sleep(35)
    # t1.stoprecord()
    # t2.stoprecord()
    # t3.stoprecord()
    # t4 = FFmpegThread('tmp1.avi', 'mic.wav', 'output.mp4')
    t4 = FFmpegThread('tmp1.avi', None, 'output.mp4')

    # t4 = FFmpegThread('tmp1.avi', 'sys.wav', 'output.mp4', 'mic.wav')
    t4.start()




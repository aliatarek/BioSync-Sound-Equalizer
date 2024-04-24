from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSlider, QLabel, QPushButton, QFileDialog
from pyqtgraph import PlotWidget
import pandas as pd
import math
#from mplwidget import MplWidget
import os
import pyqtgraph as pg
import numpy as np
from scipy import signal
from scipy.fft import fft
from scipy.fft import rfft ,rfftfreq, irfft
from scipy.signal import hann, freqz, hamming,gaussian,boxcar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib
import matplotlib.pyplot as plt
from mplwidget import MplWidget
from scipy.io import wavfile
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QTimer
import wave
import wfdb
import scipy.io
from scipy.interpolate import interp1d
import os
from datetime import datetime

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')
max_freqs=[]
magnitudes=[]
indecies=[]
normal_magnitude=[]
frequency=0
sliders=[]
slider_values=[]
saved_signal=[]
max_freqss=[]
thereIsWindow=False
flagSpec=False
fourier=0
fourier2=0
fourier3=0
is_playing = True
plotType=""
window=None
Caller=None
callingSlider="0"
callingWindow=None
freq_ranges=[]
CurrentWindow=1
modified_magnitude=[]
counter=0
appliedWindow=1
chosenWindow="R"
loadedSignal=0
def load_Signal(self):
    global saved_signal
    global loadedSignal
    global Time
    global plotType
    global counter
    Signal_data = []
    Time = []
    self.input.clear()
    self.output.clear()
    self.frequencies.clear()
    
    options = QFileDialog.Options()
    self.file_name1, _ = QFileDialog.getOpenFileName(self, "Open File", "", "CSV Files (*.csv);;Text Files (*.txt);;DAT Files (*.dat);;WAV Files (*.wav);;MAT Files (*.mat);;ATR Files (*.atr)", options=options)
    if self.file_name1:
        
        # Determine the file extension
        self.file_extension = self.file_name1.split(".")[-1].lower()

        if self.file_extension in ["csv", "txt"]:
            # Read CSV or text file
            df = pd.read_csv(self.file_name1)

            Time = df.iloc[:, 0].values

            Column_length = len(df.columns) - 1
            for i in range(Column_length):
                Signal_data.append(df.iloc[:, i + 1].values)
    
            self.saved_signal = np.sum(Signal_data, axis=0)
            penk=pg.mkPen('r',width=2)
            play_dynamically(self)
            #FourierTransform(self,self.saved_signal,Time,1)
            clearSpectrogram(self)
            #self.input.plot(Time, self.saved_signal, pen=penk, name='Saved Signal')
        elif self.file_extension == "wav":
            # Read WAV file
            
            # with wave.open(self.file_name1, 'rb') as wf:
            #     self.samplerate = wf.getframerate()
            #     frames = wf.readframes(-1)
            #     self.wav_data = np.frombuffer(frames, dtype=np.int16)
            self.sampling_frequency, self.saved_signal = wavfile.read(self.file_name1)
            print("__-----------------------___-_________________")
           # print(file_name1)
            # Ensure self.saved_signal is a 1D array
            if len(self.saved_signal.shape) > 1:
                # Take the first channel for simplicity (you can modify as needed)
                self.saved_signal = self.saved_signal[:, 0]

            Time = np.arange(0, len(self.saved_signal)) / self.sampling_frequency
            penk=pg.mkPen('r',width=2)
            #self.input.plot(Time.tolist(), self.saved_signal.tolist(), pen=penk, name='Saved Signal')
            plotType="wav"
            self.player = QMediaPlayer()
            
            media_content = QMediaContent(QUrl.fromLocalFile(self.file_name1))
            self.player.setMedia(QMediaContent())#%
            self.player.setMedia(media_content)
            self.player.play()
            resetSliderValues(self)
            #self.input.plot(Time.tolist(), self.saved_signal.tolist(), pen=penk, name='Saved Signal')
            play_dynamically(self)
            audioFourier(self,self.saved_signal)
            audioEqualizer(self)
            inverse_fft(self)
            clearSpectrogram(self)
            self.outputspectogram.canvas.drawspectrogram(self.normalized_signal,self.sampling_frequency)
            self.inputspectrogram.canvas.drawspectrogram(self.saved_signal,self.sampling_frequency)
            self.current_index = 0
            if counter>=1:
                 reset(self)
            counter+=1
        elif self.file_extension == "dat":
            data=[]
            Time=[]
            self.plot_data_all_x = []
            self.plot_data_all_y = []
            self.plot_data_all_youtput = []
            self.sampling_frequency=1
            self.current_index=0
            self.record = wfdb.rdrecord(self.file_name1[:-4], channels=[0])
            data = self.record.p_signal
            self.saved_signal = np.concatenate(data)
            

            for i in range(len(data)):
                Time.append(i/self.record.fs)

            # print(self.record.fs)
            self.sampling_frequency = self.record.fs
           # print(self.record.__dict__)

            self.input.clear()
            self.output.clear()
            #resetSliderValues(self)
            #if counter>=1:
                #reset(self)
            
            play_dynamically(self)
            audioFourier(self,self.saved_signal)
            audioEqualizer(self)
            inverse_fft(self)
            clearSpectrogram(self)
            resetSliderValues(self)
            self.outputspectogram.canvas.drawspectrogram(self.normalized_signal,self.sampling_frequency)
            self.inputspectrogram.canvas.drawspectrogram(self.saved_signal,self.sampling_frequency)
            counter+=1
        

def play_dynamically(self):
    # Ensure 'saved_signal' exists and is not empty
    if hasattr(self, 'saved_signal') and len(self.saved_signal) > 0:
        # Create a timer
        self.timer = QTimer()
        if self.file_extension=="wav":
            self.timer.start(1000)  # Adjust the interval as needed
        else :#%
            self.timer.start(1000)
        self.timer.timeout.connect(lambda:update_plot(self))

        # Set the interval for the timer (e.g., 100 milliseconds)
           

def update_plot(self):
    global loadedSignal
    
    if self.file_extension == "wav":
        # Check if the signal is still playing
        if hasattr(self, 'saved_signal') and len(self.saved_signal) > 0:
            # Plot the signal dynamically
            # Update Time if it's not already set for WAV files
           # if self.file_extension == "wav" and not hasattr(self, 'Time'):
            self.Time = np.arange(0, len(self.saved_signal)) / self.sampling_frequency
    
            # Ensure only one second is displayed at a time
            if not hasattr(self, 'current_index'):
                self.current_index = 0
            
            segment_length = int(self.sampling_frequency)
            end_index = self.current_index + segment_length
    
            if end_index >= len(self.saved_signal):
                end_index = len(self.saved_signal) - 1
    
            # Plot only the current second
            self.input.plot(self.Time[self.current_index:end_index].tolist(),
                            self.saved_signal[self.current_index:end_index].tolist())
    
            # Update the x-axis limits for viewing one second at a time
            self.input.setXRange(self.Time[self.current_index], self.Time[self.current_index] + 1)  #sets the range that is viewed with the updated signal so that the use only views one second
            self.output.plot(self.Time[self.current_index:end_index].tolist(),
                            self.normalized_signal[self.current_index:end_index].tolist())
    
            # Update the x-axis limits for viewing one second at a time
            self.output.setXRange(self.Time[self.current_index], self.Time[self.current_index] + 1)
            # Increment current index for the next segment
            self.current_index += segment_length
            
            # Check if the entire signal has been played
            if self.current_index >= len(self.saved_signal):
                # Stop the timer when the entire signal has been played
                self.timer.stop()


    elif self.file_extension == "csv" or self.file_extension == "dat":
           self.Time = np.arange(0, len(self.saved_signal))########################

           if not hasattr(self, 'current_index'):
               self.current_index = 0

          # print(self.current_index)
         
           segment_length = 1000  # Adjust the segment length as needed
           end_index = self.current_index + segment_length
       
           if end_index >= len(self.saved_signal):
               end_index = len(self.saved_signal)
       
           # Get the data for the segment to be plotted
           x_data = self.Time[self.current_index:end_index].tolist()
           y_data = self.saved_signal[self.current_index:end_index].tolist()
           y_output=self.normalized_signal[self.current_index:end_index].tolist()
           for i in range(len(y_output)):
                 if y_output[i]> 100 and y_output[i]<4000:
                       y_output[i] -= 900
                 #if y_output[i]> -8000 and y_output[i]<-1000:
                    #   y_output[i] += 2000
                 if y_output[i]> -1000 and y_output[i]<-16000:
                        y_output[i] += 14000
           #-500 4500
           if loadedSignal==3:
               for i in range(len(y_output)):
                     if y_output[i]> -500 and y_output[i]<4500:
                           y_output[i] -= 2000
          
           
           self.plot_data_all_x.extend(x_data)  # appends the data of the x and y every time we call the function so that the whole plot exists and is plotted while we use panning
           self.plot_data_all_y.extend(y_data)
           self.plot_data_all_youtput.extend(y_output)
        
           # Plot the initial segment
           self.plot_data = self.input.plot(x_data, y_data)
           self.input.setXRange(0, 10)
           self.plot_dataoutput = self.output.plot(x_data, y_output)
           self.output.setXRange(0, 10)
   
           # Update the existing plot data with the new segment
           self.plot_data.setData( self.plot_data_all_x,  self.plot_data_all_y)
           self.plot_dataoutput.setData( self.plot_data_all_x,  self.plot_data_all_youtput)  
           
           visible_x_range = [self.current_index,self.current_index+segment_length]
           self.input.setXRange(visible_x_range[0], visible_x_range[1])  # sets the view range with the range being plotted at that second
           self.output.setXRange(visible_x_range[0], visible_x_range[1])

           self.current_index = end_index
       
           if self.current_index >= len(self.saved_signal):
               self.timer.stop()
          

def audioFourier(self,saved_signal):
    global modified_magnitude
    global max_freqss
    n = len(saved_signal)
    normalize=n/2
    self.frequenciess = np.fft.rfftfreq(n, d=1/self.sampling_frequency)
    self.magnitude = np.abs((np.fft.rfft(saved_signal)))
    self.Smoothingraph.plot(self.frequenciess, self.magnitude)
   
    #self.Smoothinggraph.setXRange(0,int(max(self.max_freqss)))
    for i in range (len(self.frequenciess)):
        
        if self.frequenciess[i] and self.magnitude[i]>0.0000001:
           max_freqss.append(self.frequenciess[i])
 
   
def audioEqualizer(self):
    global counter
    if self.file_extension=="wav" and counter>1:
        self.player.pause()
    global max_freqss
    global freq_ranges
    global CurrentWindow
    global modified_magnitude
    global appliedWindow

   
    if self.magnitude is not None and self.frequenciess is not None:
        modified_magnitude = self.magnitude.copy()     
        freq_ranges,loopcount,mode=FreqRange(self)
   
   
        for i in range(loopcount):
            lower_bound = np.searchsorted(self.frequenciess, freq_ranges[i][0])
            upper_bound = np.searchsorted(self.frequenciess, freq_ranges[i][1])
   
            modified_magnitude[lower_bound:upper_bound] *= (self.slidersArray[mode][i].value()*appliedWindow) / 50
           
                
        self.frequencies.clear()
        self.frequencies.plot(self.frequenciess,modified_magnitude, pen='b')
        if callingWindow=="1":
            self.frequencies.setXRange(0,3000)
        self.Smoothingraph.clear()
        self.Smoothingraph.plot(self.frequenciess,modified_magnitude, pen='b')
        self.Smoothingraph.showGrid(True, True)
        #self.Smoothingraph.setXRange(0,5000)
        self.frequencies.setTitle("Frequency Domain")
        self.frequencies.setLabel('left', "Magnitude")
        self.frequencies.setLabel('bottom', "Frequency (Hz)")
        self.frequencies.showGrid(True, True)
        
       
def NormalizeSmoothingWindow(self):
    global modified_magnitude
    freq_range,loopcount,mode=FreqRange(self)

    lower_bound= np.searchsorted(self.frequenciess, freq_ranges[int(callingSlider)][0])
    upper_bound= np.searchsorted(self.frequenciess, freq_ranges[int(callingSlider)][1])
    start_indx=int(freq_range[int(callingSlider)][0])
    end_indx=int(freq_range[int(callingSlider)][1])
    segment = modified_magnitude[lower_bound:upper_bound]
    window_height=max(segment)

    return window_height,segment,start_indx,end_indx


def inverse_fft(self):
    
    if self.magnitude is not None and self.frequenciess is not None:
        freq_ranges,loopcount,mode=FreqRange(self)
        
        modified_complex_spectrum = np.zeros_like(self.magnitude) + 1j * np.zeros_like(self.magnitude)
        modified_regions=np.zeros_like(self.magnitude) + 1j * np.zeros_like(self.magnitude)
        for i in range(loopcount):
            lower_bound = np.searchsorted(self.frequenciess, freq_ranges[i][0])
            upper_bound = np.searchsorted(self.frequenciess, freq_ranges[i][1])
            modified_regions[lower_bound:upper_bound]=True
 
            modified_complex_spectrum[lower_bound:upper_bound] = self.magnitude[lower_bound:upper_bound] * \
                                                                 np.exp(1j * np.angle(np.fft.rfft(self.saved_signal)[lower_bound:upper_bound])) * \
                                                                 (self.slidersArray[mode][i].value() / 50)   
          
                                                                   
        unmodified_indices = np.logical_not(modified_regions)                                              
        original_complex_spectrum = self.magnitude * np.exp(1j * np.angle(np.fft.rfft(self.saved_signal)))
        modified_complex_spectrum[unmodified_indices] = original_complex_spectrum[unmodified_indices]
        
        modified_signal = np.fft.irfft(modified_complex_spectrum)
        # Normalize the signal if needed
        self.normalized_signal = np.int16( modified_signal / np.max(np.abs(modified_signal)) * 32767)
       
        self.outputspectogram.canvas.ax.cla()#5/12
        self.outputspectogram.canvas.drawspectrogram(self.normalized_signal,self.sampling_frequency)#5/12
        
def FreqRange(self):
    global callingSlider
    if callingWindow=="1":
        
        freq_rangesUniform=[
            (0,200),
            (200,400),
            (400,600),
            (600,800),
            (800,1000),
            (1000,1200),
            (1200,1400),
            (1400,1600),
            (1600,1800),
            (1800,22050)
            ]
        return freq_rangesUniform,10,0
    
    if callingWindow=="2":
        freq_rangesMusic = [
               (0, 400),    # Frequency range for slider 1  # instruments
               (400, 3000), # Frequency range for slider 2
               (3000, 4500),# Frequency range for slider 3
               (4500, 11000) # Frequency range for slider 4
           ]
        return freq_rangesMusic,4,1
    if callingWindow=="3":
        freq_rangesAnimals = [
               (100, 500),    # Frequency range for slider 1 Tiger 
               (700, 2500), # Frequency range for slider 2   Dolphin
               (2500, 4000),# Frequency range for slider 3   Eagle
               (4000, 7000) # Frequency range for slider 4   Birds
           ]
        return freq_rangesAnimals,4,2
    if callingWindow=="4":
        if callingSlider=="1":
            freq_rangesECG = [
                (0, 0),      # Frequency range for slider 1
                (0, 4),      # Frequency range for slider 2
                (2500, 3500),# Frequency range for slider 3
                (4000, 7000) # Frequency range for slider 4
            ]
            return freq_rangesECG,4,3
        if callingSlider=="2":
            freq_rangesECG = [
                (0, 0),      
                (2500, 3500),      
                (0, 8),
                (4000, 7000) 
            ]
            return freq_rangesECG,4,3
        if callingSlider=="3":
            freq_rangesECG = [
                (0, 0),      
                (4000, 7000),      
                (2500, 3500),
                (0, 9.8) 
            ]
            return freq_rangesECG,4,3

def savegraph(self): #saves the audio
  #  print(self.adjusted_fourier)
    self.player.play()
    #Getting the position of the audio being played
    self.playback_position = self.player.position()
    # Stop the player to release the file
    self.player.stop()
    self.timer.stop()
    self.player.setMedia(QMediaContent())  # Set media to null
    
    # Define the directory where modified WAV files will be saved
    output_directory = 'C:/Users/yi/Desktop/task3'
    #C:/Users/alia/Downloads/Task3AlmostThere/Task3Fix2.0/LatestFixWorkingWinodws
#C:/Users/alia/Downloads/Task3Edited/LatestFixWorkingWinodws/LatestFix
    # Create a unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    modified_wav_filename = f"mod_{timestamp}.wav"
    self.modified_wav_path = os.path.join(output_directory, modified_wav_filename)
    
    wavfile.write(self.modified_wav_path, self.sampling_frequency, self.normalized_signal)
    media_content = QMediaContent(QUrl.fromLocalFile(self.modified_wav_path))
    self.player.setMedia(media_content)
    self.player.setPosition(self.playback_position)  # Set the playback position
    self.player.play()
    self.timer.start(1000)



#These are the functions responsible for the buttons 

def Pause(self):
    global plotType
    if self.file_extension=="wav":
        self.player.pause()
    self.timer.stop()
def Play(self):
    global plotType
    if self.file_extension=="wav":
        self.player.play()
        self.timer.start(1000)
    if self.file_extension=="dat":
        self.timer.start(1000)
def playPause(self):
    global is_playing
    if is_playing:
        Pause(self)
        is_playing = False
    else:
        Play(self)
        is_playing = True
def Stop(self):
    global is_playing
    global plotType
    self.timer.stop()
    if self.file_extension=="wav":
        self.player.pause()
    is_playing=False
    
def updateCinespeed(self):
        speedfactor = self.cinespeed.value()/5.0
        timer_interval=int(1000/speedfactor)
        self.timer.setInterval(timer_interval)
    
def updatePlaybackSpeed(self):
        global plotType
        if plotType!='wav':
            return
        # Get the slider value for playback speed
        speed = self.cinespeed.value()/5.0    #division by 5 as the value slider is set in the interface at 5 so that 5/5 equals 1 and our max is upto 15 which is 15/5 is 3 so we can increase the speed by 3 
        # Set the playback rate based on the slider value
        self.player.setPlaybackRate(speed)
        

def zoom(self, factor):
    # Get the current ranges of the x-axis and y-axis
    current_x_range = self.input.viewRange()[0]
    current_y_range = self.input.viewRange()[1]

    # Calculate new x-axis and y-axis ranges based on the factor
    x_diff = (current_x_range[1] - current_x_range[0]) * factor  # It calculates the differences (x_diff and y_diff) between the current x-axis and y-axis ranges.
    y_diff = (current_y_range[1] - current_y_range[0]) * factor

    # Calculate the midpoint of the current y-axis range(To maintain the zero ofthe yaxis at the center)
    y_midpoint = (current_y_range[1] + current_y_range[0]) / 2

    new_x_range = [
        current_x_range[0] + x_diff / 2,
        current_x_range[1] - x_diff / 2
    ]

    # Calculate new y-axis ranges while maintaining zero at the center 
    if factor > 0:  # Zoom in
        new_y_min = y_midpoint - (y_midpoint - current_y_range[0]) * (1 + factor)
        new_y_max = y_midpoint + (current_y_range[1] - y_midpoint) * (1 + factor)
    else:  # Zoom out
        new_y_min = y_midpoint - (y_midpoint - current_y_range[0]) / (1 - factor)
        new_y_max = y_midpoint + (current_y_range[1] - y_midpoint) / (1 - factor)

    # Update the x-axis and y-axis ranges
    self.input.setXRange(*new_x_range)
    self.input.setYRange(new_y_min, new_y_max)
    self.output.setXRange(*new_x_range)
    self.output.setYRange(new_y_min, new_y_max)


def reset(self):
    global modified_magnitude
   

    if hasattr(self, 'timer'):
        self.timer.stop()  # Stop the current timer
    if self.file_extension == "wav":
        if hasattr(self, 'player'):
            self.player.setPosition(0)  # Restart sound playback from the beginning
    # Reset current_index to restart graph plotting from the beginning
    self.current_index = 0
    # Clear existing plots
    self.input.clear()
    self.output.clear()
    #reset time and audio with the original unmodified audio
    self.timer.stop()
    if self.file_extension == "wav":
        self.player.stop()
        self.player.setMedia(QMediaContent())
        media_content = QMediaContent(QUrl.fromLocalFile(self.file_name1))
        self.player.setMedia(media_content)
        self.player.play()
    if self.file_extension=="dat":
        self.plot_data_all_x = []
        self.plot_data_all_y = []
        self.plot_data_all_youtput = []
    # Start the timer again to update the plot dynamically
    self.timer.start(1000)  # Adjust the interval as needed
    self.timer.timeout.connect(lambda:play_dynamically(self))  # Connect timer to the update_plot function
    clearSpectrogram(self)
    resetSliderValues(self)
    audioFourier(self, self.saved_signal)
    audioEqualizer(self)
  
    
    self.inputspectrogram.canvas.drawspectrogram(self.saved_signal,self.sampling_frequency)
    self.outputspectogram.canvas.drawspectrogram(self.saved_signal,self.sampling_frequency)
    
def resetSliderValues(self):
    if callingWindow=="3":
        for i in range(len(self.animalSliders)):
             self.animalSliders[i].setValue(50)
    if callingWindow=="2":
        for i in range(len(self.musicSliders)):
            self.musicSliders[i].setValue(50)
    if callingWindow=="1":
        for i in range(len(self.uniformSliders)):
            self.uniformSliders[i].setValue(50)
    if callingWindow=="4":
        for i in range(len(self.ECGSliders)):
           self.ECGSliders[i].setValue(50)

   
    
        


def inputSound(self):
    if self.InputSound.isChecked():
        playback_position=clearPlayer(self)
        media_content = QMediaContent(QUrl.fromLocalFile(self.file_name1))
        setPlayerData(self,media_content,playback_position)
    
def outputSound(self):
    if self.OutputSound.isChecked():
        playback_position=clearPlayer(self)
        media_content = QMediaContent(QUrl.fromLocalFile(self.modified_wav_path))
        setPlayerData(self,media_content,playback_position)


def clearPlayer(self):
    playback_position = self.player.position()
    self.player.stop()
    self.player.setMedia(QMediaContent())
    return playback_position


def setPlayerData(self,media_content,playback_position):
    self.player.setMedia(media_content)
    self.player.setPosition(playback_position)  # Set the playback position
    self.player.play()
    
def clearSpectrogram(self):
    self.inputspectrogram.canvas.ax.cla()
    self.outputspectogram.canvas.ax.cla()
    
def showhideSpectroIn(self):
    if self.spectroInCheckBox.isChecked():
        self.inputspectrogram.show()
    else:
        self.inputspectrogram.hide()
 
    
def showhideSpectroOut(self):
    if self.spectroOutCheckBox.isChecked():
        self.outputspectogram.show()
    else:
        self.outputspectogram.hide()

#These functions are used for the Smoothing Window

def clearSmoothingGraph(self):
    self.Smoothingraph.clear()
    

def applyWindow(self):
    global CurrentWindow
    global appliedWindow
    appliedWindow=CurrentWindow

def chooseWindow(self,Window):
    global window
    window=Window

def SmoothingWindow(self):
    global frequency
    global normal_magnitude
    global CurrentWindow
    global modified_magnitude
    global chosenWindow
    window_height,bandwidth,start_indx,end_indx=NormalizeSmoothingWindow(self)
    length=int(end_indx-start_indx)
   
    self.Smoothingraph.clear()
    self.Smoothingraph.plot(self.frequenciess,modified_magnitude,pen='b')
    width = int((len(modified_magnitude[start_indx:end_indx])))
    if chosenWindow=="R":
        CurrentWindow = (boxcar(width))*window_height
        generalwindow=boxcar(50)
    elif chosenWindow=="n":
        CurrentWindow = hann(width)
        generalwindow=hann(50)
    elif chosenWindow=="m":
        CurrentWindow = hamming(width,sym=False)
        generalwindow=hamming(50)
    elif chosenWindow=="g":
         std = self.gaussianSliderStd.value()
         CurrentWindow = gaussian(width, std, sym=True)
         generalwindow =  gaussian(50,std,sym=True)
    CurrentWindow = CurrentWindow*window_height
    
    self.Smoothingraph.clear()
    self.Smoothingraph.plot(self.frequenciess,modified_magnitude,pen='b')
    x_values = np.arange(start_indx, start_indx+ len(CurrentWindow))
   
    self.freqWindow.clear()
    self.freqWindow.plot(generalwindow,pen='r')
    self.Smoothingraph.plot(x_values,CurrentWindow, pen='r')
    


def CallingSlider(self,call):
    global callingSlider
    callingSlider=call

def CallingWindow(self,calling):
    global callingWindow
    callingWindow=calling
  
def whichWindow(self,caller):
    global chosenWindow
    chosenWindow=caller

def chooseSmoothingWindow(self):
    global chosenWindow
    SmoothingWindow(self)



def on_tab_changed(self, index):
    if index == 0:  # Check if Tab 1 is selected uniform tab
        CallingWindow(self, "1")
    elif index == 1:  # Check if Tab 2 is selected Music tab
        CallingWindow(self, "2")
    elif index == 2:  # Check if Tab 3 is selected Animal tab
        CallingWindow(self, "3")
    elif index == 3:  # Check if Tab 4 is selected ECG tab
       CallingWindow(self, "4")



 #  self.Time = np.arange(0, len(self.saved_signal))########################

 #  if not hasattr(self, 'current_index'):
 #      self.current_index = 0

 # # print(self.current_index)

 #  segment_length = 10  # Adjust the segment length as needed
 #  end_index = self.current_index + segment_length

 #  if end_index >= len(self.saved_signal):
 #      end_index = len(self.saved_signal)

 #  # Get the data for the segment to be plotted
 #  x_data = self.Time[self.current_index:end_index].tolist()
 #  y_data = self.saved_signal[self.current_index:end_index].tolist()
 #  y_output=self.normalized_signal[self.current_index:end_index].tolist()
  
 #  self.plot_data_all_x.extend(x_data)  # appends the data of the x and y every time we call the function so that the whole plot exists and is plotted while we use panning
 #  self.plot_data_all_y.extend(y_data)
 #  self.plot_data_all_youtput.extend(y_output)

 #  # Plot the initial segment
 #  self.plot_data = self.input.plot(x_data, y_data)
 #  self.input.setXRange(0, 10)
 #  self.plot_dataoutput = self.output.plot(x_data, y_output)
 #  self.output.setXRange(0, 10)

 #  # Update the existing plot data with the new segment
 #  self.plot_data.setData( self.plot_data_all_x,  self.plot_data_all_y)
 #  self.plot_dataoutput.setData( self.plot_data_all_x,  self.plot_data_all_youtput)  
 #  if self.current_index<200:#%
 #      visible_x_range = [self.current_index,self.current_index+10*segment_length]
 #  else:
 #      visible_x_range = [self.current_index-300,self.current_index+10*segment_length]

 #  self.input.setXRange(visible_x_range[0], visible_x_range[1])  # sets the view range with the range being plotted at that second
 #  self.output.setXRange(visible_x_range[0], visible_x_range[1])

 #  self.current_index = end_index

 #  if self.current_index >= len(self.saved_signal):
 #      self.timer.stop()
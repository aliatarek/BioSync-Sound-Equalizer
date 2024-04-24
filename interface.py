from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton,QLCDNumber
from pyqtgraph import PlotWidget
#from mplwidget import MplWidget
import pyqtgraph
import Equalizer
from mplwidget import MplWidget
#from classes import channelLine




def initConnectors(self):
    
    self.tabWidget=self.findChild(QtWidgets.QTabWidget , "tabWidget") 

    self.tabWidget_2=self.findChild(QtWidgets.QTabWidget , "tabWidget_2")

    self.tab_3
    self.tab =self.findChild(QtWidgets.QWidget, "tab") 
    
    self.tab_2 = self.findChild(QtWidgets.QWidget,"tab_2")

    self.tab_3 = self.findChild(QtWidgets.QWidget,"tab_3")
    # Assuming self.tabWidget_2 is your QTabWidget
    self.tabWidget_2.currentChanged.connect(lambda index: Equalizer.on_tab_changed(self, index))
    # self.tab_4 = self.findChild(QtWidgets.QWidget,"tab_4")
    # self.tab_4.currentChanged.connect(lambda:Equalizer.CallingWindow(self, "2"))
    # self.tab_5 = self.findChild(QtWidgets.QWidget,"tab_5")
    # self.tab_5.currentChanged.connect(lambda:Equalizer.CallingWindow(self, "3"))
    # self.tab_6 = self.findChild(QtWidgets.QWidget,"tab_6")
    # self.tab_6.currentChanged.connect(lambda:Equalizer.CallingWindow(self, "4"))
    self.smoothingTabs= self.findChild(QtWidgets.QWidget,"smoothingTabs")

    self.horizontalLayout_2 = self.findChild(QtWidgets.QHBoxLayout, "horizontalLayout_2")

    self.Rectangle=self.findChild(QtWidgets.QRadioButton,"Rectangle")
    self.Rectangle.toggled.connect(lambda:Equalizer.whichWindow(self,"R"))
    # self.Rectangle.clicked.connect(lambda: Equalizer.callingWindow(self,"1"))
    # print(self.Rectangle)
    self.Hamming=self.findChild(QtWidgets.QRadioButton,"Hamming")
    self.Hamming.toggled.connect(lambda:Equalizer.whichWindow(self,"m"))
    # self.Hamming.clicked.connect(lambda: Equalizer.SmoothingandEqualizingFunction(self))
    # self.Hamming.clicked.connect(lambda: Equalizer.callingWindow(self,"3"))
    self.Hanning=self.findChild(QtWidgets.QRadioButton,"Hanning")
    self.Hanning.toggled.connect(lambda:Equalizer.whichWindow(self,"n"))
    # self.Hanning.clicked.connect(lambda: Equalizer.SmoothingandEqualizingFunction(self))
    # self.Hanning.clicked.connect(lambda: Equalizer.callingWindow(self,"2"))
    self.Gaussian=self.findChild(QtWidgets.QRadioButton,"Gaussian")
    self.Gaussian.toggled.connect(lambda:Equalizer.whichWindow(self,"g"))
    # self.Gaussian.clicked.connect(lambda: Equalizer.SmoothingandEqualizingFunction(self))
    # self.Gaussian.clicked.connect(lambda: Equalizer.callingWindow(self,"4"))
   # self.smoothingTabs.currentChanged.connect(lambda: Equalizer.clearSmoothingGraph(self))
    
   # self.hannTab=self.findChild(QtWidgets.QWidget,"hannTab")
    
    #self.hannTab.currentChanged.connect(lambda: Equalizer.clearSmoothingGraph(self))
    ##self.hammTab=self.findChild(QtWidgets.QWidget,"hammTab")
    #self.hammTab.currentChanged.connect(lambda: Equalizer.clearSmoothingGraph(self))

    ############################################ Uniform ######################################################
  
    self.uniformslider1=self.findChild(QtWidgets.QSlider , "uniformslider1")
    self.uniformslider1.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"0"))
    self.uniformslider1.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))
    self.uniformslider1.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.uniformslider1.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.uniformslider1.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.uniformslider1.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))
    
    # self.uniformslider1.valueChanged.connect(lambda: Equalizer.SliderValues(self,"1"))
    # self.uniformslider1.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"1"))
    # self.uniformslider1.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))

    self.uniformslider2=self.findChild(QtWidgets.QSlider , "uniformslider2")
    self.uniformslider2.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"1"))
    self.uniformslider2.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))
    self.uniformslider2.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.uniformslider2.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.uniformslider2.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.uniformslider2.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))

    # self.uniformslider2.valueChanged.connect(lambda: Equalizer.SliderValues(self,"1"))
    # self.uniformslider2.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"2"))
    # self.uniformslider2.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))

    self.uniformslider3=self.findChild(QtWidgets.QSlider , "uniformslider3")
    self.uniformslider3.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"2"))
    self.uniformslider3.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))
    self.uniformslider3.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.uniformslider3.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.uniformslider3.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.uniformslider3.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))
    # self.uniformslider3.valueChanged.connect(lambda: Equalizer.SliderValues(self,"1"))
    # self.uniformslider3.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"3"))
    # self.uniformslider3.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))

    self.uniformslider4=self.findChild(QtWidgets.QSlider , "uniformslider4")
    self.uniformslider4.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"3"))
    self.uniformslider4.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))
    self.uniformslider4.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.uniformslider4.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.uniformslider4.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.uniformslider4.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))
    # self.uniformslider4.valueChanged.connect(lambda: Equalizer.SliderValues(self,"1"))
    # self.uniformslider4.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"4"))
    # self.uniformslider4.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))

    self.uniformslider5=self.findChild(QtWidgets.QSlider , "uniformslider5")
    self.uniformslider5.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"4"))
    self.uniformslider5.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))
    self.uniformslider5.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.uniformslider5.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.uniformslider5.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.uniformslider5.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))
    # self.uniformslider5.valueChanged.connect(lambda: Equalizer.SliderValues(self,"1"))
    # self.uniformslider5.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"5"))
    # self.uniformslider5.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))

    self.uniformslider6=self.findChild(QtWidgets.QSlider , "uniformslider6")
    self.uniformslider6.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"5"))
    self.uniformslider6.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))
   # self.uniformslider6.valueChanged.connect(lambda: Equalizer.SliderValues(self,"1"))
    self.uniformslider6.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.uniformslider6.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.uniformslider6.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.uniformslider6.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))
    

    self.uniformslider7=self.findChild(QtWidgets.QSlider , "uniformslider7")
    self.uniformslider7.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"6"))
    self.uniformslider7.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))
    self.uniformslider7.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.uniformslider7.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.uniformslider7.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.uniformslider7.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))
    # self.uniformslider7.valueChanged.connect(lambda: Equalizer.SliderValues(self,"1"))
    # self.uniformslider7.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"7"))
    # self.uniformslider7.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))

    self.uniformslider8=self.findChild(QtWidgets.QSlider , "uniformslider8")
    self.uniformslider8.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"7"))
    self.uniformslider8.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))
    self.uniformslider8.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.uniformslider8.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.uniformslider8.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.uniformslider8.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))
    # self.uniformslider8.valueChanged.connect(lambda: Equalizer.SliderValues(self,"1"))
    # self.uniformslider8.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"8"))
    # self.uniformslider8.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))
   
    self.uniformslider9=self.findChild(QtWidgets.QSlider , "uniformslider9")
    self.uniformslider9.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"8"))
    self.uniformslider9.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))
    self.uniformslider9.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.uniformslider9.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.uniformslider9.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.uniformslider9.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))
    # self.uniformslider9.valueChanged.connect(lambda: Equalizer.SliderValues(self,"1"))
    # self.uniformslider9.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"9"))
    # self.uniformslider9.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))

    self.uniformslider10=self.findChild(QtWidgets.QSlider , "uniformslider10")
    self.uniformslider10.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"9"))
    self.uniformslider10.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))
    self.uniformslider10.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.uniformslider10.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.uniformslider10.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.uniformslider10.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))
    
    # self.uniformslider10.valueChanged.connect(lambda: Equalizer.SliderValues(self,"1"))
    # self.uniformslider10.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"10"))
    # self.uniformslider10.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"1"))
    
    self.uniformSliders=[]
    
    self.uniformSliders.append(self.uniformslider1)
    self.uniformSliders.append(self.uniformslider2)
    self.uniformSliders.append(self.uniformslider3)
    self.uniformSliders.append(self.uniformslider4)
    self.uniformSliders.append(self.uniformslider5)
    self.uniformSliders.append(self.uniformslider6)
    self.uniformSliders.append(self.uniformslider7)
    self.uniformSliders.append(self.uniformslider8)
    self.uniformSliders.append(self.uniformslider9)
    self.uniformSliders.append(self.uniformslider10)
    
    for i in range(len(self.uniformSliders)):
        self.uniformSliders[i].setMaximum(100)
        self.uniformSliders[i].setMinimum(0)
        self.uniformSliders[i].setValue(50)

     ###############################  ECG  ##################################

    self.ECGslider1=self.findChild(QtWidgets.QSlider , "ECGslider1")
    # self.ECGslider1.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"0"))
    # self.ECGslider1.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"4"))
    # self.ECGslider1.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    # self.ECGslider1.valueChanged.connect(lambda: Equalizer.inverse_fft(self))


    self.ECGslider2=self.findChild(QtWidgets.QSlider , "ECGslider2")
    #if lambda:Equalizer.returnECGfile(self)==1:
    self.ECGslider2.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"1"))
    self.ECGslider2.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"4"))
    self.ECGslider2.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.ECGslider2.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.ECGslider2.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))
  



    self.ECGslider3=self.findChild(QtWidgets.QSlider , "ECGslider3")
    #if lambda:Equalizer.returnECGfile(self)==2:
    self.ECGslider3.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"2"))
    self.ECGslider3.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"4"))
    self.ECGslider3.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.ECGslider3.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.ECGslider3.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))



    self.ECGslider4=self.findChild(QtWidgets.QSlider , "ECGslider4")
   # if lambda:Equalizer.returnECGfile(self)==3:
    self.ECGslider4.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"3"))
    self.ECGslider4.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"4"))
    self.ECGslider4.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.ECGslider4.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.ECGslider4.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))


    

    self.ECGSliders=[]

    self.ECGSliders.append(self.ECGslider1)
    self.ECGSliders.append(self.ECGslider2)
    self.ECGSliders.append(self.ECGslider3)
    self.ECGSliders.append(self.ECGslider4)

    for i in range(len(self.ECGSliders)):
       self.ECGSliders[i].setMaximum(100)
       self.ECGSliders[i].setMinimum(0)
       self.ECGSliders[i].setValue(50)


    ################################### Music #########################################
    
    self.musicslider1=self.findChild(QtWidgets.QSlider , "musicslider1")
    self.musicslider1.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"0"))
    self.musicslider1.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"2"))
    self.musicslider1.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.musicslider1.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.musicslider1.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.musicslider1.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))

    
    self.musicslider2=self.findChild(QtWidgets.QSlider , "musicslider2")
    self.musicslider2.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"1"))
    self.musicslider2.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"2"))
    self.musicslider2.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.musicslider2.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.musicslider2.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.musicslider2.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))


    
    self.musicslider3=self.findChild(QtWidgets.QSlider , "musicslider3")
    self.musicslider3.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"2"))
    self.musicslider3.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"2"))
    self.musicslider3.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.musicslider3.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.musicslider3.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.musicslider3.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))


    
    self.musicslider4=self.findChild(QtWidgets.QSlider , "musicslider4")
    self.musicslider4.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"3"))
    self.musicslider4.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"2"))
    self.musicslider4.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.musicslider4.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.musicslider4.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.musicslider4.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))



    self.musicSliders=[]
    self.musicSliders.append(self.musicslider1)
    self.musicSliders.append(self.musicslider2)
    self.musicSliders.append(self.musicslider3)
    self.musicSliders.append(self.musicslider4)
    
    for i in range(len(self.musicSliders)):
        self.musicSliders[i].setMaximum(100)
        self.musicSliders[i].setMinimum(0)
        self.musicSliders[i].setValue(50)

 ################################### Animals #########################################
    
    self.animalslider1=self.findChild(QtWidgets.QSlider , "animalslider1")
    self.animalslider1.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"0"))
    self.animalslider1.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"3"))
    self.animalslider1.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.animalslider1.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.animalslider1.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.animalslider1.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))

    
    self.animalslider2=self.findChild(QtWidgets.QSlider , "animalslider2")
    self.animalslider2.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"1"))
    self.animalslider2.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"3"))
    self.animalslider2.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.animalslider2.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.animalslider2.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.animalslider2.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))
    
    self.animalslider3=self.findChild(QtWidgets.QSlider , "animalslider3")
    self.animalslider3.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"2"))
    self.animalslider3.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"3"))
    self.animalslider3.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.animalslider3.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.animalslider3.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.animalslider3.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))
    
    self.animalslider4=self.findChild(QtWidgets.QSlider , "animalslider4")
    self.animalslider4.valueChanged.connect(lambda: Equalizer.CallingSlider(self,"3"))
    self.animalslider4.valueChanged.connect(lambda: Equalizer.CallingWindow(self,"3"))
    self.animalslider4.valueChanged.connect(lambda: Equalizer.audioEqualizer(self))
    self.animalslider4.valueChanged.connect(lambda: Equalizer.inverse_fft(self))
    self.animalslider4.valueChanged.connect(lambda: Equalizer.savegraph(self))
    self.animalslider4.valueChanged.connect(lambda: Equalizer.chooseSmoothingWindow(self))
    
    
    

    self.animalSliders=[]
    self.animalSliders.append(self.animalslider1)
    self.animalSliders.append(self.animalslider2)
    self.animalSliders.append(self.animalslider3)
    self.animalSliders.append(self.animalslider4)
     
    for i in range(len(self.animalSliders)):
         self.animalSliders[i].setMaximum(100)
         self.animalSliders[i].setMinimum(0)
         self.animalSliders[i].setValue(50)
    
    
    # for i in range(len(self.uniformSliders)-1):
    #     self.uniformSliders[i].setMaximum(100)
    #     self.uniformSliders[i].setMinimum(0)
    #     #self.uniformSliders[i].setValue(50)

    self.Smoothingraph=self.findChild(PlotWidget , "Smoothingraph")
    self.freqWindow=self.findChild(PlotWidget , "freqWindow")
    self.curve = self.Smoothingraph.plot(pen='r', name='Hanning Window')
    #self.hamming_curve = self.Smoothingraph.plot(pen='r', name='Hanning Window')
    self.tab_4 = self.findChild(QtWidgets.QWidget,"tab_4")

    self.hanningSlider1=self.findChild(QtWidgets.QSlider , "hanningSlider1")
  #  self.rectangleSlider1.setOrientation(0)  # Vertical orientation
    # self.hanningSlider1.setMinimum(1)
    # self.hanningSlider1.setMaximum(200)
    # self.hanningSlider1.setValue(5)
    #self.hanningSlider1.valueChanged.connect(lambda: Equalizer.Hanning(self))
    #self.hanningSlider2.setMinimum(0)
    #self.hanningSlider1.setMaximum(1)
    #self.hanningSlider1.setValue(0.56)
    #self.hanningSlider1.valueChanged.connect(lambda: Equalizer.Hanning(self))
    #self.verticalSlider_9.setMinimum(0)
    #self.verticalSlider_9.setMaximum(1)
    #self.verticalSlider_9.setValue(0.3)
    #self.verticalSlider_9.valueChanged.connect(lambda: Equalizer.Hanning(self))
   
    
    self.hammingSlider= self.findChild(QtWidgets.QSlider, "hammingSlider")
    # self.hammingSlider.setMinimum(1)
    # self.hammingSlider.setMaximum(200)
    # self.hammingSlider.setValue(5)
    #self.hammingSlider.valueChanged.connect(lambda: Equalizer.Hamming(self))
    
    
    self.rectangleSlider=self.findChild(QtWidgets.QSlider, "rectangleSlider")
    #self.rectangleSlider.setValue(5)
    #self.rectangleSlider.valueChanged.connect(lambda: Equalizer.Rectangular(self))
    
   
    # self.gaussianSliderMean.setMinimum(1)
    # self.gaussianSliderMean.setMaximum(100)
    # self.gaussianSliderMean.setValue(1)
    # self.gaussianSliderMean.valueChanged.connect(lambda: Equalizer.gaussianWindow(self))
    self.gaussianSliderStd=self.findChild(QtWidgets.QSlider, "gaussianSliderStd")
    self.gaussianSliderStd.setMinimum(1)
    self.gaussianSliderStd.setMaximum(30)
    self.gaussianSliderStd.setValue(1)
    self.gaussianSliderStd.valueChanged.connect(lambda: Equalizer.Gaussian(self))
    
    
   
   
    
    # self.gaussianSliderWidth.setMinimum(1)
    # self.gaussianSliderWidth.setMaximum(200)
    # self.gaussianSliderWidth.setValue(1)
    #self.gaussianSliderWidth.valueChanged.connect(lambda: Equalizer.Gaussian(self))
    self.tab_5 = self.findChild(QtWidgets.QWidget,"tab_5")

    self.tab_6 = self.findChild(QtWidgets.QWidget,"tab_6")
    
    self.gridLayout_2=self.findChild(QtWidgets.QGridLayout , "gridLayout_2") 
    
    
    #self.inputspectogram=self.findChild(PlotWidget , "inputspectogram") 
    #self.inputspectogram.setBackground('w')

    self.input=self.findChild(PlotWidget , "input") 
    #self.input.setBackground('w')


    self.output=self.findChild(PlotWidget , "output") 
    #self.output.setBackground('w')

    self.frequencies=self.findChild(PlotWidget,"frequencies")
    self.outputspectogram=self.findChild(MplWidget,"outputspectogram") 
    self.inputspectrogram=self.findChild(MplWidget,"inputspectrogram") 
    #self.outputspectogram.setBackground('w')
    
    
    self.playPause=self.findChild(QtWidgets.QPushButton, "playPause")
    self.playPause.clicked.connect(lambda: Equalizer.playPause(self))
    
    
    self.stop=self.findChild(QtWidgets.QPushButton, "stop")
    self.stop.clicked.connect(lambda: Equalizer.Stop(self))
    
    self.reset=self.findChild(QtWidgets.QPushButton, "reset")
    self.reset.clicked.connect(lambda: Equalizer.reset(self))
    self.zoomIn=self.findChild(QtWidgets.QPushButton, "zoomIn")
    self.zoomIn.clicked.connect(lambda: Equalizer.zoom(self,-0.5))
    
    
    self.zoomOut=self.findChild(QtWidgets.QPushButton, "zoomOut")
    self.zoomOut.clicked.connect(lambda: Equalizer.zoom(self,0.5))
    
    
    self.cinespeed=self.findChild(QtWidgets.QSlider , "cinespeed") 
    self.cinespeed.valueChanged.connect(lambda:Equalizer.updateCinespeed(self))
    self.cinespeed.valueChanged.connect(lambda:Equalizer.updatePlaybackSpeed(self))
    self.cinespeed.setRange(1,15)
    self.cinespeed.setValue(5)
    
    self.Load=self.findChild(QtWidgets.QPushButton, "Load")
    self.Load.clicked.connect(lambda: Equalizer.load_Signal(self))
    #self.Load.clicked.connect(lambda: Equalizer.spectrogram(self))
    
    
    
    self.InputSound=self.findChild(QtWidgets.QRadioButton, "inputSound")
    self.InputSound.toggled.connect(lambda:Equalizer.inputSound(self))
    self.InputSound.setChecked(False)
    self.OutputSound=self.findChild(QtWidgets.QRadioButton, "outputSound")
    self.OutputSound.toggled.connect(lambda:Equalizer.outputSound(self))
    self.OutputSound.setChecked(True)
    
    
    
    self.spectroInCheckBox=self.findChild(QtWidgets.QCheckBox, "spectroInCheckBox")
    self.spectroInCheckBox.stateChanged.connect(lambda:Equalizer.showhideSpectroIn(self))
    self.spectroOutCheckBox=self.findChild(QtWidgets.QCheckBox, "spectroOutCheckBox")
    self.spectroOutCheckBox.stateChanged.connect(lambda:Equalizer.showhideSpectroOut(self))
    
    
    self.slidersArray=[]
    self.slidersArray.append(self.uniformSliders)
    self.slidersArray.append(self.musicSliders)
    self.slidersArray.append(self.animalSliders)
    self.slidersArray.append(self.ECGSliders)
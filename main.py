from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox ,QSizePolicy
import pandas as pd
from scipy.io import loadmat
from fpdf import FPDF
import os
import pyqtgraph as pg
import pyqtgraph.exporters
import random
from PyQt5.QtCore import QTimer

class Ui_MainWindow(object):

    # Add the legend_items attribute
    legend_items = {}

    # dictinary stores files with its format
    filenames = dict()
    # dictinary stores files with its graph widget
    Current_File = dict()


    # a list of images of the graphs (use for create_pdf)
    image_list = []
    # flags for pause and stop functions
    isPaused = False
    isStoped = False
    # the length of data on a file
    dataLength = 0
    # stores number of the selected widget
    current_widget = []
    # intial graph range
    graph_rangeMin = [0, 0, 0]
    graph_rangeMax = [1000, 1000, 1000]
    speed = 1
    files = []
    selected_color = None

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 0, 28, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QtGui.QIcon("images/open.png"))
        self.pushButton.setIconSize(QtCore.QSize(28, 28))
        self.pushButton.setToolTip("open new signal file")

        # self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_2.setGeometry(QtCore.QRect(45, 0, 28, 28))
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_2.setIcon(QtGui.QIcon("images/show.png"))
        # self.pushButton_2.setIconSize(QtCore.QSize(28, 28))
        # self.pushButton_2.setToolTip("show")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 0, 28, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setIcon(QtGui.QIcon("images/hide.png"))
        self.pushButton_3.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_3.setToolTip("hide")

        # self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_4.setGeometry(QtCore.QRect(115, 0, 28, 28))
        # self.pushButton_4.setObjectName("pushButton_4")
        # self.pushButton_4.setIcon(QtGui.QIcon("images/color.png"))
        # self.pushButton_4.setIconSize(QtCore.QSize(28, 28))
        # self.pushButton_4.setToolTip("select color")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 0, 28, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setIcon(QtGui.QIcon("images/save.png"))
        self.pushButton_5.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_5.setToolTip("save the signal graph")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 0, 28, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setIcon(QtGui.QIcon("images/clear.png"))
        self.pushButton_6.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_6.setToolTip("clear the signal")

        # self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_7.setGeometry(QtCore.QRect(220, 0, 28, 28))
        # self.pushButton_7.setObjectName("pushButton_7")
        # self.pushButton_7.setIcon(QtGui.QIcon("images/start.jpg"))
        # self.pushButton_7.setIconSize(QtCore.QSize(28, 28))
        # self.pushButton_7.setToolTip("play the signal")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(170, 0, 28, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setIcon(QtGui.QIcon("images/stop.png"))
        self.pushButton_8.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_8.setToolTip("pause the signal")

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 0, 28, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setIcon(QtGui.QIcon("images/reset.png"))
        self.pushButton_9.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_9.setToolTip("restart the signal")

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(250, 0, 28, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setIcon(QtGui.QIcon("images/zoom-in.png"))
        self.pushButton_10.setIconSize(QtCore.QSize(33, 33))
        self.pushButton_10.setToolTip("Zoom In")

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(290, 0, 28, 28))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setIcon(QtGui.QIcon("images/zoom-out.png"))
        self.pushButton_11.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_11.setToolTip("Zoom Out")

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(330, 0, 28, 28))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.setIcon(QtGui.QIcon("images/right.png"))
        self.pushButton_12.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_12.setToolTip("Move Right")

        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(370, 0, 28, 28))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.setIcon(QtGui.QIcon("images/left.png"))
        self.pushButton_13.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_13.setToolTip("Move Left")

        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(410, 0, 28, 28))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.setIcon(QtGui.QIcon("images/speed.png"))
        self.pushButton_14.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_14.setToolTip("speed up")

        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(450, 0, 28, 28))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.setIcon(QtGui.QIcon("images/slow.png"))
        self.pushButton_15.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_15.setToolTip("slow down")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(490, 0, 90, 28))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.signals_combo = QtWidgets.QComboBox(self.centralwidget)
        self.signals_combo.setGeometry(QtCore.QRect(590, 0, 110, 28))
        self.signals_combo.setObjectName("signals_combobox")
        self.signals_combo.addItem("choose signal")

        self.Color_Signal = QtWidgets.QPushButton(self.centralwidget)
        self.Color_Signal.setGeometry(QtCore.QRect(710, 0, 80, 28))
        self.Color_Signal.setObjectName("Color_Signal")
        self.Color_Signal.setText("Color Signal")

        self.Move_Signal = QtWidgets.QPushButton(self.centralwidget)
        self.Move_Signal.setGeometry(QtCore.QRect(810, 0, 80, 28))
        self.Move_Signal.setObjectName("Move_Signal")
        self.Move_Signal.setText("Move Signal")

        self.Change_Label = QtWidgets.QLineEdit(self.centralwidget)
        self.Change_Label.setGeometry(QtCore.QRect(900, 0, 80, 28))
        self.Change_Label.setObjectName("Change_Label")
        self.Change_Label.setPlaceholderText("new label...")


        ##for style channel
        # Set fixed geometry for graphicsView
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")

        # Set fixed geometry for graphicsView_2
        self.graphicsView_2 = pg.PlotWidget(self.centralwidget)
        self.graphicsView_2.setObjectName("graphicsView_2")

        # Create a layout for the central widget
        central_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        central_layout.setContentsMargins(0, 40, 0, 0)  # Set top margin to 80

        # Set size policy and stretch factors for the widgets
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Allow widgets to expand
        self.graphicsView.setSizePolicy(size_policy)
        self.graphicsView_2.setSizePolicy(size_policy)

        # Add widgets to the layout with stretch factors
        central_layout.addWidget(self.graphicsView, 1)  # Stretch factor 1 allows the widget to expand
        central_layout.addWidget(self.graphicsView_2, 1)  # Stretch factor 1 allows the widget to expand

        # Set the central layout for the central widget
        self.centralwidget.setLayout(central_layout)

        # Set the central layout for the central widget
        self.centralwidget.setLayout(central_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 696, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #############



        # connecting each button by its function
        self.pushButton.clicked.connect(self.load_file)
        # self.pushButton_2.clicked.connect(self.show)
        self.pushButton_3.clicked.connect(self.hide)
        # self.pushButton_4.clicked.connect(self.select_color)

        self.pushButton_5.clicked.connect(self.export)
        self.pushButton_6.clicked.connect(self.clear)
        # self.pushButton_7.clicked.connect(self.start)
        self.pushButton_8.clicked.connect(self.pause)
        self.pushButton_9.clicked.connect(self.stop)
        self.pushButton_10.clicked.connect(self.zoom_in)
        self.pushButton_11.clicked.connect(self.zoom_out)
        self.pushButton_12.clicked.connect(self.move_right)
        self.pushButton_13.clicked.connect(self.move_left)
        self.pushButton_14.clicked.connect(self.speed_up)
        self.pushButton_15.clicked.connect(self.slow_down)

        self.Color_Signal.clicked.connect(self.color_signal)
        self.Move_Signal.clicked.connect(self.move_signal)
        self.Change_Label.returnPressed.connect(self.change_label)

        self.widget1 = self.graphicsView
        self.widget2 = self.graphicsView_2
        self.widgets = [self.widget1, self.widget2]

        #############
        # Add these lines in your __init__ method to initialize lists for combo box items
        # Add this line in your __init__ method to initialize a list for combo box items
        self.comboBox2_items = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", ""))
        self.pushButton.setShortcut(_translate("MainWindow", "Ctrl+L"))
        # self.pushButton_2.setText(_translate("MainWindow", ""))
        # self.pushButton_2.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.pushButton_3.setText(_translate("MainWindow", ""))
        self.pushButton_3.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.pushButton_5.setText(_translate("MainWindow", ""))
        self.pushButton_5.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_6.setText(_translate("MainWindow", ""))
        self.pushButton_6.setShortcut(_translate("MainWindow", "Ctrl+Shift+D"))
        # self.pushButton_7.setText(_translate("MainWindow", ""))
        # self.pushButton_7.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.pushButton_8.setText(_translate("MainWindow", ""))
        self.pushButton_8.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.pushButton_9.setText(_translate("MainWindow", ""))
        self.pushButton_9.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.pushButton_10.setText(_translate("MainWindow", "+"))
        self.pushButton_10.setShortcut(_translate("MainWindow", "Up"))
        self.pushButton_11.setText(_translate("MainWindow", "-"))
        self.pushButton_11.setShortcut(_translate("MainWindow", "Down"))
        self.pushButton_12.setText(_translate("MainWindow", "R"))
        self.pushButton_12.setShortcut(_translate("MainWindow", "Right"))
        self.pushButton_13.setText(_translate("MainWindow", "L"))
        self.pushButton_13.setShortcut(_translate("MainWindow", "Left"))
        self.pushButton_14.setText(_translate("MainWindow", ""))
        self.pushButton_14.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.pushButton_15.setText(_translate("MainWindow", ""))
        self.pushButton_15.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Widget1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Widget2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "link"))

    def load_file(self):
        # a function that loads the files data

        self.check_widget()
        self.filename, self.format = QtWidgets.QFileDialog.getOpenFileName(None, "Load Signal File", "",
                                                                           "*.csv;;" " *.txt;;" "*.mat")
        # checks if no file selected
        if self.filename == "":
            pass
        else:

            if self.current_widget not in self.Current_File:
                self.Current_File[self.current_widget] = []
            self.filenames[self.filename] = self.format
            self.Current_File[self.current_widget].append(self.filename)
            # print(self.filenames)
            # print(self.Current_File)
            #self.checkFileEXT(self.filenames)
            csv_file = pd.read_csv(self.filename).iloc[:, 1]
            # saves data length of the file
            self.widgets[self.current_widget].dataLength = csv_file.__len__()
            widget=self.current_widget
            # Add the signal name to the combobox
            self.signals_combo.addItem(self.filename.split("/")[-1])
            self.plot_here(csv_file, self.filename, widget)


    # def plot_here(self, file, fileName, widget):
    #     # the function that plots the graphs on the selected widget
    #
    #     label=(self.filename.split("/")[-1])
    #
    #     self.widgets[widget].plotItem.setTitle("Channel " + str(widget + 1))
    #
    #     # Check if the legend_items dictionary contains an entry for the current widget
    #     if widget not in self.legend_items:
    #         self.legend_items[widget] = {}
    #
    #     # Create a legend if not present
    #     if 'legend' not in self.legend_items[widget]:
    #         self.legend_items[widget]['legend'] = self.widgets[widget].plotItem.addLegend(size=(2, 3))
    #
    #     self.widgets[widget].plotItem.showGrid(True, True, alpha=1)
    #     self.widgets[widget].setXRange(0, 1000)
    #     self.widgets[widget].plotItem.setLabel("bottom", text="Time (ms)")
    #
    #     pen_color = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    #     pen = pg.mkPen(color=pen_color)
    #
    #     # Plot the signal and get the PlotDataItem
    #     plot_data_item = self.widgets[widget].plot(file, name=label, pen=pen)
    #
    #
    #
    #     self.start()
    def plot_here(self, file, fileName, widget):
        # the function that plots the graphs on the selected widget

        label = (fileName.split("/")[-1])

        self.widgets[widget].plotItem.setTitle("Channel " + str(widget + 1))

        # Check if the legend_items dictionary contains an entry for the current widget
        if widget not in self.legend_items:
            self.legend_items[widget] = {}

        # Create a legend if not present
        if 'legend' not in self.legend_items[widget]:
            self.legend_items[widget]['legend'] = self.widgets[widget].plotItem.addLegend(size=(2, 3))

        self.widgets[widget].plotItem.showGrid(True, True, alpha=1)

        # Calculate min and max values of the data
        min_time = min(file.index)
        max_time = max(file.index)
        min_signal = min(file)
        max_signal = max(file)

        # Set limits for the X and Y axes
        self.widgets[widget].plotItem.setLimits(xMin=min_time, xMax=max_time, yMin=min_signal, yMax=max_signal)

        self.widgets[widget].plotItem.setLabel("bottom", text="Time (ms)")

        pen_color = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pen = pg.mkPen(color=pen_color)

        # Plot the signal and get the PlotDataItem
        plot_data_item = self.widgets[widget].plot(file, name=label, pen=pen)

        self.start()
    def start(self):
        # the function that makes the graph start to move

        self.check_widget()
        self.isPaused = False
        self.isStopped = False

        if self.current_widget == 2:
            data_length = min(self.widget1.dataLength, self.widget2.dataLength)
            for x in range(data_length):
                self.widgets[0].setXRange(self.graph_rangeMin[0] + x * self.speed, self.graph_rangeMax[0] + x * self.speed)
                self.widgets[1].setXRange(self.graph_rangeMin[1] + x * self.speed, self.graph_rangeMax[1] + x * self.speed)
                QtWidgets.QApplication.processEvents()

                if self.isPaused:
                    self.graph_rangeMin[0] += x * self.speed
                    self.graph_rangeMax[0] += x * self.speed
                    self.graph_rangeMin[1] += x * self.speed
                    self.graph_rangeMax[1] += x * self.speed
                    break

                if self.isStopped:
                    break
        else:
            data_length = self.widgets[self.current_widget].dataLength

            for x in range(data_length):
                self.widgets[self.current_widget].setXRange(self.graph_rangeMin[self.current_widget] + x * self.speed,
                                                            self.graph_rangeMax[self.current_widget] + x * self.speed)
                QtWidgets.QApplication.processEvents()

                if self.isPaused:
                    self.graph_rangeMin[self.current_widget] += x * self.speed
                    self.graph_rangeMax[self.current_widget] += x * self.speed
                    break

                if self.isStopped:
                    break



    def color_signal(self):
        # the function that makes the graph start to move
        selected_signal = self.signals_combo.currentText()
        signal_path = self.get_signal_path(selected_signal)
        csv_file = pd.read_csv(signal_path).iloc[:, 1]


        signal_widget= self.get_widget( signal_path)

        color_dialog = QtWidgets.QColorDialog()
        color = color_dialog.getColor()

        # Check if a color was selected
        if color.isValid():
            items = self.widgets[signal_widget].getPlotItem().items

            # Iterate through items to find the PlotDataItem associated with the selected signal
            for item in items:
                if isinstance(item, pg.PlotDataItem) and item.name() == selected_signal:
                    # Set the new color
                    item.setPen(pg.mkPen(color))
                    break

        else:
            print("No color selected")

    def move_signal(self):
        selected_signal = self.signals_combo.currentText()
        signal_path = self.get_signal_path(selected_signal)
        signal_widget = self.get_widget(signal_path)
        target_widget=abs(signal_widget-1)

        # # Check if the selected signal is currently plotted on widget1 or widget2
        # if signal_widget == 0:
        #     target_widget = 1
        # elif signal_widget == 1:
        #     target_widget = 0


        # Get the current range of the source widget
        current_range_min = self.widgets[signal_widget].getViewBox().state['viewRange'][0][0]
        current_range_max = self.widgets[signal_widget].getViewBox().state['viewRange'][0][1]
        print(current_range_min)
        # removing the signal from the source widget
        items = self.widgets[signal_widget].getPlotItem().listDataItems()

        # Iterate through items to find the PlotDataItem associated with the selected signal
        for item in items:
            if isinstance(item, pg.PlotDataItem) and item.name() == selected_signal:
                # Remove the item from the widget
                self.widgets[signal_widget].getPlotItem().removeItem(item)
                break
        csv_file = pd.read_csv(signal_path).iloc[:, 1]
        #removing the path  corresponds to the old widget

        print(self.Current_File)

        self.Current_File[signal_widget].remove(signal_path)
        if target_widget not in self.Current_File:
            self.Current_File[target_widget] = []
            self.Current_File[target_widget].append(signal_path)
        else:
            self.Current_File[target_widget].append(signal_path)


        print(self.Current_File)

        #updating the current widget
        self.comboBox.setCurrentIndex(target_widget)
        # Plot the signal on the target widget starting from the current range
        self.plot_here(csv_file, signal_path, target_widget)
        self.widgets[signal_widget].setXRange(current_range_min, current_range_max)

        # Start the source widget again to ensure the signal continues moving

        # Set back the current view range for the target widget
        self.widgets[signal_widget].setXRange(current_range_min, current_range_max)


    def change_label(self):
        selected_signal = self.signals_combo.currentText()
        signal_path = self.get_signal_path(selected_signal)
        signal_widget = self.get_widget(signal_path)

        # Get the text from the QLineEdit
        new_label = self.Change_Label.text()
        # Clear the content of the QLineEdit
        self.Change_Label.clear()

        # Check if the signal_widget is a valid widget index
        if signal_widget is not None and signal_widget < len(self.widgets):
            # Find the PlotDataItem associated with the selected signal
            for item in self.widgets[signal_widget].items():
                if isinstance(item, pg.PlotDataItem) and item.name() == selected_signal:
                    # Update the legend entry with the new label
                    if signal_widget in self.legend_items and 'legend' in self.legend_items[signal_widget]:
                        self.legend_items[signal_widget]['legend'].removeItem(selected_signal)
                        self.legend_items[signal_widget]['legend'].addItem(item, new_label)

                    # Update the combobox entry with the new label
                    index = self.signals_combo.findText(selected_signal)


                    break  # Break out of the loop once the item is found

    def get_signal_path(self, signal_name):
        # Search for the signal name across all widgets in Current_File
        for widget_signals in self.Current_File.values():
            for signal_path in widget_signals:
                if signal_name in signal_path:
                    return signal_path

        # Handle the case when the signal name is not found
        return None

    def get_widget(self, signal_path):
        for widget, signal_paths in self.Current_File.items():
            if signal_path in signal_paths:
                # Now 'widget' contains the corresponding widget
                return widget
        return 0

    def clear(self):
        # A function that clears a graph and deletes its file

        self.check_widget()

        if self.current_widget is None:
            # Clear both widgets
            for widget in self.widgets:
                widget.clear()
                widget.plotItem.showGrid(False, False)

                self.stop()
                if widget in self.Current_File:
                    # Delete the file from filenames dict and current_file dict
                    del self.filenames[self.Current_File[widget]]
                    del self.Current_File[widget]

        else:
            # Clear the selected widget
            self.widgets[self.current_widget].clear()
            self.widgets[self.current_widget].plotItem.showGrid(False, False)
            self.stop()
            if self.widgets[self.current_widget] in self.Current_File:
                # Delete the file from filenames dict and current_file dict
                del self.filenames[self.Current_File[self.widgets[self.current_widget]]]
                del self.Current_File[self.widgets[self.current_widget]]

    def hide(self):
        self.check_widget()
        self.widgets[self.current_widget].setVisible(False)

    def show(self):
        self.check_widget()
        self.widgets[self.current_widget].setVisible(True)

    #
    def zoom(self):
        # u can zoom and move in any direction
        self.check_widget()
        if self.current_widget !=2:
            self.widgets[self.current_widget].plotItem.setMouseEnabled(y=True, x=True)

        else:
            self.widgets[0].plotItem.setMouseEnabled(y=True, x=True)
            self.widgets[1].plotItem.setMouseEnabled(y=True, x=True)




    def export(self):
        # a function that creates a pictures of the drawn graphs

        exporter1 = pg.exporters.ImageExporter(self.graphicsView.plotItem)
        exporter1.export('fileName1.png')
        exporter2 = pg.exporters.ImageExporter(self.graphicsView_2.plotItem)
        exporter2.export('fileName2.png')

        # stores the pictures files in image list
        self.image_list = ['fileName1.png', 'fileName2.png']
        self.create_pdf()


    def create_pdf(self):
        # the function that creates the pdf report

        pdf = FPDF()

        for x in range(2):
            # set pdf title
            pdf.add_page()
            pdf.set_font('Arial', 'B', 15)
            pdf.cell(70)
            pdf.cell(60, 10, 'Siganl Viewer Report', 1, 0, 'C')
            pdf.ln(20)

            # put the graphs on the pdf
            pdf.image(self.image_list[x], 10, 50, 190, 50)

        pdf.output("report.pdf", "F")

        # removes the graphs pictures as we dont need
        os.remove("fileName1.png")
        os.remove("fileName2.png")


    def check_widget(self):
        if self.comboBox.currentText() == "Widget1":
            self.current_widget = 0
        elif self.comboBox.currentText() == "Widget2":
            self.current_widget = 1
        elif self.comboBox.currentText() == "link":
            self.current_widget = 2

    def select_color(self):

        color = QtWidgets.QColorDialog.getColor()  # Open QColorDialog
        if color.isValid():
            # Store the selected color value
            self.selected_color = color



    def speed_up(self):
        self.check_widget()
        self.speed *= 2

    def slow_down(self):
        self.check_widget()
        self.speed /= 2


    def pause(self):
        self.check_widget()
        self.isPaused = True

    def stop(self):
        # the function that restart the graph

        self.check_widget()

        if self.current_widget is None:
            # Stop both widgets
            self.isStopped = True
            for widget in self.widgets:
                widget.setXRange(0, 1000)
            self.graph_rangeMin = [0, 0]
            self.graph_rangeMax = [1000, 1000]

        elif self.current_widget in [0, 1]:
            # Stop the selected widget
            self.isStopped = True
            widget_index = self.current_widget
            self.widgets[widget_index].setXRange(0, 1000)
            self.graph_rangeMin[widget_index] = 0
            self.graph_rangeMax[widget_index] = 1000






            self.widgets[self.current_widget].plotItem.getViewBox().scaleBy(x=0.5, y=1)  # Zoom in the selected widget
    def zoom_in(self):

        self.check_widget()  # Corrected method call
        if self.current_widget == 2:
            for widget in self.widgets:
                widget.plotItem.getViewBox().scaleBy(x=0.5, y=1)  # Zoom in both widgets
        else:
            self.widgets[self.current_widget].plotItem.getViewBox().scaleBy(x=0.5, y=1)  # Zoom in the selected widget





    def zoom_out(self):
        self.check_widget()  # Corrected method call
        if self.current_widget == 2:
            for widget in self.widgets:
                widget.plotItem.getViewBox().scaleBy(x=2, y=1)  # Zoom out both widgets
        else:
            self.widgets[self.current_widget].plotItem.getViewBox().scaleBy(x=2, y=1)  # Zoom out the selected widget

    def move_right(self):
        self.check_widget
        self.widgets[self.current_widget].setXRange(self.graph_rangeMin[self.current_widget] + 100,
                                                    self.graph_rangeMax[self.current_widget] + 100)

        self.graph_rangeMin[self.current_widget] = self.graph_rangeMin[self.current_widget] + 100
        self.graph_rangeMax[self.current_widget] = self.graph_rangeMax[self.current_widget] + 100

    def move_left(self):
        self.check_widget
        self.widgets[self.current_widget].setXRange(self.graph_rangeMin[self.current_widget] - 100,
                                                    self.graph_rangeMax[self.current_widget] - 100)

        self.graph_rangeMin[self.current_widget] = self.graph_rangeMin[self.current_widget] - 100
        self.graph_rangeMax[self.current_widget] = self.graph_rangeMax[self.current_widget] - 100




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
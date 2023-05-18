import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import ( QApplication, QMainWindow, QWidget,
                             QHBoxLayout,QVBoxLayout,QLabel,QSpinBox,
                             QDoubleSpinBox,QPushButton,QLineEdit,
                             QComboBox)
from PyQt6.QtGui import QPalette, QColor

DISTANCES = {
    "Choose Location": 0,
    "Sun": 93900000,
    "Mercury": 55357000,
    "Venus": 82762000,
    "Mars": 172120000,
    "Ceres": 257000000,
    "Jupiter": 545630000,
    "Saturn": 982750000,
    "Uranus": 1919700000,
    "Neptune": 2832500000,
    "Pluto": 3195800000,
    "Makemake": 3486000000,   
    "Haumea": 4577100000,
    "Eris": 8983400000
}

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(300,250))
        layout = QVBoxLayout()
    
        title_label = QLabel("Light Speed Calculator")
        layout.addWidget(title_label)

        main_pane = QHBoxLayout()

        # Left pane inputs
        left_pane = QVBoxLayout()
        speed_label = QLabel("Speed")
        self.speed_input = QSpinBox()
        distance_label = QLabel("Distance")
        self.distance_input = QDoubleSpinBox()
        self.locations_input = QComboBox()
        self.locations_input.addItems(DISTANCES.keys())
        self.locations_input.currentTextChanged.connect(self.get_location)
        time_label = QLabel("Time")
        self.time_output = QDoubleSpinBox()        
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)

        left_pane.addWidget(speed_label)
        left_pane.addWidget(self.speed_input)
        self.speed_input.setRange(186000,186000)
        left_pane.addWidget(distance_label) 
        left_pane.addWidget(self.distance_input)
        self.distance_input.setRange(0,9999999999)
        left_pane.addWidget(self.locations_input)
        left_pane.addWidget(time_label)
        left_pane.addWidget(self.time_output)
        self.time_output.setRange(0,9999999999)
        left_pane.addWidget(self.calculate_button)

        # Right pane inputs
        right_pane = QVBoxLayout()
        output_box = QLineEdit()
        output_box.setMaximumHeight(100)
        output_box.setMaximumWidth(150)
        output_box.setPlaceholderText("Results")

        right_pane.addWidget(output_box)
          

        main_pane.addLayout(left_pane)
        main_pane.addLayout(right_pane)
        layout.addLayout(main_pane)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    # An attempt to make the push button calculate
    def divide(x, y):
        return x / y
    num1 = 
    num2 = 
    if():
        print(num1, "/", num2, "=", divide(num1, num2))
    # End of attempt
    def convert_time(time):
        day = time // (24 * 3600)
        time = time % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        return "d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds)

    def calculate(self):
        distance=self.distance_input.text()
        print(distance)

    def get_location(self):
        location = self.locations_input.currentText()
        distance = DISTANCES.get(location)
        self.distance_input.setValue(distance)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# Form implementation generated from reading ui file '/Users/isaac/My Drive/Documents/Programming/Projects/lift-control-simulation/src/ui/main_menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mwindow_main_menu(object):
    def setupUi(self, mwindow_main_menu):
        mwindow_main_menu.setObjectName("mwindow_main_menu")
        mwindow_main_menu.resize(600, 300)
        font = QtGui.QFont()
        font.setPointSize(10)
        mwindow_main_menu.setFont(font)
        self.central_widget = QtWidgets.QWidget(mwindow_main_menu)
        self.central_widget.setObjectName("central_widget")
        self.layoutWidget = QtWidgets.QWidget(self.central_widget)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 564, 265))
        self.layoutWidget.setObjectName("layoutWidget")
        self.vert_layout_lift_control = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.vert_layout_lift_control.setContentsMargins(0, 0, 0, 0)
        self.vert_layout_lift_control.setObjectName("vert_layout_lift_control")
        self.lbl_lift_control = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.lbl_lift_control.setFont(font)
        self.lbl_lift_control.setObjectName("lbl_lift_control")
        self.vert_layout_lift_control.addWidget(self.lbl_lift_control)
        self.hori_line_lift_control = QtWidgets.QFrame(self.layoutWidget)
        self.hori_line_lift_control.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.hori_line_lift_control.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hori_line_lift_control.setObjectName("hori_line_lift_control")
        self.vert_layout_lift_control.addWidget(self.hori_line_lift_control)
        self.hori_layout_nav = QtWidgets.QHBoxLayout()
        self.hori_layout_nav.setObjectName("hori_layout_nav")
        self.btn_config_sim = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_config_sim.setObjectName("btn_config_sim")
        self.hori_layout_nav.addWidget(
            self.btn_config_sim, 0, QtCore.Qt.AlignmentFlag.AlignLeft
        )
        self.vert_line_buttons = QtWidgets.QFrame(self.layoutWidget)
        self.vert_line_buttons.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.vert_line_buttons.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.vert_line_buttons.setObjectName("vert_line_buttons")
        self.hori_layout_nav.addWidget(self.vert_line_buttons)
        self.btn_open_sim = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_open_sim.setObjectName("btn_open_sim")
        self.hori_layout_nav.addWidget(
            self.btn_open_sim, 0, QtCore.Qt.AlignmentFlag.AlignLeft
        )
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.hori_layout_nav.addItem(spacerItem)
        self.vert_layout_lift_control.addLayout(self.hori_layout_nav)
        self.hori_line_nav = QtWidgets.QFrame(self.layoutWidget)
        self.hori_line_nav.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.hori_line_nav.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hori_line_nav.setObjectName("hori_line_nav")
        self.vert_layout_lift_control.addWidget(self.hori_line_nav)
        self.lbl_current_config = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.lbl_current_config.setFont(font)
        self.lbl_current_config.setObjectName("lbl_current_config")
        self.vert_layout_lift_control.addWidget(self.lbl_current_config)
        self.lbl_num_floors = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_num_floors.setObjectName("lbl_num_floors")
        self.vert_layout_lift_control.addWidget(self.lbl_num_floors)
        self.lbl_num_people = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_num_people.setObjectName("lbl_num_people")
        self.vert_layout_lift_control.addWidget(self.lbl_num_people)
        self.lbl_lift_capacity = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_lift_capacity.setObjectName("lbl_lift_capacity")
        self.vert_layout_lift_control.addWidget(self.lbl_lift_capacity)
        self.lbl_ui_delay = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_ui_delay.setObjectName("lbl_ui_delay")
        self.vert_layout_lift_control.addWidget(self.lbl_ui_delay)
        self.hori_line_config = QtWidgets.QFrame(self.layoutWidget)
        self.hori_line_config.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.hori_line_config.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hori_line_config.setObjectName("hori_line_config")
        self.vert_layout_lift_control.addWidget(self.hori_line_config)
        self.lbl_instruction = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lbl_instruction.setFont(font)
        self.lbl_instruction.setObjectName("lbl_instruction")
        self.vert_layout_lift_control.addWidget(self.lbl_instruction)
        spacerItem1 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vert_layout_lift_control.addItem(spacerItem1)
        mwindow_main_menu.setCentralWidget(self.central_widget)

        self.retranslateUi(mwindow_main_menu)
        QtCore.QMetaObject.connectSlotsByName(mwindow_main_menu)

    def retranslateUi(self, mwindow_main_menu):
        _translate = QtCore.QCoreApplication.translate
        mwindow_main_menu.setWindowTitle(
            _translate("mwindow_main_menu", "Lift Control Simulation – Main Menu")
        )
        self.lbl_lift_control.setText(
            _translate("mwindow_main_menu", "Lift Control Simulation – Main Menu")
        )
        self.btn_config_sim.setText(
            _translate("mwindow_main_menu", "Configure Simulation")
        )
        self.btn_open_sim.setText(_translate("mwindow_main_menu", "Open Simulation"))
        self.lbl_current_config.setText(
            _translate("mwindow_main_menu", "Current Configuration")
        )
        self.lbl_num_floors.setText(
            _translate("mwindow_main_menu", "Number of Floors: ")
        )
        self.lbl_num_people.setText(
            _translate("mwindow_main_menu", "Number of People: ")
        )
        self.lbl_lift_capacity.setText(
            _translate("mwindow_main_menu", "Lift Capacity: ")
        )
        self.lbl_ui_delay.setText(
            _translate("mwindow_main_menu", "UI Delay (Milliseconds): ")
        )
        self.lbl_instruction.setText(
            _translate(
                "mwindow_main_menu",
                "Machine Learning Project Review \n21BCE1779\n21BCE1125\n21BCE1059",
            )
        )

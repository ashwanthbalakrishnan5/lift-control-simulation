# Form implementation generated from reading ui file '/Users/isaac/My Drive/Documents/Programming/Projects/lift-control-simulation/src/ui/sim_5_floors.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mwindow_sim_5_floors(object):
    def setupUi(self, mwindow_sim_5_floors):
        mwindow_sim_5_floors.setObjectName("mwindow_sim_5_floors")
        mwindow_sim_5_floors.resize(650, 450)
        font = QtGui.QFont()
        font.setPointSize(10)
        mwindow_sim_5_floors.setFont(font)
        self.central_widget = QtWidgets.QWidget(mwindow_sim_5_floors)
        self.central_widget.setObjectName("central_widget")
        self.layoutWidget = QtWidgets.QWidget(self.central_widget)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 611, 418))
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
        self.btn_generate_new_sim = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_generate_new_sim.setObjectName("btn_generate_new_sim")
        self.hori_layout_nav.addWidget(self.btn_generate_new_sim)
        self.vert_line_buttons = QtWidgets.QFrame(self.layoutWidget)
        self.vert_line_buttons.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.vert_line_buttons.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.vert_line_buttons.setObjectName("vert_line_buttons")
        self.hori_layout_nav.addWidget(self.vert_line_buttons)
        self.btn_run_sim_naive = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_run_sim_naive.setObjectName("btn_run_sim_naive")
        self.hori_layout_nav.addWidget(
            self.btn_run_sim_naive, 0, QtCore.Qt.AlignmentFlag.AlignLeft
        )
        self.btn_run_sim_improved = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_run_sim_improved.setObjectName("btn_run_sim_improved")
        self.hori_layout_nav.addWidget(self.btn_run_sim_improved)
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
        self.lbl_num_delivered = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_num_delivered.setObjectName("lbl_num_delivered")
        self.vert_layout_lift_control.addWidget(self.lbl_num_delivered)
        self.lbl_distance_travelled = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_distance_travelled.setObjectName("lbl_distance_travelled")
        self.vert_layout_lift_control.addWidget(self.lbl_distance_travelled)
        self.hori_line_summary = QtWidgets.QFrame(self.layoutWidget)
        self.hori_line_summary.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.hori_line_summary.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hori_line_summary.setObjectName("hori_line_summary")
        self.vert_layout_lift_control.addWidget(self.hori_line_summary)
        self.grid_layout_sim = QtWidgets.QGridLayout()
        self.grid_layout_sim.setObjectName("grid_layout_sim")
        self.lbl_delivered_2 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_delivered_2.setObjectName("lbl_delivered_2")
        self.grid_layout_sim.addWidget(self.lbl_delivered_2, 3, 1, 1, 1)
        self.lbl_floor_0 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_floor_0.setObjectName("lbl_floor_0")
        self.grid_layout_sim.addWidget(self.lbl_floor_0, 5, 2, 1, 1)
        self.lbl_floor_3 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_floor_3.setObjectName("lbl_floor_3")
        self.grid_layout_sim.addWidget(self.lbl_floor_3, 2, 2, 1, 1)
        self.lbl_delivered_floors = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.lbl_delivered_floors.setFont(font)
        self.lbl_delivered_floors.setObjectName("lbl_delivered_floors")
        self.grid_layout_sim.addWidget(self.lbl_delivered_floors, 0, 1, 1, 1)
        self.lbl_delivered_4 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_delivered_4.setObjectName("lbl_delivered_4")
        self.grid_layout_sim.addWidget(self.lbl_delivered_4, 1, 1, 1, 1)
        self.lbl_floor_1 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_floor_1.setObjectName("lbl_floor_1")
        self.grid_layout_sim.addWidget(self.lbl_floor_1, 4, 2, 1, 1)
        self.lbl_waiting_floors = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.lbl_waiting_floors.setFont(font)
        self.lbl_waiting_floors.setObjectName("lbl_waiting_floors")
        self.grid_layout_sim.addWidget(self.lbl_waiting_floors, 0, 0, 1, 1)
        self.lbl_waiting_0 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_waiting_0.setObjectName("lbl_waiting_0")
        self.grid_layout_sim.addWidget(self.lbl_waiting_0, 5, 0, 1, 1)
        self.lbl_lift_floors = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.lbl_lift_floors.setFont(font)
        self.lbl_lift_floors.setObjectName("lbl_lift_floors")
        self.grid_layout_sim.addWidget(self.lbl_lift_floors, 0, 2, 1, 1)
        self.lbl_floor_2 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_floor_2.setObjectName("lbl_floor_2")
        self.grid_layout_sim.addWidget(self.lbl_floor_2, 3, 2, 1, 1)
        self.lbl_waiting_1 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_waiting_1.setObjectName("lbl_waiting_1")
        self.grid_layout_sim.addWidget(self.lbl_waiting_1, 4, 0, 1, 1)
        self.lbl_waiting_3 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_waiting_3.setObjectName("lbl_waiting_3")
        self.grid_layout_sim.addWidget(self.lbl_waiting_3, 2, 0, 1, 1)
        self.lbl_delivered_0 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_delivered_0.setObjectName("lbl_delivered_0")
        self.grid_layout_sim.addWidget(self.lbl_delivered_0, 5, 1, 1, 1)
        self.lbl_waiting_2 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_waiting_2.setObjectName("lbl_waiting_2")
        self.grid_layout_sim.addWidget(self.lbl_waiting_2, 3, 0, 1, 1)
        self.lbl_floor_4 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_floor_4.setObjectName("lbl_floor_4")
        self.grid_layout_sim.addWidget(self.lbl_floor_4, 1, 2, 1, 1)
        self.lbl_delivered_3 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_delivered_3.setObjectName("lbl_delivered_3")
        self.grid_layout_sim.addWidget(self.lbl_delivered_3, 2, 1, 1, 1)
        self.lbl_waiting_4 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_waiting_4.setObjectName("lbl_waiting_4")
        self.grid_layout_sim.addWidget(self.lbl_waiting_4, 1, 0, 1, 1)
        self.lbl_delivered_1 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_delivered_1.setObjectName("lbl_delivered_1")
        self.grid_layout_sim.addWidget(self.lbl_delivered_1, 4, 1, 1, 1)
        self.vert_layout_lift_control.addLayout(self.grid_layout_sim)
        self.lbl_key = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lbl_key.setFont(font)
        self.lbl_key.setObjectName("lbl_key")
        self.vert_layout_lift_control.addWidget(self.lbl_key)
        self.hori_line_sim = QtWidgets.QFrame(self.layoutWidget)
        self.hori_line_sim.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.hori_line_sim.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.hori_line_sim.setObjectName("hori_line_sim")
        self.vert_layout_lift_control.addWidget(self.hori_line_sim)
        self.lbl_num_in_lift = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_num_in_lift.setObjectName("lbl_num_in_lift")
        self.vert_layout_lift_control.addWidget(self.lbl_num_in_lift)
        self.lbl_update = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_update.setText("")
        self.lbl_update.setObjectName("lbl_update")
        self.vert_layout_lift_control.addWidget(self.lbl_update)
        spacerItem1 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.vert_layout_lift_control.addItem(spacerItem1)
        mwindow_sim_5_floors.setCentralWidget(self.central_widget)

        self.retranslateUi(mwindow_sim_5_floors)
        QtCore.QMetaObject.connectSlotsByName(mwindow_sim_5_floors)

    def retranslateUi(self, mwindow_sim_5_floors):
        _translate = QtCore.QCoreApplication.translate
        mwindow_sim_5_floors.setWindowTitle(
            _translate("mwindow_sim_5_floors", "Lift Control Simulation – 5 Floors")
        )
        self.lbl_lift_control.setText(
            _translate("mwindow_sim_5_floors", "Lift Control Simulation – 5 Floors")
        )
        self.btn_generate_new_sim.setText(
            _translate("mwindow_sim_5_floors", "Generate New Simulation")
        )
        self.btn_run_sim_naive.setText(
            _translate("mwindow_sim_5_floors", "Run Simulation (Improved)")
        )
        self.btn_run_sim_improved.setText(
            _translate("mwindow_sim_5_floors", "Run Simulation (Naive)")
        )
        self.lbl_num_delivered.setText(
            _translate("mwindow_sim_5_floors", "Number of People Delivered: 0")
        )
        self.lbl_distance_travelled.setText(
            _translate("mwindow_sim_5_floors", "Total Distance Travelled: 0")
        )
        self.lbl_delivered_2.setText(_translate("mwindow_sim_5_floors", "0"))
        self.lbl_floor_0.setText(_translate("mwindow_sim_5_floors", "0"))
        self.lbl_floor_3.setText(_translate("mwindow_sim_5_floors", "0"))
        self.lbl_delivered_floors.setText(
            _translate("mwindow_sim_5_floors", "Number of People Delivered:")
        )
        self.lbl_delivered_4.setText(_translate("mwindow_sim_5_floors", "0"))
        self.lbl_floor_1.setText(_translate("mwindow_sim_5_floors", "0"))
        self.lbl_waiting_floors.setText(
            _translate("mwindow_sim_5_floors", "Number of People Waiting:")
        )
        self.lbl_waiting_0.setText(_translate("mwindow_sim_5_floors", "0"))
        self.lbl_lift_floors.setText(_translate("mwindow_sim_5_floors", "Lift Floors:"))
        self.lbl_floor_2.setText(_translate("mwindow_sim_5_floors", "0"))
        self.lbl_waiting_1.setText(_translate("mwindow_sim_5_floors", "0"))
        self.lbl_waiting_3.setText(_translate("mwindow_sim_5_floors", "0"))
        self.lbl_delivered_0.setText(_translate("mwindow_sim_5_floors", "0"))
        self.lbl_waiting_2.setText(_translate("mwindow_sim_5_floors", "0"))
        self.lbl_floor_4.setText(_translate("mwindow_sim_5_floors", "0"))
        self.lbl_delivered_3.setText(_translate("mwindow_sim_5_floors", "0"))
        self.lbl_waiting_4.setText(_translate("mwindow_sim_5_floors", "0"))
        self.lbl_delivered_1.setText(_translate("mwindow_sim_5_floors", "0"))
        self.lbl_key.setText(
            _translate(
                "mwindow_sim_5_floors",
                "(White blocks represent floors, and red blocks represent floors with the lift on it.)",
            )
        )
        self.lbl_num_in_lift.setText(
            _translate("mwindow_sim_5_floors", "Number of People in Lift: 0")
        )

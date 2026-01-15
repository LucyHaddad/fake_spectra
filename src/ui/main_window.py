from PySide6.QtWidgets import (QApplication, QMainWindow, QHBoxLayout, QVBoxLayout,
                            QLineEdit, QLabel, QWidget, QDoubleSpinBox,
                            QComboBox, QPushButton)
from PySide6.QtCore import Qt

from process.find_e0 import get_edges, get_e0
from process.make_bkg import make_background
from plotter import BasicPlot

class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        self.layout = QVBoxLayout()

        atsym_layout = QHBoxLayout()
        atsym_label = QLabel("Absorbing Atom:"); self.atsym_box = QLineEdit("", parent=self)
        self.atsym_box.setFixedWidth(100)
        edge_label = QLabel("Absorbing Edge: "); self.edge_box = QComboBox()
        nedge_label = QLabel("Num. Edges: "); self.edge_no = QComboBox()
        self.edge_no.addItems(["1", "2", "3"])

        self.atsym_box.editingFinished.connect(self.on_atsym_change)
        self.edge_box.currentIndexChanged.connect(self.on_edge_change)
        
        [atsym_layout.addWidget(w) for w in [atsym_label, self.atsym_box, edge_label,\
                                              self.edge_box, nedge_label, self.edge_no]]
        self.layout.addLayout(atsym_layout)

        energy_layout = QHBoxLayout()
        e_label = QLabel("Energy Ranges: ")
        energy_layout.addWidget(e_label)

        range_layout = QHBoxLayout()
        Elow_layout = QVBoxLayout()
        Elow_label = QLabel("Pre-edge"); self.Elow = QDoubleSpinBox(minimum=-100, maximum=-1, singleStep=5)
        self.Elow.setValue(-30)
        [Elow_layout.addWidget(w) for w in [Elow_label, self.Elow]]
        range_layout.addLayout(Elow_layout)
        
        Ehigh_layout = QVBoxLayout()
        Ehigh_label = QLabel("Post-edge"); self.Ehigh = QDoubleSpinBox(minimum=1, maximum=1000, singleStep=5)
        self.Ehigh.setValue(500)
        [Ehigh_layout.addWidget(w) for w in [Ehigh_label, self.Ehigh]]
        range_layout.addLayout(Ehigh_layout)

        self.Npoints = QLineEdit("1000"); Np_label = QLabel("Num. Points:")
        Npoints_layout = QHBoxLayout()
        [Npoints_layout.addWidget(w) for w in [Np_label, self.Npoints]]

        [energy_layout.addLayout(l) for l in [range_layout, Npoints_layout]]
        self.layout.addLayout(energy_layout)

        info_layout = QHBoxLayout(); self.info_text = QLabel(f"Current e0: , range: ")
        info_layout.addWidget(self.info_text, alignment=Qt.AlignmentFlag.AlignCenter)
        data_button = QPushButton("Generate some (f)XAS?")
        info_layout.addWidget(data_button, alignment=Qt.AlignmentFlag.AlignRight)
        self.layout.addLayout(info_layout)

        self.plot = BasicPlot(self)
        self.layout.addWidget(self.plot)

        self.setLayout(self.layout)
        self.Npoints.textChanged.connect(self._param_maker)
        self.edge_no.currentIndexChanged.connect(self._param_maker)
        [w.valueChanged.connect(self._param_maker) for w in [self.Elow, self.Ehigh]]
        data_button.pressed.connect(self.generate_xas)

    def on_atsym_change(self):
        atsym = self.atsym_box.text()
        try: edges = get_edges(atsym)
        except ValueError: return
        self.edge_box.clear()
        self.edge_box.addItems(edges)
    
    def on_edge_change(self):
        atsym = self.atsym_box.text()
        edge = self.edge_box.currentText()
        self.e0 = get_e0(atsym, edge)
        self._param_maker()
    
    def change_infotext(self):
        self.info_text.clear()
        ce0 = self.params["e0"]
        c_up = self.params["upper"]; c_low = self.params["lower"]
        c_npts = self.params["npoints"]; c_nedge = self.params["n_edge"]

        self.info_text.setText(f"Current e0: {ce0}, range: {c_low}-{c_up} eV, Npoints: {c_npts},\
                               num. edges: {c_nedge}")

    def _param_maker(self):
        self.params = {"atsym": self.atsym_box.text(),
                       "edge": self.edge_box.currentText(),
                       "e0": self.e0,
                       "lower": self.e0+self.Elow.value(),
                       "upper": self.e0+self.Ehigh.value(),
                       "pad_lower": int(self.Elow.value()),
                       "pad_upper": int(self.Ehigh.value()),
                       "npoints": int(self.Npoints.text()),
                       "n_edge": int(self.edge_no.currentText())}
        self.change_infotext()
    
    def generate_xas(self):
        bkg = make_background(self.params)
        self.plot.canvas.ax.clear()
        self.plot.canvas.ax.plot(bkg.energy, bkg.mu)
        self.plot.canvas.draw_idle()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        main_widget = MainWidget(self)
        self.setCentralWidget(main_widget)


app = QApplication([])
main = MainWindow()
if __name__ == "__main__":
    main.show()
    app.exec()



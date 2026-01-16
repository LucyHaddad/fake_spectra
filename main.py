from PySide6.QtWidgets import QApplication
from src.fake_spectra.ui.main_window import MainWindow

app = QApplication([])
main = MainWindow()
if __name__ == "__main__":
    main.show()
    app.exec()

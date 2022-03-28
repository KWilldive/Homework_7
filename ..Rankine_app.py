import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QCursor

from Rankine_GUI import Ui_Form
from Rankine import rankine  #importing classes

class main_window(QDialog):
    def __init__(self):
        super(main_window,self).__init__()

        self.useX = True


        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.assign_widgets()
        self.show()

    def assign_widgets(self):
        #self.ui.ExitButton.clicked.connect(self.ExitApp)
        self.ui.btn_Calculate.clicked.connect(self.Calculate)



    def Calculate(self):
        p_low = float(self.ui.le_PLow.text())
        p_high = float(self.ui.le_PHigh.text())
        t_high = float(self.ui.le_TurbineInletCondition.text())
        t_eff = float(self.ui.le_TurbineEff.text())

        if self.useX is True:
            r = rankine(p_low, p_high)
        else:
            r = rankine(p_low, p_high, t_high=t_high)

        eff = r.calc_efficiency()

        self.ui.le_TurbineInletCondition.setText('{:.1f}'.format(r.turbine_work))
        self.ui.le_PumpWork.setText('{:.1f}'.format(r.pump_work))
        self.ui.le_HeatAdded.setText('{:.1f}'.format(r.heat_added))
        self.ui.le_H1.setText('{:.1f}'.format(r.state1))
        self.ui.le_H2.setText('{:.1f}'.format(r.state2))
        self.ui.le_H3.setText('{:.1f}'.format(r.state3))
        self.ui.le_H4.setText('{:.1f}'.format(r.state4))
        self.ui.le_Efficiency.setText('{:.3f}'.format(eff))

        return


    def ExitApp(self):
        app.exit()

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())

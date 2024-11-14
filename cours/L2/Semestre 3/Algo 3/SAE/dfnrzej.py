import sys
from PySide2 import QtCore, QtGui, QtWidgets
class MaFenetre(QtWidgets.QDialog):
	def __init__(self, parent=None):
		QtWidgets.QDialog.__init__(self,parent)
		# Les cases à cocher
		self.__caseMinuscules = QtWidgets.QCheckBox("Minuscules")
		self.__caseMajuscules = QtWidgets.QCheckBox("Majuscules")
		self.__caseChiffres = QtWidgets.QCheckBox("Chiffres")
		self.__caseSymboles = QtWidgets.QCheckBox("Symboles")
		# Les boutons
		self.__boutonQuitter = QtWidgets.QPushButton("Quitter")
		self.__boutonCopier = QtWidgets.QPushButton("Vers le presse-papier")
		self.__boutonGenerer = QtWidgets.QPushButton("Générer")
		# Le champ de texte
		self.__champTexte = QtWidgets.QLineEdit("")
		# La glissière
		self.__glissiereTaille = QtWidgets.QSlider(QtCore.Qt.Horizontal)
		self.__glissiereTaille.setMinimum(8)
		self.__glissiereTaille.setMaximum(30)
		# Le label
		self.__labelTaille = QtWidgets.QLabel("Taille du mot de passe : " + str(self.__glissiereTaille.value()))
		layout = QtWidgets.QGridLayout()
		layout.addWidget(self.__caseMajuscules, 0, 0)
		layout.addWidget(self.__labelTaille, 0, 1)
		layout.addWidget(self.__caseMinuscules, 0, 2)
		layout.addWidget(self.__caseChiffres, 1, 0)
		layout.addWidget(self.__glissiereTaille, 1, 1)
		layout.addWidget(self.__caseSymboles, 1, 2)
		layout.addWidget(self.__champTexte, 2, 1)
		layout.addWidget(self.__boutonQuitter, 3, 0)
		layout.addWidget(self.__boutonCopier, 3, 1)
		layout.addWidget(self.__boutonGenerer, 3, 2)
		self.setLayout(layout)
		self.setWindowTitle("Générateur de mot de passe")
		icone = QtGui.QIcon()
		icone.addPixmap(QtGui.QPixmap("cadenas.svg"))
		self.setWindowIcon(icone)
		self.__caseMinuscules.setChecked(True)
		self.__caseChiffres.setChecked(True)
app = QtWidgets.QApplication(sys.argv)
dialog = MaFenetre()
dialog.exec_()
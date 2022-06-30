import sys
import webbrowser
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QToolBar
from PyQt5.uic import loadUi
import numpy as np
import bibtexparser
import pandas as pd
import subprocess
import pickle
import os

edge_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.exe %s'


class BibReader():
    def __init__(self):
        self.references = pd.DataFrame()
        self.cont = 0
        self.work_directory = os.getcwd()

    def update_data(self, file_name):
        columns = ['Control', 'Optimization', 'Type', 'Keyword1', 'Keyword2', 'Methodology', 'Results',
                   'Conclusions', 'pdf']
        self.references = pd.read_csv(file_name)
        for col in columns:
            self.references[col] = ''
        print(self.references)
        self.cont = 0


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("gui.ui", self)
        self.memory()
        self.browse.clicked.connect(self.browsefiles)
        self.next.clicked.connect(self.NextArticle)
        self.previous.clicked.connect(self.PrevArticle)
        self.discard.clicked.connect(self.DeleteArticle)
        self.sciHub.clicked.connect(self.OpenWebSciHub)
        self.google.clicked.connect(self.OpenWebGoogle)
        self.openFile.clicked.connect(self.OpenFile)
        self.directory.clicked.connect(self.working_folder)
        self.save.clicked.connect(self.Save)
        # self.progressBar.setValue(self.bibReader.cont / (self.bibReader.references['title'].count() - 1) * 100)
        # self.number.display(self.bibReader.cont)
        try:
            self.UpdateComboBox()
        except:
            print('Data frame error')
        self.UpdateArticle()

    def save_object(self):
        try:
            with open("__memory.pickle", "wb") as f:
                pickle.dump(self.bibReader, f, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            print("Error during pickling object (Possibly unsupported):", ex)

    def memory(self):
        try:
            with open("__memory.pickle", "rb") as f:
                self.bibReader = pickle.load(f)
        except:
            self.bibReader = BibReader()
            self.save_object()

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './', 'Bibtex (*.csv *.xlsx);; PDF (*.pdf)')
        self.filename.setText(fname[0])
        try:
            if fname[0].split('.')[-1] == 'pdf':
                self.bibReader.references['pdf'].iloc[self.bibReader.cont] = fname[0]
                print(self.bibReader.references['pdf'].iloc[self.bibReader.cont])
                self.openFile.setStyleSheet("background-color: rgb(0, 255, 0);")
                self.openFile.setEnabled(True)
            elif fname[0].split('.')[-1] == 'csv':
                self.bibReader.update_data(fname[0])
                self.UpdateArticle()
        except:
            print('Invalid FileName')
        self.Save()

    def NextArticle(self):
        self.Save()
        if self.bibReader.references['title'].count() - 1 > self.bibReader.cont:
            self.bibReader.cont += 1
            self.UpdateArticle()
        else:
            self.bibReader.cont = 0
            self.UpdateArticle()

    def PrevArticle(self):
        self.Save()
        if 0 < self.bibReader.cont:
            self.bibReader.cont -= 1
            self.UpdateArticle()
        else:
            self.bibReader.cont = self.bibReader.references['title'].count() - 1
            self.UpdateArticle()

    def OpenWeb(self):
        try:
            webbrowser.get(edge_path).open(self.bibReader.references['url'].iloc[self.bibReader.cont])
        except:
            print('Error')

    def OpenWebGoogle(self):
        try:
            webbrowser.get(edge_path).open('https://www.google.com/search?q=' + self.bibReader.references['doi'].iloc[
                self.bibReader.cont])
        except:
            print('Error')

    def OpenWebSciHub(self):
        try:
            webbrowser.get(edge_path).open('https://sci-hub.se/' + self.bibReader.references['doi'].iloc[
                self.bibReader.cont])
        except:
            print('Error')

    def OpenFile(self):
        print(self.bibReader.references['pdf'].iloc[self.bibReader.cont])
        subprocess.Popen(str(self.bibReader.references['pdf'].iloc[self.bibReader.cont]), shell=True)

    def DeleteArticle(self):
        self.bibReader.references.drop(self.bibReader.cont, inplace=True)
        self.bibReader.references.reset_index(inplace=True, drop=True)
        self.UpdateArticle()
        self.Save()

    def UpdateArticle(self):
        # Clear text fields in the GUI
        self.title.setPlainText('')
        self.keywords.setPlainText('')
        self.year.display(0)
        self.abstract_2.setPlainText('')
        # Update text fields in the GUI
        try:
            self.title.setPlainText(self.bibReader.references['title'].iloc[self.bibReader.cont])
        except:
            print('No title')
        try:
            self.keywords.setPlainText(self.bibReader.references['author_keywords'].iloc[self.bibReader.cont].replace('; ', '\n'))
        except:
            print('No keywords')
        try:
            self.year.display(int(self.bibReader.references['year'].iloc[self.bibReader.cont]))
        except:
            print('No year')
        try:
            self.abstract_2.setPlainText(self.bibReader.references['abstract'].iloc[self.bibReader.cont])
        except:
            print('No abstract')
        try:
            if self.bibReader.references['pdf'].iloc[self.bibReader.cont] != '':
                self.openFile.setStyleSheet("background-color: rgb(0, 255, 0);")
                self.openFile.setEnabled(True)
            else:
                self.openFile.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.openFile.setEnabled(False)
        except:
            print('No pdf path in the DataFrame')
        # Update number and bar progress
        self.progressBar.setValue(self.bibReader.cont / (len(self.bibReader.references['title']) - 1) * 100)
        self.number.display(self.bibReader.cont)
        try:
            self.control.setEditText(self.bibReader.references['Control'].iloc[self.bibReader.cont])
            self.optimization.setEditText(self.bibReader.references['Optimization'].iloc[self.bibReader.cont])
            self.type.setEditText(self.bibReader.references['Type'].iloc[self.bibReader.cont])
            self.k1.setEditText(self.bibReader.references['Keyword1'].iloc[self.bibReader.cont])
            self.k2.setEditText(self.bibReader.references['Keyword2'].iloc[self.bibReader.cont])
            self.methodology.setText(self.bibReader.references['Methodology'].iloc[self.bibReader.cont])
            self.results.setText(self.bibReader.references['Results'].iloc[self.bibReader.cont])
            self.conclusions.setText(self.bibReader.references['Conclusions'].iloc[self.bibReader.cont])
        except:
            print('Dataframe error')
        self.save_object()

    def Save(self):
        self.bibReader.references['Control'].iloc[self.bibReader.cont] = self.control.currentText()
        if (self.control.findText(self.control.currentText()) == -1) & (self.control.currentText() != ''):
            self.control.addItem(self.control.currentText())
        self.bibReader.references['Optimization'].iloc[self.bibReader.cont] = self.optimization.currentText()
        if (self.optimization.findText(self.optimization.currentText()) == -1) & (
                self.optimization.currentText() != ''):
            self.optimization.addItem(self.optimization.currentText())
        self.bibReader.references['Type'].iloc[self.bibReader.cont] = self.type.currentText()
        if (self.type.findText(self.type.currentText()) == -1) & (self.type.currentText() != ''):
            self.type.addItem(self.type.currentText())
        self.bibReader.references['Keyword1'].iloc[self.bibReader.cont] = self.k1.currentText()
        if (self.k1.findText(self.k1.currentText()) == -1) & (self.k1.currentText() != ''):
            self.k1.addItem(self.k1.currentText())
        self.bibReader.references['Keyword2'].iloc[self.bibReader.cont] = self.k2.currentText()
        if (self.k2.findText(self.k2.currentText()) == -1) & (self.k2.currentText() != ''):
            self.k2.addItem(self.k2.currentText())
        self.bibReader.references['Methodology'].iloc[self.bibReader.cont] = self.methodology.toPlainText()
        self.bibReader.references['Results'].iloc[self.bibReader.cont] = self.results.toPlainText()
        self.bibReader.references['Conclusions'].iloc[self.bibReader.cont] = self.conclusions.toPlainText()

    def UpdateComboBox(self):
        for row in self.bibReader.references['Control'].drop_duplicates():
            if (row != ''):
                self.control.addItem(row)
        for row in self.bibReader.references['Optimization'].drop_duplicates():
            if (row != ''):
                self.optimization.addItem(row)
        for row in self.bibReader.references['Type'].drop_duplicates():
            if (row != ''):
                self.type.addItem(row)
        for row in self.bibReader.references['Keyword1'].drop_duplicates():
            if (row != ''):
                self.k1.addItem(row)
        for row in self.bibReader.references['Keyword2'].drop_duplicates():
            if (row != ''):
                self.k2.addItem(row)

    def working_folder(self):
        fname = QFileDialog.getExistingDirectory(self, "Open Directory", './')
        f = open(fname + '/' + self.lineEdit1.currentText() + '.csv', 'w')
        print(fname)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setMinimumWidth(1010)
    widget.setMinimumHeight(586)
    widget.setWindowTitle('Bib Reader')
    widget.show()
    sys.exit(app.exec_())

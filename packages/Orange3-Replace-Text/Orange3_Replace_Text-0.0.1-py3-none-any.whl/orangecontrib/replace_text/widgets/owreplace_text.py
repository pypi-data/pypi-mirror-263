from AnyQt.QtCore import Qt
from orangecontrib.text import Corpus
from Orange.data import StringVariable
from Orange.widgets import gui
from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget
from Orange.widgets.utils.signals import Input, Output
from Orange.widgets.utils.widgetpreview import WidgetPreview

from os.path import basename
from re import sub

from AnyQt.QtWidgets import (
    QLabel, QComboBox, QPushButton, QDialog, QDialogButtonBox, QGridLayout,
    QVBoxLayout, QSizePolicy, QStyle, QFileIconProvider, QFileDialog,
    QApplication, QMessageBox, QTextBrowser, QMenu
)
from Orange.widgets.utils.combobox import ItemStyledComboBox

debug = None

class OWReplaceText(OWWidget):
    name = "Replace Text"
    description = "Replaces Text"
    icon = "icons/replace_text.svg"
    priority = 80
    keywords = "text"
    
    want_main_area = False
    resizing_enabled = False

    use_regexp       = Setting(False)
    recentFiles      = Setting([])
    replaceColumn    = Setting("")
    
    class Inputs:
        corpus = Input("Corpus", Corpus)
        
    class Outputs:
        corpus = Output("Corpus", Corpus)
        
    want_main_area = False
    
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        
        self.replacements_index = 0
        self.columns_index = 0
        self.data = None
        self.column = self.replaceColumn
        self.updated_corpus = None
        self.columns = []
        self.replacements = None
        self.regex_check = False
        
        
        hb = gui.widgetBox(self.controlArea, orientation=Qt.Horizontal)
        hb = gui.hBox(self.controlArea, "Replacements")
        layout = QGridLayout()
        layout.setVerticalSpacing(5)
        layout.setColumnStretch(2,1)
        layout.setColumnMinimumWidth(1,15)
        
        ROW = 0
        COLUMNS = 3

        def add_row(label, items):
            nonlocal ROW, COLUMNS
            layout.addWidget(QLabel(label), ROW, 0)
            if isinstance(items, tuple):
                for i, item in enumerate(items):
                    layout.addWidget(item, ROW, 1 + i)
            else:
                layout.addWidget(items, ROW, 1, 1, COLUMNS - 1)
            ROW += 1
            
        self.filecombo = gui.comboBox(
            hb, self, "replacements_index", callback=self.select_replacements_file,
            minimumWidth=250)
        
        self.columnscombo = gui.comboBox(
            hb, self, "columns_index", callback=self.select_column
        )
        
        self.regexcheck = gui.checkBox(
            hb, self, "regex_check", label='regex', callback=self.check_regex
        )
        
        add_row(
            "Replacements File",
            (
                self.filecombo,
                gui.button(
                    hb, self, '...', callback=self.browse_replacements_file, disabled=0,
                    icon=self.style().standardIcon(QStyle.SP_DirOpenIcon),
                    sizePolicy=(QSizePolicy.Maximum, QSizePolicy.Fixed))
            )
        )
        
        add_row(
            "Use Regular Expressions",
            self.regexcheck
        )
        add_row(
            "Column",
            self.columnscombo
        )
        
        add_row(
            "Reload",
            gui.button(
                hb, self, 'Reload', callback=self.reload,
                icon=self.style().standardIcon(QStyle.SP_BrowserReload),
                sizePolicy=(QSizePolicy.Maximum, QSizePolicy.Fixed))
        )
        
        hb.layout().addLayout(layout)
 
        self.reload()
        
    @Inputs.corpus
    def set_data(self, data: Corpus):
        self.data = data
        self.update_columns(data)
        self.process()
        self.send_output()
        
    def browse_replacements_file(self, browse_demos=False):
        """user pressed the '...' button to manually select a file to load"""
        startfile = self.recentFiles[0] if self.recentFiles else '.'

        filename, _ = QFileDialog.getOpenFileName(
            self, 'Open a Replacements File', startfile,
            ';;'.join(("Replacements files (*.txt)",)))
        if not filename:
            return False

        if filename in self.recentFiles:
            self.recentFiles.remove(filename)
        self.recentFiles.insert(0, filename)

        self.populate_comboboxes()
        self.replacements_index = 0
        self.select_replacements_file()
        return True

    def populate_comboboxes(self):
        self.filecombo.clear()
        for file in self.recentFiles or ("(None)",):
            self.filecombo.addItem(basename(file))
        self.filecombo.addItem("Browse documentation STIX bundles...")
        self.filecombo.updateGeometry()

    def reload(self):
        if self.recentFiles:
            self.select_replacements_file()

    def update_columns(self, data: Corpus):
        if data is None:
            return
        self.columns = [x.name for x in data.domain.metas if isinstance(x, StringVariable)]
        self.columnscombo.clear()
        for col in self.columns:
            self.columnscombo.addItem(col)
        
    def select_column(self):
        self.column = self.columns[self.columns_index]
        self.replaceColumn = self.column
        
    def check_regex(self):
        self.use_regexp = self.regex_check
    
    def select_replacements_file(self):
        """user selected a replacements file from the combo box"""
        if self.replacements_index > len(self.recentFiles) - 1:
            if not self.browse_replacements_file(True):
                return  # Cancelled
        elif self.replacements_index:
            self.recentFiles.insert(0, self.recentFiles.pop(self.replacements_index))
            self.replacements_index = 0
            self.populate_comboboxes()
        if self.recentFiles:
            self.open_replacements_file(self.recentFiles[0])
            
    def open_replacements_file(self, filename):
        try:
            self.replacements = self.read_replacements(filename)
            self.recentFiles.insert(0, filename)
            self.process()
            self.send_output()
        except OSError as err:
            print(e)
        
    def read_replacements(self, filename):
        try:
            replacements = []
            with open(filename, 'r', encoding='UTF-8') as fh:
                for line in fh.readlines():
                    find, repl = line.strip().split('\t', 1)
                    replacements.append( (find, repl) )
            return replacements
        except Exception as e:
            print(e)
            
    def process(self):
        if self.replacements and self.data and self.column:
            def replacer(text):
                for repl in self.replacements:
                    if self.regex_check:
                        text = sub(repl[0], repl[1], text)
                    else:
                        text = text.replace(repl[0], repl[1])
                return text
            
            self.updated_corpus = self.data.copy()
            df = self.updated_corpus.metas_df
            df[self.column] = df[self.column].apply(replacer)
            self.updated_corpus.metas_df = df
            
    def send_output(self):
        self.Outputs.corpus.send(self.updated_corpus)
            
if __name__ == "__main__":  # pragma: no cover
    WidgetPreview(OWReplaceText).run(Corpus("grimm-tales-selected"))

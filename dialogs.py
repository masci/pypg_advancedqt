'''

@author: masci
'''
from windowmeta import *
from mixinutils import *
from itemselector import ItemSelector
from PyQt4.QtGui import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from PyQt4.QtGui import QStandardItemModel, QPushButton, QComboBox

class SelectItemsMixin(object):
    """ 
    """   
    def setupMixin (self, **kwargs):
        parent = kwargs.pop('parent', None)
        self._selector = ItemSelector(QStandardItemModel(), parent)
        self._selector.setLabel('My Recurrent Items')
        self.layout().insertWidget(0, self._selector)
    
    @property
    def selection(self):
        """Return a list of selected items"""
        return [x for x in self._selector.selectedItems()]

class SpecializedDialogOne(QDialog):
    """
    """
    def __init__ (self, parent=None):
        QDialog.__init__(self)
        layout = QVBoxLayout(self)
        sublayout = QHBoxLayout()
        self.label = QLabel("Put your value here:", self)
        self.text = QLineEdit(self)
        self.button = QPushButton("Close",self)
        self.button.clicked.connect(self.close)
        sublayout.addWidget(self.label)
        sublayout.addWidget(self.text)
        sublayout.addWidget(self.button)
        layout.addLayout(sublayout)
        self.setLayout(layout)
        
        self.setupMixin()
    
    @property
    def my_property(self):
        return self.text.text()
mixIn(SpecializedDialogOne, SelectItemsMixin)

class SpecializedDialogTwo(QDialog):
    """
    
    """
    def __init__ (self, parent=None):
        QDialog.__init__(self)
        layout = QVBoxLayout(self)
        sublayout = QHBoxLayout()
        self.label = QLabel("Select your value here:", self)
        self.combo = QComboBox(self)
        self.combo.addItems(('One','Two'))
        self.button = QPushButton("Close",self)
        self.button.clicked.connect(self.close)
        sublayout.addWidget(self.label)
        sublayout.addWidget(self.combo)
        sublayout.addWidget(self.button)
        layout.addLayout(sublayout)
        self.setLayout(layout)
        
        self.setupMixin()
    
    @property
    def my_property(self):
        return self.text.text()
mixIn(SpecializedDialogTwo, SelectItemsMixin)

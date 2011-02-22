from PyQt4 import QtCore
from PyQt4.QtGui import QItemSelectionModel 
from windowmeta import WindowMeta


class ItemSelector(object):
    """This class implements a widget showing a list of items attached to a 
    certain qt model.
    
    """
    __metaclass__ = WindowMeta
    
    selectionChanged = QtCore.pyqtSignal()
    loadSelectionRequested = QtCore.pyqtSignal()
    
    def __init__ (self, model, parent=None):
        self._qt_base.__init__(self, parent)
        self.setupUi(self)
        
        self._model = model
        self.itemsTable.setModel(self._model)
        
        self.itemsTable.selectionModel().selectionChanged.connect(self.selectionChanged)
    
    def invertSelection(self):
        sm = self.itemsTable.selectionModel()
        for i in xrange(self._model.rowCount()):
            sm.select(self._model.index(i,0), 
                      QItemSelectionModel.Rows | QItemSelectionModel.Toggle)
    
    def setSelection(self, items):
        sm = self.itemsTable.selectionModel()
        sm.clearSelection()
        for item in items:
            index = self._model.indexFromItem(item)
            sm.select(index, QItemSelectionModel.Rows|QItemSelectionModel.Select)
    
    def setLabel(self, text):
        self.groupBox.setTitle(text)

    def selectedItems(self):
        sm = self.itemsTable.selectionModel()
        for index in sm.selectedRows(self._selectionColumn):
            yield index.model().itemFromIndex(index)

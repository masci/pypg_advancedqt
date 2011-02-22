# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
"""
import os
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import Qt

if __name__ == "__main__":
    sys.path[0:0] = [
        os.path.join(os.path.dirname(sys.argv[0]),'meta'),
        os.path.join(os.path.dirname(sys.argv[0]),'mixins'),
        os.path.join(os.path.dirname(sys.argv[0]),'uis'),
    ]
    from dialogs import SpecializedDialogOne, SpecializedDialogTwo

    # start QApplication    
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)

    dlg = SpecializedDialogOne()
    dlg.setAttribute(Qt.WA_DeleteOnClose)
    dlg.show()

    another_dlg = SpecializedDialogTwo()
    another_dlg.setAttribute(Qt.WA_DeleteOnClose)
    another_dlg.show()
    
    sys.exit(app.exec_())

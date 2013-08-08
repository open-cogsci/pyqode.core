"""
Contains the text block user data structure
"""
from pcef.qt import QtGui


class TextBlockUserData(QtGui.QTextBlockUserData):
    def __init__(self):
        QtGui.QTextBlockUserData.__init__(self)
        self.lineNumber = -1
        # specify if the block is folded
        self.folded = False
        # specify if the block is the fold start
        self.foldStart = False
        self.foldIndent = -1
        self.marker = None
        self.parenthesisInfos = []

    def __repr__(self):
        return ("#{} - Folded: {}  FoldIndent: {} - FoldStart: {}"
                "- Marker: {} - Parenthesis: {}"
                "".format(self.lineNumber, self.folded, self.foldIndent,
                          self.foldStart, self.marker, self.parenthesisInfos))
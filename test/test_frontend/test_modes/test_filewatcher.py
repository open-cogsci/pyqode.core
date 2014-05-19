import os
from pyqode.qt import QtCore
from pyqode.qt import QtWidgets
from pyqode.qt.QtTest import QTest
import datetime
from pyqode.core import frontend
from pyqode.core.frontend import modes
from test.helpers import editor_open, preserve_settings


file_path = os.path.join(
    os.getcwd(), 'test', 'test_frontend', 'test_modes', 'file_to_watch.txt')


def setup_module():
    with open(file_path, 'w') as f:
        f.write("test file initial")


def teardown_module():
    os.remove(file_path)


def get_mode(editor):
    return frontend.get_mode(editor, modes.FileWatcherMode)


@editor_open(file_path)
def test_enabled(editor):
    mode = get_mode(editor)
    assert mode.enabled
    mode.enabled = False
    mode.enabled = True


@editor_open(file_path)
@preserve_settings
def test_modif_accept_with_focus(editor):
    mode = get_mode(editor)
    mode.auto_reload = False
    with open(file_path, 'r') as f:
        with open(file_path, 'w') as f2:
            f2.write("test file %s" % datetime.datetime.now())
    editor.setFocus(True)
    QtCore.QTimer.singleShot(1500, accept_mbox)
    # wait for the message box to appear
    QTest.qWait(1000)


@editor_open(file_path)
def test_modif_reject_with_focus(editor):
    mode = get_mode(editor)
    mode.auto_reload = False
    with open(file_path, 'r') as f:
        with open(file_path, 'w') as f2:
            f2.write("test file %s" % datetime.datetime.now())
    editor.setFocus(True)
    QtCore.QTimer.singleShot(1500, reject_mbox)
    # wait for the message box to appear
    QTest.qWait(1000)


@editor_open(file_path)
def test_modif_without_focus(editor):
    mode = get_mode(editor)
    mode.auto_reload = False
    win = QtWidgets.QMainWindow()
    win.show()
    QTest.qWaitForWindowActive(win)
    with open(file_path, 'r') as f:
        with open(file_path, 'w') as f2:
            f2.write("test file %s" % datetime.datetime.now())
    QtCore.QTimer.singleShot(1500, accept_mbox)
    # wait for the filewatcher to detect the changed
    QTest.qWait(500)
    QtWidgets.QApplication.instance().setActiveWindow(editor)
    # wait for the message box to appear
    QTest.qWait(500)


def accept_mbox():
    widgets = QtWidgets.QApplication.instance().topLevelWidgets()
    for w in widgets:
        if isinstance(w, QtWidgets.QMessageBox):
            QTest.keyPress(w, QtCore.Qt.Key_Space)

def reject_mbox():
    widgets = QtWidgets.QApplication.instance().topLevelWidgets()
    for w in widgets:
        if isinstance(w, QtWidgets.QMessageBox):
            QTest.keyPress(w, QtCore.Qt.Key_Escape)


@editor_open(file_path)
@preserve_settings
def test_modif_autoreload(editor):
    mode = get_mode(editor)
    mode.auto_reload = False
    mode = get_mode(editor)
    mode.auto_reload = True
    with open(file_path, 'r') as f:
        with open(file_path, 'w') as f2:
            f2.write("test file %s" % datetime.datetime.now())
    QTest.qWait(1000)


@editor_open(file_path)
@preserve_settings
def test_delete(editor):
    mode = get_mode(editor)
    mode.auto_reload = False
    os.remove(file_path)
    QTest.qWait(1000)
    with open(file_path, 'w') as f:
        f.write("test file initial")
    frontend.open_file(editor, file_path)


@editor_open(file_path)
@preserve_settings
def test_none_filepath(editor):
    mode = get_mode(editor)
    mode.auto_reload = False
    mode.auto_reload = False
    p = editor.file_path
    editor.file_path = None
    mode._update_mtime()
    editor.file_path = p


@editor_open(file_path)
@preserve_settings
def test_non_existing_file_path(editor):
    mode = get_mode(editor)
    mode.auto_reload = False
    p = editor.file_path
    editor.file_path = '/usr/blah/foo/bar.txt'
    mode._update_mtime()
    editor.file_path = p

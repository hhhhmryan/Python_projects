from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineOnlyReceiver


class ConnectorProtocol(LineOnlyReceiver):
    factory: 'Connector'

    def connectionMade(self):
        self.factory.window.protocol = self
        self.factory.window.plainTextEdit.appendPlainText("Connected")

    def lineReceived(self, line):
        self.factory.window.plainTextEdit.appendPlainText(line.decode())


class Connector(ClientFactory):
    protocol =  ConnectorProtocol
    window: 'ExampleApp'

    def __init__(self, window) -> None:
        self.window = window



import sys
from PyQt5 import QtWidgets
from design import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    reactor = None
    protocol: ConnectorProtocol

    def __init__(self):
        super().__init__()
        self.setupUI(self)
        self.init_handlers()

    def init_handlers(self):
        self.pushButton.clicked.connect(self.send_message)

    def send_message(self):
        message = self.lineEdit.text()
        #self.plainTextEdit.sppendPlainText(message)
        self.protocol.sendLine(message.encode())
        self.lineedit.clear()


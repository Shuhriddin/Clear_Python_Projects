import threading
import time

import pika
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

name1 = ''
name2 = ''


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.name, ok = QInputDialog.getText(self, 'Welcome!', 'Input a nickname:')
        self.label = QtWidgets.QLabel("login: " + str(self.name))
        global name1
        name1 = str(self.name)
        self.label1 = QtWidgets.QLabel("People online:")
        self.newfont = QtGui.QFont("Times", 10)
        self.label.setFont(self.newfont)
        self.listch = QtWidgets.QListWidget()
        self.listch.itemClicked.connect(self.itemcl)
        self.textchat = QtWidgets.QTextEdit()
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.btn1 = QtWidgets.QPushButton("Send a message")
        self.texted = QtWidgets.QTextEdit()
        self.vbox = QtWidgets.QGridLayout()
        self.vbox.addWidget(self.label, 0, 0)
        self.vbox.addWidget(self.label1, 0, 1)
        self.vbox.addWidget(self.listch, 1, 1)
        self.vbox.addWidget(self.textchat, 1, 0)
        self.vbox.addWidget(self.btn1, 2, 0)
        self.vbox.addWidget(self.texted, 3, 0)
        self.vbox.setColumnStretch(0, 2)
        self.vbox.setColumnStretch(1, 1)
        self.setLayout(self.vbox)

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        self.btn1.clicked.connect(self.btn1Clicked)

        p = self.texted.viewport().palette()

        self.texted.viewport().setPalette(p)

        p1 = self.textchat.viewport().palette()

        self.textchat.viewport().setPalette(p1)
        self.newfont1 = QtGui.QFont("Times", 7, QtGui.QFont.Bold)
        self.textchat.setFont(self.newfont1)
        self.texted.setFont(self.newfont1)

        self.lcl = list('')

        t = threading.Thread(target=self.Connect, args=(True,))
        t.daemon = True
        t.start();

    def Connect(self, check):
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='logs',
                                      exchange_type='fanout')

        self.result = self.channel.queue_declare(queue='',exclusive=True
                                                 )
        self.queue_name = ''

        self.channel.queue_bind(exchange='logs',
                                queue=self.queue_name)

        def callback(ch, method, properties, body):
            print(" [x] %r" % body.decode("utf-8"))
            self.textchat.append("%r" % body.decode("utf-8"))
            print(method.routing_key)

            if (self.lcl.count(method.routing_key) == 0):
                self.lcl.append(method.routing_key)
                self.listch.addItem(method.routing_key)
            print(self.lcl)

        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=callback, auto_ack=True)

        self.channel.start_consuming()

        if (check):
            self.channel.start_consuming()
        else:
            self.connection.close()

    def btn1Clicked(self):

        self.channel.basic_publish(exchange='logs', routing_key=str(self.name),  # routing_key можно изменять
                                   body=time.strftime("%H:%M:%S ") + str(self.name) + ': ' + self.texted.toPlainText())
        self.texted.clear()

    def itemcl(self, item):
        print('dialog opened ' + item.text())
        if (item.text() == str(self.name)):
            print('Error')
        else:
            print('dialog started with ' + item.text())
            global name2
            name2 = item.text()
            self.window2 = MyWindow2()
            self.window2.show()


class MyWindow2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        global name1
        global name2
        self.label = QtWidgets.QLabel(name1 + " ==> " + name2)
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.textchat = QtWidgets.QTextEdit()
        self.btn1 = QtWidgets.QPushButton("Send message")
        self.texted = QtWidgets.QTextEdit()
        self.vbox = QtWidgets.QGridLayout()
        self.vbox.addWidget(self.label, 0, 0)
        self.vbox.addWidget(self.textchat, 1, 0)
        self.vbox.addWidget(self.btn1, 2, 0)
        self.vbox.addWidget(self.texted, 3, 0)
        self.setLayout(self.vbox)
        self.setWindowTitle("Dialog")
        self.resize(600, 600)
        p = self.texted.viewport().palette()

        self.texted.viewport().setPalette(p)

        p1 = self.textchat.viewport().palette()

        self.textchat.viewport().setPalette(p1)
        self.newfont1 = QtGui.QFont("Times", 7, QtGui.QFont.Bold)
        self.textchat.setFont(self.newfont1)
        self.texted.setFont(self.newfont1)
        self.name = min(name1, name2) + max(name1, name2)

        print('dialog id: ' + self.name)

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue=self.name)

        t = threading.Thread(target=self.Connect, args=(True,))
        t.daemon = True
        t.start();

        self.btn1.clicked.connect(self.btn1Clicked)

    def btn1Clicked(self):

        self.channel.basic_publish(exchange='', routing_key=self.name,
                                   body=time.strftime("%H:%M:%S ") + name1 + ': ' + self.texted.toPlainText(),
                                   properties=pika.BasicProperties(
                                       delivery_mode=2, ))
        self.channel.basic_publish(exchange='', routing_key=self.name,
                                   body=time.strftime("%H:%M:%S ")+ name1 + ': ' + self.texted.toPlainText(),
                                   properties=pika.BasicProperties(
                                       delivery_mode=2, ))
        #self.texted.clear()

    def Connect(self, check):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=self.name)

        def callback(ch, method, properties, body):
            self.textchat.append("%r" % body.decode("utf-8"))

        channel.basic_consume(
            queue=self.name, on_message_callback=callback)

        channel.start_consuming()

        if (check):
            self.channel.start_consuming()
        else:
            self.connection.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Chat")
    window.resize(500, 200)

    window.show()
    sys.exit(app.exec_())
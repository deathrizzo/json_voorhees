import sys
import os
import PyQt5
import PyQt5.QtCore
#import PyQt5.QtWidgets.QApplication
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QTextEdit, QComboBox, QPushButton
from PyQt5.QtGui import QIcon
import json
import requests


#Create the window

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('Json Voorhees')
w.setWindowIcon(QIcon('/icons/jason.png'))
vbox = QVBoxLayout()

# Create textbox
txtApiKey = QLineEdit(w)
txtApiKey.setEchoMode(QLineEdit.Password)
#txtApiKey = QLineEdit(w)
txtBaseDomain = QLineEdit(w)
txtSendingDomain = QLineEdit(w)
txtRcptEmail = QLineEdit(w)
txtBinding = QLineEdit(w)


# Set window size.
w.resize(320, 150)


l1 = QLabel('API Key')
l2 = QLabel('Base domain')
l3 = QLabel('Sending Domain')
l4 = QLabel('Recipient Email')
l5 = QLabel('Binding')


#logOutput = QTextEdit()
#logOutput.setReadOnly(True)
logOutput = QTextEdit()
logOutput.setReadOnly(True)
logOutput.setLineWrapMode(QTextEdit.NoWrap)


font = logOutput.font()
font.setFamily("Courier")
font.setPointSize(10)





button = QPushButton('Send Test Email', w)
button2 = QPushButton('Exit', w)
button2.clicked.connect(app.exit)


vbox.addWidget(l1)
vbox.addWidget(txtApiKey)
vbox.addWidget(l2)
vbox.addWidget(txtBaseDomain)
vbox.addWidget(l3)
vbox.addWidget(txtSendingDomain)
vbox.addWidget(l4)
vbox.addWidget(txtRcptEmail)
vbox.addWidget(l5)
vbox.addWidget(txtBinding)


vbox.addWidget(logOutput)
vbox.addWidget(button)
vbox.addWidget(button2)

w.setLayout(vbox)




def on_click():
    hf = "John Doe"
    api_key = str(txtApiKey.text())
    base_domain = str(txtBaseDomain.text())
    sending_domain = str(txtSendingDomain.text())
    binding = str(txtBinding.text())
    rcpt_email = str(txtRcptEmail.text())
    static = "jdoe@" + str(txtSendingDomain.text())
    print(api_key)
    print(base_domain)
    print(sending_domain)
    print(binding)
    print(rcpt_email)
    print(static)
    message = "Injected to: {}\n" \
              "Sending domain: {}\n" \
              "Binding Group: {}\n" \
              "Recipient: {}\n" \
              "CHECK YOUR MOTHER FUCKING INBOX!".format(base_domain, sending_domain, binding, rcpt_email)
    print(message)

    with open("payload.json", "w") as payload:
        json.dump({"options": {"open_tracking": True,"click_tracking": True,"conversion_tracking": False},"campaign_id": "CampaignN","return_path": static,"header_from": hf,"recipients": [{"address": {"email": rcpt_email,"name": hf},"return_path": static,"substitution_data": {"firstName": "John","age": 19,"member": True},"tags": ["christmas", "newyear", "clothing", "special1214"],"metadata": {"place": "Columbia"}}],"content": {"from": {"email": static},"headers": {"X-Binding": binding},"subject": "Welcome from Demo Env 022415 - test 4:18","text": "This is the text part\n","html": "<html><body>hello {{firstName}}<br>\n<a href=\"http://www.animaljam.com\">click on link A</a><br>\n{{if age < 50}}lucky guy{{end}}\n</body>\n</html>"}},payload, indent=4)
    payload.close()

#    with open("payload.json", "r") as payload:
#        result = json.load(payload)
#    payload.close()

#    print (type(result))
#    print (result.keys())
#    print (result)

    url = "https://{}/api/v1/transmissions/".format(base_domain)
    headers = {'Authorization': api_key, 'Accept': 'application/json', 'Content-Type':'application/json'}
    contents = open('payload.json', 'rb').read()
    r = requests.post(url, data=contents, headers=headers)
    r.json()
    logOutput.setPlainText(message)
    os.remove("payload.json")
button.clicked.connect(on_click)
w.show()
app.exec_()


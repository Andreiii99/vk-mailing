from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import randint as r
import vk_mailing_gui
import vk_api
import sys

class App(QWidget, vk_mailing_gui.Ui_vkmailing):
    def __init__(self):
        super().__init__()
        self.ui = vk_mailing_gui.Ui_vkmailing()
        self.ui.setupUi(self)
        self.ui.btn_send.clicked.connect(self.send_message)
        self.ui.btn_exit.clicked.connect(self.exiting)

        login = QInputDialog.getText(self, 'Auth', 'VK login: ')[0]
        password = QInputDialog.getText(self, 'Auth', 'VK password: ')[0]

        app_id = '2685278' # Kate Mobile App ID (messages.send bypass)
    
        try:
            vk_session = vk_api.VkApi(login, password, app_id=app_id)
            vk_session.auth()
        except vk_api.exceptions.BadPassword:
            QMessageBox.about(self, 'Error', 'Bad password!'); exit()
        except vk_api.exceptions.AuthError:
            vk_session = vk_api.VkApi(login, password, app_id=app_id, auth_handler=lambda: [QInputDialog.getText(self, 'Two-Factor Auth', 'Two-Factor auth code: '), False])
            vk_session.auth()

        self.vk = vk_session.get_api()

        self.ui.lbl_status.setText(f'[Online] {self.vk.users.get()[0]["first_name"]} {self.vk.users.get()[0]["last_name"]}, ID:{self.vk.users.get()[0]["id"]}')

    def send_message(self): 
        self.receivers = self.ui.txtedit_links.toPlainText().split('\n')
        QMessageBox.about(self, '', str(self.receivers))
        if len(self.receivers) == 1 and self.receivers[0] == '':
            QMessageBox.about(self, 'Error', 'No receivers!'); return 0
        self.message = self.ui.txtedit_msg.toPlainText()
        if self.message == '':
            QMessageBox.about(self, 'Error', 'Message is empty'); return 0
        self.random_id = r(-9223372036854775808, 9223372036854775807)
        for k in self.receivers:
            self.vk.messages.send(user_id=self.vk.utils.resolveScreenName(screen_name=k.strip().split('/')[-1])['object_id'], random_id=self.random_id, message=str(self.message))

    def exiting(self):
        QMessageBox.about(self, 'Good bye!', 'See you later, username :D \n\t- Oleg Voevodin'); exit()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

import sqlite3


class Functions:
    def __init__(self):
        conn = sqlite3.connect('root.db')
        self.c = conn.cursor()
        self.user_id = str()
        self.user_name = str()
        self.permission = str()

    def login(self, username: str, password: str):
        sen = "select ID, PERMISSION from USER where USER.NAME = '%s' and USER.PASSWORD = '%s'" % (username, password)
        self.c.execute(sen)
        info = self.c.fetchall()
        info = list(info[0])

        if len(info) == 0:
            return 0
        else:
            self.user_id = info[0]
            self.user_name = username
            self.permission = info[1]
            return 1

    def enter_question(self, content: str, answer: str):
        pass

    def revise_question(self, q_id: str, u_id: str, permission: str):
        pass

    def search_question(self, words: str):
        pass

    def make_paper(self, q_id, content):
        '''将选定的题id和内容保存在本地文本中'''
        pass


if __name__ == "__main__":
    f = Functions()
    login = f.login('Robert Garza', 'plP3wihDfH')
    if login == 0:
        print('User not exist')
    elif login == 1:
        print('Login successfully')

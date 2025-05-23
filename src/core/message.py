import threading
from datetime import datetime

class Message:
    def __init__(self, username, data, time):
        self.username = username
        self.data = data
        self.time = time

    def format(self): # [username]:[message]:[timesent]
        return f"{self.username}:\n{self.data}\n[@{self.time}]"

    def raw(self):
        return b"{}:\n{}\n[@{}]\n".format(self.username, self.data, self.time)

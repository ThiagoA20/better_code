from .database import createDatabaseConnection
from .webserver import createWebserver


class createCore:

    def __init__(self):
        self.database = createDatabaseConnection()
        self.webserver = createWebserver()

    def start(self):
        print("[Core] Starting...")
        self.database.start()
        self.webserver.start()
        print("[Core] System running!")

    def stop(self):
        print("[Core] Stopping...")
        self.webserver.stop()
        self.database.stop()
        print("[Core] the system has stoped!")